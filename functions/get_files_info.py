import os

def get_files_info(working_directory, directory="."):
	cur_dir = os.path.join(working_directory, directory)

	abs_cur_dir = os.path.abspath(cur_dir)

	if not abs_cur_dir.startswith(os.path.abspath(working_directory)):
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
	if os.path.isfile(abs_cur_dir) == True:
		return f'Error: "{directory}" is not a directory'
	else:
		retstring =""
		dirlist = None
		try:
			dirlist = os.listdir(abs_cur_dir)
		except Exception as e:
			return(f'Error: {e}')

		for elem in dirlist:
			try:
				size = os.path.getsize(os.path.join(abs_cur_dir, elem))
			except Exception as e:
				return(f'Error: {e}')
			retstring += f"- {elem}: file_size={size} bytes, is_dir={os.path.isdir(os.path.join(abs_cur_dir, elem))}\n"
		return retstring.rstrip('\n')