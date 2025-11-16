import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        abs_file_path = os.path.abspath(open(file_path, "x"))
    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Succesfully wrote to {file_path} ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file {e}" 
