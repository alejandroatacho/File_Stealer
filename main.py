import os
from shutil import copyfile
import getpass


# directory = r'temp/file_path'
directory = r"C:\\Users\\" + getpass.getuser() + "\\documents"
save_path = r'temp/file_path'
for filename in os.listdir(directory):
    # comment below is working version/2nd if is broken due to max 3 arguments per .endswith
    if filename.endswith(".pdf") or filename.endswith(".pptx") or filename.endswith(".doc") or filename.endswith(".docx"):
        # if filename.endswith(".pptx", ".doc", ".docx", ".txt", ".pdf", ".mp3"):
        copyfile(directory + '/' + filename, save_path + '/' + filename)
        print(filename + " has been successfully copied!")
        # file = os.path.basename(filename[0])
        # copyfile(file[0], os.path.join(save_path, file))

    else:
        print(
            "This is not a an important file, this file will be skipped: " + filename + "!")
        text_file = open("output.txt", "a")
        n = text_file.write(filename)
        text_file.close()

input("Press any key to exit...")
