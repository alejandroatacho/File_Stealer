from genericpath import isdir
import os
from re import sub
from shutil import copyfile
import getpass


# directory = r'temp/file_path'
directory = r"C:\\Users\\" + getpass.getuser() + "\\documents"
save_path = r'temp/file_path'

# Future codes to implement to scan thru all sub folders within the folder
'''for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        print(os.path.join(root, subdirectory))
    for file in files:
        print(os.path.join(root, file))
'''


def run():
    dirs = os.listdir(directory)

    for filename in dirs:
        # comment below is broken due to max 3 arguments per .endswith, very easy fix but im also very lazy to change 1 line of code :3
        # if filename.endswith(".pptx", ".doc", ".docx", ".txt", ".pdf", ".mp3"):
        for subdirs in dirs:
            if subdirs.endswith(".pptx"):
                print(subdirs)
                copyfile(subdirs, save_path)
            elif subdirs.endswith(".doc"):
                print(subdirs)
                copyfile(subdirs, save_path)
            elif subdirs.endswith(".docx"):
                print(subdirs)
                copyfile(subdirs, save_path)
            elif subdirs.endswith(".txt"):
                print(subdirs)
                copyfile(subdirs, save_path)
            elif subdirs.endswith(".pdf"):
                print(subdirs)
                copyfile(subdirs, save_path)
            elif subdirs.endswith(".mp3"):
                print(subdirs)
                copyfile(subdirs, save_path)
            else:
                print("No files found")
                break
        if filename.endswith(".pdf") or filename.endswith(".pptx") or filename.endswith(".doc") or filename.endswith(".docx"):
            copyfile(directory + '/' + filename, save_path + '/' + filename)
            print(filename + " has been successfully copied!")

            # file = os.path.basename(filename[0])
            # copyfile(file[0], os.path.join(save_path, file))

        else:
            print(
                "This is not a an important file, this file will be skipped: " + filename + "!")
            text_file = open("output.txt", "a")
            n = text_file.write(filename + "\n")
            text_file.close()


__name__ == "__main__"
run()
input("Press any key to exit...")
