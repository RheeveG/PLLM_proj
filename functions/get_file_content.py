import os
from config import MAX_CHARS

from dotenv import load_dotenv
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a single file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to read.",
            ),
        },
        required=["file_path"],
    ),
)
def get_file_content(working_directory, file_path):
    cur_path = os.path.join(working_directory, file_path)
    abs_cur_path = os.path.abspath(cur_path)
    if not abs_cur_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_cur_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_cur_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if os.path.getsize(abs_cur_path) > MAX_CHARS:
            file_content_string += f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"
    except Exception as e:
        return f"Error: {e}"
    return file_content_string
    