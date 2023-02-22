# searching for an item in an unordered list
# sometimes called a linear search

# declare a list of items to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item):
    # loop through the list of items
    for i in range(len(items)):
        # if the item is found, return the index
        if items[i] == item:
            return i

    # if the item is not found, return -1
    # return -1
    return None

# try out the function with a few examples
print(find_item(87))    # should be 6
print(find_item(250))   # should be -1
