import os

# directory = r'temp/file_path'
directory = r'C:\Users\alex_\Desktop\Holder\School\Semester 4\Economics\assignment'

for filename in os.listdir(directory):
    if filename.endswith(".pdf") or filename.endswith(".pptx") or filename.endswith(".doc") or filename.endswith(".docx"):
        print(filename)

    else:
        print(
            "This is not a an important file, this file will be skipped: " + filename + "!")
