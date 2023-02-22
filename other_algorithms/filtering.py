# use hashmap to filter out duplicate items

# create a list of fruits and vegetables to filter out duplicates
fruits = ['apple', 'banana', 'orange', 'apple', 'pear', 'orange', 'banana']
vegetables = ['lettuce', 'cucumber', 'carrot', 'cucumber', 'lettuce', 'cucumber']

# create a hashmap to store the unique items
unique_fruits = {}
unique_vegetables = {}

# loop through the list of fruits and add them to the hashmap
for fruit in fruits:
    unique_fruits[fruit] = 0

# loop through the list of vegetables and add them to the hashmap
for vegetable in vegetables:
    unique_vegetables[vegetable] = 0

# print out the unique fruits and vegetables
print(unique_fruits.keys())
print(unique_vegetables.keys())
print(unique_fruits)
print(unique_vegetables)
print()
print(set(unique_fruits.keys()))
print(set(unique_vegetables.keys()))