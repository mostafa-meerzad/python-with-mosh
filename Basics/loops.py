# for x in "Mostafa":
#     print(x)

# for x in ["a", "b", "c"]:
#     print(x)

# for x in range(10):
#     print(x)

# for x in range(2, 10, 2):
# print(x)

# --------------------------------
# consider a scenario that you have a list of names and want to find the first name matching our criteria and immediately jump out of the loop (for performance reasons) display a message if no matching name found

names = ["John", "Mary"]

found = False
for name in names:
    if name.startswith("J"):
        print("Name Found")
        found = True
        break
if not found:
    print("Name not found")


# for...else 
# else block is executed if our for-loop completes successfully without an immediate break
for name in names:
    if name.startswith("J"):
        print("Name Found")
        found = True
        break
else:
    print("Name not found")

# --------------------------------------

guess = 0
answer = 5

# while guess != answer:
#     guess = int(input("Guess: "))


# while...else 
# else block is executed if our while-loop completes successfully without an immediate break
while guess != answer:
    guess = int(input("guess: "))
    if guess == 1000:
        print("you did guess the king number")
        break

else:
    print("you didn't guess the king number but guessed the correct answer")