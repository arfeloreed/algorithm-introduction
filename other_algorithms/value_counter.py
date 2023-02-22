# using hashmap to count individual items

# create a list of fruits to count
fruits = ['apple', 'banana', 'orange', 'apple', 'pear', 'kiwi', 'banana',
            'apple', 'kiwi', 'orange', 'apple', 'pear', 'orange', 'banana',
            'apple', 'banana', 'orange', 'kiwi', 'pear', 'orange', 'banana']

# create a hashmap to store the unique items
unique_fruits = {}

# loop through the list of fruits and add them to the hashmap and count them
for fruit in fruits:
    if fruit in unique_fruits:
        unique_fruits[fruit] += 1
    else:
        unique_fruits[fruit] = 1

# print out the unique fruits and their counts
print(unique_fruits)