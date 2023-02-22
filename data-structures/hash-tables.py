# hash table example

# create a hash table all at once
# item1 = dict({"key1": 1, "key2": 2, "key3": 3})
# print(item1)

# create a hash table progressively
# item2 = {}
# for i in range(1, 4):
#     item2["key" + str(i)] = i
# print(item2)

item2 = {f"key{i}": i for i in range(1,4)}
# print(item2)

# access values
# print(item2["key1"])

# add a new key
# item2["key4"] = 4
# print(item2)

# modify a value
# item2["key4"] = 5
# print(item2)

# delete a key
# del item2["key4"]
# print(item2)

# iterate over a hash table
for key, value in item2.items():
    print(f"key: {key}, value: {value}")