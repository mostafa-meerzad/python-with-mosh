from pathlib import Path
import shutil
from time import ctime


file = Path("./PythonStandardLibrary/__init__.py")
# print(file.absolute())
# file.exists()
# file.name
# file.stem
# file.unlink() # to delete the file
print(ctime(file.stat().st_ctime))  # the timestamp from 1970-01-01
# file.rename("newName.js")
content = file.read_bytes()  # file content as bytes
content = file.read_text()  # file content as text
# content = file.write_bytes()
content = file.write_text("print('hello')")  # file content as text
print(file.read_text())

# ---------------------------------------
# copying contents of one file into another

source = Path("./PythonStandardLibrary/source.py")
target = Path("./PythonStandardLibrary/") / "testDir/target.py"

if not target.exists():
    # target.write_text(source.read_text())
    # not the best option
    print("copying...")
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy(source, target)
    print("copied")
else:
    print("failed to copy")
