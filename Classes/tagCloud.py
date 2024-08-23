class TagCloud:
    def __init__(self):
        # self.tags = {} # leaving tags this way makes it available to the outside but we don't want it that way
        self.__tags = {} # now tags property is private and can't be accessed from the outside

    def add(self, tag):
        self.__tags[tag.lower()] = (
            self.__tags.get(tag.lower(), 0) + 1
        )  # increase tag value by 1 if already exists otherwise set 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __str__(self):
        return "something new"

    def __iter__(self):
        # an iterator is an object that walks a container (list, dictionary, tuple...) and gets one item at a time
        # use built-in iter() function to create an iterator object
        return iter(self.__tags)

# we could have created a simple dictionary and a
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
# print(cloud.tags)
# before handling case sensitivity {'python': 2, 'Python': 1}
# after handling case sensitivity {'python': 3}

cloud["JS"] = 10
# print(cloud.tags)
print(cloud["JS"])
print(cloud["python"])
print(len(cloud))

print(cloud)
print()
print("iterating over cloud tags")
for x in cloud:
    print(x)

print()
# print(cloud.tags["python"])
# print(cloud.tags)
# print(cloud.__tags) # now doing this will throw an error. AttributeError: 'TagCloud' object has no attribute '__tags'
# but __tags is not 100% private and can't be accessed, here is how to access it
# cloud.__dict__ will return a dictionary containing class-attributes each prefixed with the class-name
# {'_TagCloud__tags': {'python': 3, 'js': 10}}

print(cloud.__dict__)
print(cloud._TagCloud__tags) # and this is the tags dictionary which we tried to make private