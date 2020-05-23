
# tuple
first = (1, 2, 3, 4)
# list
second = [1, 2, 3, 4, 5, 6, 7, 8]

print("type of first tuple is ", type(first))
print("type of second list is ", type(second))

print(first)
print(second)

# edit the list
second[1] = 324
print("after the list is changed...", second)
print("tuple slicing ", first[:2])
print("list slicing ", second[1:])

# edit the tuple, resulting in error
first[0] = 12
