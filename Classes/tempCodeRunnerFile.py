class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = (
            self.tags.get(tag.lower(), 0) + 1
        )  # increase tag value by 1 if already exists otherwise set 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    
    def __len__(self):
        return len(self.tags)
    
    def __str__(self):
        return "something new"

# we could have created a simple dictionary and a
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.tags)
# before handling case sensitivity {'python': 2, 'Python': 1}
# after handling case sensitivity {'python': 3}

cloud["JS"] = 10
print(cloud.tags)
print(cloud["JS"])
print(cloud["python"])
print(len(cloud))

print(cloud)
# for x in cloud:
    # print(x)