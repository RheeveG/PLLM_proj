from functions.get_files_info import get_files_info
def printErr(err):
    if err != None:
        print(err)
err = get_files_info("calculator", ".")
printErr(err)
err = get_files_info("calculator", "pkg")
printErr(err)
err = get_files_info("calculator", "/bin")
printErr(err)
err = get_files_info("calculator", "../")
printErr(err)
err = get_files_info("calculator", "main.py")
printErr(err)