my_set = {1,2,5, "22"}

print(my_set)

for x in my_set:
    print(x)

my_set.add(22)
print(my_set)
# my_set.remove("222")

my_set.update((8,4))
my_set.update([99])
print(my_set)

my_set.discard(22)
print(my_set)
my_set.clear()
print(my_set)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}

print(set1)
print(set2)
print(union_set)

print (set1.difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.symmetric_difference(set2))

print(500 in set1)