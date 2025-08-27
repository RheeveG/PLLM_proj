

def get_files_info(working_directory, directory=None):
	if (directory not in working_directory):
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
