import pathlib
from zipfile import ZipFile
import zipfile

# # Create and write to file1.txt
# with open('file1.txt', 'w') as f1:
#     f1.write('This is the content of file1.')

# Create and write to file2.txt
# with open('file2.txt', 'w') as f2:
# f2.write('This is the content of file2.')

# Create a ZIP file
# one way but not the best way
# zipF = ZipFile("testZip.zip", "w")
# zipF.write("./file1.txt")
# zipF.write("./file2.txt")

# recommended way
# with ZipFile("example.zip", "w") as zipf:
# Add files to the ZIP file
# zipf.write("file1.txt")
# zipf.write("file2.txt")

# adding files to an existing zip file
# with ZipFile("testZip.zip", "a") as zipf:
# zipf.write("file3.txt")

# extracting zip file
# with ZipFile("testZip.zip") as zipf:
# zipf.extractall("./testDir")

# to see the files in side zipfile
# with ZipFile("testZip.zip") as zipf:
# print(zipf.namelist())

# to read the contents of a zipfile without extracting it
# with ZipFile("testZip.zip") as zipf:
# with zipf.open("file1.txt") as file:
# content = file.read()
# print(content)

# zipping a whole directory
# zipping all files and folders inside the specified directory
# with ZipFile("files.zip", "w") as zip:
# for path in pathlib.Path("./testDir").rglob("*.*"):
# zip.write(path)

# going to zip only the specified directory without it's content
# with ZipFile("file.zip", "w") as zip:
# zip.write("./testDir/")

# getting info about zipped file
with ZipFile("file.zip") as zip:
    # print(zip.namelist()) # contents inside it
    # print(zip.compression) # compression ration
    # print(zip.getinfo("/file1.txt").file_size) # contents inside it
    # print(zip.getinfo("testDir/file1.txt").compress_size) # contents inside it
    print("contents of zip file")
    for info in zip.infolist():
        print("file name: ", info.filename)
        print(info.compress_size, " file compression size")
        print(info.compress_type, " file compression type")
        print(info.date_time, " file date")
        print(info.is_dir(), " is a directory")
