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
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
            if subdirectory.endswith('.txt') or subdirectory.endswith('.pdf') or subdirectory.endswith('.docx'):
                copyfile(os.path.join(root, subdirectory), save_path)

        for file in files:
            print(os.path.join(root, file))
            if file.endswith('.txt') or file.endswith('.docx') or file.endswith('.pdf'):
                print('File found')
                print(file)
                print(os.path.join(root, file))
                copyfile(os.path.join(root, file),
                         os.path.join(save_path, file))
                print('File copied')
        # print(filename)
        # copyfile(filename, save_path)
        # comment below is broken due to max 3 arguments per .endswith, very easy fix but im also very lazy to change 1 line of code :3


__name__ == "__main__"
run()
input("Press any key to exit...")
