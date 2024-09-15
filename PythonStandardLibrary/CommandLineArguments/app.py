import sys

# sys module has "argv" property that is populated with the values provided after the name of the app
# in the terminal like so "python app.py a b c d"
# this argv returns a list object and it always have one element and that is the name of your app here "app.py"
#
# cmdArgs = sys.argv
# print("Here is the arguments you've provided:")
# print(cmdArgs)
#
# for arg in cmdArgs:
#      print("argument" ,arg)

password = sys.argv[1]
if password == "1234":
    print("welcome")
else:
    print("not recognized")
    sys.exit(1)
