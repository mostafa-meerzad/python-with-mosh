from pathlib import Path

path = Path("")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2") 

# for p in path.iterdir():
    # print(p)

# paths = [p for p in path.iterdir()] # a list of WindowsPath objects
paths = [p for p in path.iterdir() if p.is_dir()] # list of directories only
paths = [p for p in path.iterdir() if p.is_file()] # list of files only
paths = [p for p in path.glob("**/*.py") if p.is_file()] # list of files only using the glob method
paths = [p for p in path.rglob("*.py") if p.is_file()] # list of files only recursively the better way
print(paths)