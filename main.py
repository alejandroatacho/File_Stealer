import os
from shutil import copyfile
import getpass


# directory = r'temp/file_path'
directory = r"C:\\Users\\" + getpass.getuser() + "\\documents"
save_path = r'temp/file_path'
files_list = []
i = 0
# Future codes to implement to scan thru all sub folders within the folder
for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        # print(os.path.join(root, subdirectory))
        files_list.append(files)
        print(files_list)
        for files in files_list.endswith('.txt', '.doc', '.docx'):
            print(files)
            i += 1
        else:
            print('No files found')

    #     if files_list.endswith(".pdf") or files_list.endswith(".pptx") or files_list.endswith(".doc") or files_list.endswith(".docx"):
    #         copyfile(directory + '/' + files, save_path + '/' + files)
    #         print(files + " has been successfully copied!")
    #     else:
    #         print(
    #             "This is not a an important file, this file will be skipped: " + files + "!")
    #         text_file = open("output.txt", "a")
    #         n = text_file.write(files + "\n")
    #         text_file.close()

    # for file in files:
    #     print(os.path.join(root, file))


# for files in os.listdir(directory):
#     # comment below is broken due to max 3 arguments per .endswith, very easy fix but im also very lazy to change 1 line of code :3
#     # if files.endswith(".pptx", ".doc", ".docx", ".txt", ".pdf", ".mp3"):
#     if files.endswith(".pdf") or files.endswith(".pptx") or files.endswith(".doc") or files.endswith(".docx"):
#         copyfile(directory + '/' + files, save_path + '/' + files)
#         print(files + " has been successfully copied!")
#         # file = os.path.basename(files[0])
#         # copyfile(file[0], os.path.join(save_path, file))

#     else:
#         print(
#             "This is not a an important file, this file will be skipped: " + files + "!")
#         text_file = open("output.txt", "a")
#         n = text_file.write(files + "\n")
#         text_file.close()

input("Press any key to exit...")
