import os
from shutil import copyfile


# directory = r'temp/file_path'
directory = r'/file_path'
save_path = r'temp/file_path'
for filename in os.listdir(directory):
    if filename.endswith(".pptx", ".doc", ".docx", ".txt", ".pdf", ".mp3"):
        copyfile(directory + '/' + filename, save_path + '/' + filename)
        print(filename + " has been successfully copied!")
        # file = os.path.basename(filename[0])
        # copyfile(file[0], os.path.join(save_path, file))

    else:
        print(
            "This is not a an important file, this file will be skipped: " + filename + "!")
