import os
import sys
import subprocess

from dotenv import load_dotenv
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file with optional CLI arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the Python file to run.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional command-line arguments to pass to the script.",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir:        
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    command = [sys.executable, abs_file_path]
    command += args
    try:
        completed_object = subprocess.run(command, cwd=abs_working_dir, capture_output=True, timeout=30, text=True)
        if not completed_object.stdout and not completed_object.stderr:
            return "No output produced."
        ret_string = f'STDOUT: {completed_object.stdout}\nSTDERR: {completed_object.stderr}'
        if completed_object.returncode != 0:
            ret_string += f'\nProcess exited with code {completed_object.returncode}'
        return ret_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
        
