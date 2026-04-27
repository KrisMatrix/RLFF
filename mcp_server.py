import os
import subprocess
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP - This is your "Local Engineering Gateway"
mcp = FastMCP("ISO-NE-Modernization-Gateway")

PERL_DIR = "perl_codebase"
PYTHON_DIR = "python_codebase"

@mcp.tool()
def read_perl_script(filename: str) -> str:
    """Reads a source Perl script to understand its logic for conversion."""
    # Security: Ensure we only read from the perl_codebase folder
    safe_path = os.path.join(PERL_DIR, os.path.basename(filename))
    try:
        with open(safe_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: {filename} not found in {PERL_DIR}."

@mcp.tool()
def write_python_script(filename: str, code: str) -> str:
    """Writes the converted Python code to the python_codebase folder."""
    if not os.path.exists(PYTHON_DIR):
        os.makedirs(PYTHON_DIR)
        
    safe_path = os.path.join(PYTHON_DIR, os.path.basename(filename))
    with open(safe_path, "w") as f:
        f.write(code)
    return f"Successfully wrote {filename} to {PYTHON_DIR}."

@mcp.tool()
def run_validation_test() -> str:
    """
    Executes the Validator to compare Perl 'Oracle' output 
    against new Python output. Returns the parity results.
    """
    try:
        # Executes the validator.py script we discussed earlier
        result = subprocess.run(
            ["python3", "validator.py"], 
            capture_output=True, 
            text=True
        )
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return f"Validator failed to execute: {str(e)}"

if __name__ == "__main__":
    mcp.run()