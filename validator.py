import json
import subprocess
import os

def run_validation():
    # Load the "Oracle" Ground Truth
    with open('ground_truth.json', 'r') as f:
        ground_truth = json.load(f)

    results = {}

    for script_name, data in ground_truth.items():
        # Map Perl filename to Python filename
        python_script = script_name.replace('.pl', '.py')
        python_path = os.path.join('python_codebase', python_script)

        if os.path.exists(python_path):
            # Run the Python script and capture output
            process = subprocess.run(['python3', python_path], capture_output=True, text=True)
            python_output = process.stdout

            # Compare against Perl ground truth
            if python_output == data['content']:
                results[python_script] = "PASS: 100% Functional Parity"
            else:
                results[python_script] = f"FAIL: Variance Detected.\nExpected: {data['content']}\nGot: {python_output}"
        else:
            results[python_script] = "MISSING: Python script not yet generated."

    for script, status in results.items():
        print(f"--- {script} ---\n{status}\n")

if __name__ == "__main__":
    run_validation()