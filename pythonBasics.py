studentCount = 1000
rating = 4.99
isPublished = False
courseName = """
Multiple
Lines of
String
"""
x = 1
y = 2
# is equivalent to this
x, y = 1, 2

# setting multiple variables to the same value

a = b = 10

x = 1

print(id(x))

x = x + 1

print(id(x))

nums = [1, 2, 4]
print(id(nums))

nums.append(10)
print(id(nums))

# -----------------------------------------------


course = "Python Programming"
print(len(course))  # 18 => number of characters in the string
print(course[0])  # p => first character of string
print(course[-1])  # g => first element form the end of the string
# pyt => a slice of string starting from 0 (first element) to 3 (fourth element but except itself)
print(course[0:3])
# Python Programming => from first to last element or the whole string
print(course[:])
print(course[:2])  # Pyt =>starting point omitted 0 used as default value
# on Programming => ending point omitted len(course) used as default value
print(course[4:])

print(id(course))
print(id(course[0]))


# -----------------------------------------------

first = "Mostafa"
last = "Meerzad"
full = first + " " + last  # string concatenation

full = f"{first} {last}"  # formatted string
full = F"{first} {last}"  # formatted string

print(full)
print(f"this is the length of fullName {len(full)}")

#-----------------------------------------

course = " Python Programming on"

print(course.upper()) # returns a copy of the string turned into uppercase
print(course.lower()) # returns a copy of the string turned into lowercase
print(course.split(" "))  # returns a list of parts of the string separated with the provided separator
print(course.strip()) # returns a copy of string with leading and trailing whitespaces removed
print(course.rstrip()) # stript right
print(course.lstrip()) # strip left
print(course.count("on", 0, 9)) # Return the number of non-overlapping occurrences of substring sub in string 
print(course.count("m"))
print(course.casefold()) # removes casing, useful for comparison
print(course.istitle()) # True if string is titleCase
print(course.islower()) 
print(course.isupper())
print(course.isalnum()) # True if string is alphanumeric (mix of letters and numbers)

print(course.find("Pro")) # returns the starting index of substring -1 if non existing
print(course.replace(" ", "#")) # reruns a copy of string with characters replaced

print("Programming" in course) # use in operator to check if substring is included in the string
print("Python" not in course) # not operator also exist to negate