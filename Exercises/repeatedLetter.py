from pprint import pprint

sentence = "This is a common interview question"

# todo: find the most repeated letter in the st

characters = {}

for letter in sentence:
    if not letter in characters:
        characters[letter] = 1
    else:
        characters[letter] += 1

charactersSorted = sorted(characters.items(), key=lambda x: x[1], reverse=True)
print(charactersSorted[0])
