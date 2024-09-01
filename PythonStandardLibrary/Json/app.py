import json
from pathlib import Path

# ----------------------------- writing data to a json file -------------

# data = {"name": "Alice", "age": 30, "is_student": False, "courses": ["Math", "Science"]}

# with open("data.json", "w") as file:
#     json.dump(data, file)

# ----------------------------- reading data from a json file -------------

# with open("data.json", "r") as file:
    # data = json.load(file)
    # print(data)


# ----------------------------- reading data from a json string -------------

# json_string = '{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "Science"]}'

# data = json.loads(json_string)

# print(data)

# ----------------------------- converting python object to json  -------------

data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science']
}

json_data = json.dumps(data)
print(json_data)

data = [
    {"id": 1, "name": "sky fall", "year": "2017"},
    {"id": 2,"name": "terminator", "year": "1989"}
]

with Path("movies.json") as path:
    path.write_text(json.dumps(data))
    
with open("movies2.json", 'w') as file:
    json.dump(data, file)