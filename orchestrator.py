import os
import json
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai # Modern 2026 SDK
import time

# Load secure configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# 1. Setup Modern Gemini Client
client = genai.Client(api_key=config["GEMINI_API_KEY"])
model_id = config["MODEL_NAME"]

# 2. Define the MCP Server Parameters (Windows friendly)
server_params = StdioServerParameters(
    command="python", # Changed from python3 for Windows
    args=["mcp_server.py"], 
)

async def run_conversion_pipeline():
    print("Connecting to Local Engineering Gateway...")
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("✅ Gateway Connected.")
                
                perl_dir = config["PERL_CODEBASE"]
                scripts = [f for f in os.listdir(perl_dir) if f.endswith('.pl')]

                for script in scripts:
                    print(f"\n--- Processing: {script} ---")

                    try:
                      # 1. Read via MCP
                      mcp_response = await session.call_tool("read_perl_script", {"filename": script})
                      perl_content = mcp_response.content[0].text

                      # 2. RAG Core Logic
                      prompt = f"Convert this Perl code to Python with 100% parity. Return ONLY the code:\n\n{perl_content}"
                      response = client.models.generate_content(model=model_id, contents=prompt)
                      python_code = response.text

                      # Clean up code...
                      if "```python" in python_code:
                          python_code = python_code.split("```python")[1].split("```")[0].strip()
                      elif "```" in python_code:
                          python_code = python_code.split("```")[1].split("```")[0].strip()
                      else:
                          python_code = python_code.strip()

                      # 3. Write via MCP
                      python_filename = script.replace(".pl", ".py")
                      await session.call_tool("write_python_script", {
                          "filename": python_filename, 
                          "code": python_code
                      })

                      # 4. Validation
                      mcp_val_response = await session.call_tool("run_validation_test", {})
                      print(f"✅ Result: {mcp_val_response.content[0].text}")

                      # SUCCESS DELAY: Wait 15 seconds between successful scripts
                      print("Waiting 15s to respect API rate limits...")
                      time.sleep(15)

                    except Exception as e:
                      if "429" in str(e):
                          print("❌ Quota Exhausted. Cooling down for 45 seconds...")
                          time.sleep(45) 
                      else:
                          print(f"⚠️ Error processing {script}: {str(e)}")
                      continue

    except Exception as e:
        print(f"❌ Critical Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(run_conversion_pipeline())