import os
from shutil import copyfile


# directory = r'temp/file_path'
directory = r'C:\Users\alex_\Desktop\Holder\School\Semester 4\Economics\assignment'
save_path = r'temp/save_path'
for filename in os.listdir(directory):
    if filename.endswith(".pdf") or filename.endswith(".pptx") or filename.endswith(".doc") or filename.endswith(".docx"):
        print(filename)
        copyfile(directory + '/' + filename, save_path + '/' + filename)
        # file = os.path.basename(filename[0])
        # copyfile(file[0], os.path.join(save_path, file))

    else:
        print(
            "This is not a an important file, this file will be skipped: " + filename + "!")
