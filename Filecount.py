import os, os.path

# simple version for working with CWD
#listy of files
files=[]
folders=[]
for filenames in os.listdir():
    if os.path.isfile(filenames):
        files.append(filenames)
    else:
        folders.append(filenames)

no_of_files=len(files)-1
no_of_folders=len(folders)
print("Total number of Files: %d"%no_of_files)
print("Total number of Folders: %d"%no_of_folders)


input("\n\nPress a key to exit")
