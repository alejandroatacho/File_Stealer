import os
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

for filename in os.listdir(directory):
    # comment below is broken due to max 3 arguments per .endswith, very easy fix but im also very lazy to change 1 line of code :3
    # if filename.endswith(".pptx", ".doc", ".docx", ".txt", ".pdf", ".mp3"):
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

input("Press any key to exit...")
