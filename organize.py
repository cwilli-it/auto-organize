import getopt
import os
import shutil
import sys


def check_path(path):
    dir_exist = os.path.exists(path)

    if not dir_exist:
        os.makedirs(path)
        print("Directory created: " + path)
        return path
    else:
        return path


def move_files(working_dir):
    file_list = [f for f in os.listdir(working_dir) if os.path.isfile(os.path.join(working_dir, f))]
    for file in file_list:
        if file.endswith(".pdf"):
            shutil.move(working_dir + file, check_path(working_dir + "PDF/") + file)
        elif file.endswith(".html"):
            shutil.move(working_dir + file, check_path(working_dir + "HTML/") + file)
        elif file.endswith((".csv", ".tsv", ".xlsx")):
            shutil.move(working_dir + file, check_path(working_dir + "Excel/") + file)
        elif file.endswith(".docx"):
            shutil.move(working_dir + file, check_path(working_dir + "Word/") + file)
        elif file.endswith(".txt"):
            shutil.move(working_dir + file, check_path(working_dir + "Notepad/") + file)
        elif file.endswith(".json"):
            shutil.move(working_dir + file, check_path(working_dir + "JSON/") + file)
        elif file.endswith((".pub", ".ppk")):
            shutil.move(working_dir + file, check_path(working_dir + "Keys/") + file)
        elif file.endswith(".mkv"):
            shutil.move(working_dir + file, check_path(working_dir + "Video/") + file)
        elif file.endswith(".tar"):
            shutil.move(working_dir + file, check_path(working_dir + "Archive/") + file)
        elif file.endswith(".py"):
            shutil.move(working_dir + file, check_path(working_dir + "Python/") + file)
        elif file.endswith(".xml"):
            shutil.move(working_dir + file, check_path(working_dir + "XML/") + file)
        elif file.endswith(".js"):
            shutil.move(working_dir + file, check_path(working_dir + "Javascript/") + file)
        elif file.endswith(".cer"):
            shutil.move(working_dir + file, check_path(working_dir + "Certificate/") + file)


def main():
    argument_list = sys.argv[1:]
    options = "hd:"

    if argument_list == []:
        argument_list = ["-h"]

    try:
        opts, args = getopt.getopt(argument_list, options)
        for opt, arg in opts:
            if opt == "-h":
                print("Organize files in a directory")
                print("organize.py -d <directory>")
            elif opt in ("-d"):
                working_dir = arg
                print(os.path.join(working_dir, ""))
                move_files(os.path.join(working_dir, ""))

    except getopt.error as err:
        print(err)


main()
