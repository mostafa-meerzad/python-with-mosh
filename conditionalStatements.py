from cgi import print_arguments
from email import message


age = 24

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done!")

x = 1000
if x > 1:
    pass
else:
    print("else block")


# ------------------------

# name = "John"
name = ""

# name = " "  # " " a string with just one space is not considered an empty string
# if not name.strip(): # solution is to strip the white-spaces

if not name.strip():
    print("name is empty")

age = 19

if age >= 18 and age < 65:
    print("Eligible")

# the same comparison as above
if 18 <= age < 65:  # this is called chaining comparison-operators
    print("Eligible")

# -------------------------------
print("---------------------------------- ")
age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
