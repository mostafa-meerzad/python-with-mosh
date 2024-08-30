from pathlib import Path

# creating a path object
path = Path("some_dir\\some_dir\\some_file.txt") # "\" is calculated as escape-character

path = Path(r"some_dir\some_dir\some_file.txt") # path as a raw-string
print(path.name)
print()
currentPath = Path() # creating a path object relative to the current file
print(currentPath)
print(currentPath.absolute())
print()
# joining paths
path = Path('some_directory') / 'some_subdirectory' / 'some_file.txt'
# print(path.name)

currentFilePath = Path("someDir/someFile.txt")
print(currentFilePath.absolute())

# combining paths
combinedPath = Path() / Path("subDir") / "someDir"

# some useful methods

path = Path("some_dir/some_file.txt")
print(path.exists())
print(path.is_absolute())
print(path.is_dir())
print(path.is_file())
print(path.name)
print(path.stem)
print(path.parent)