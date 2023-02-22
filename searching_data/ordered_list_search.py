# searching for an item in an ordered list
# using the binary search algorithm

# created an ordered list of random numbers
items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    loweridx = 0
    upperidx = listsize
    
    # while we haven't narrowed it down to one element ...
    while loweridx <= upperidx:
        # ... check the middle most element
        midval = (loweridx + upperidx) // 2
        
        # found the item, return the index
        if itemlist[midval] == item:
            return midval
        
        # get the next midpoint
        if item > itemlist[midval]:
            loweridx = midval + 1
        else:
            upperidx = midval - 1
        
    # if the item isn't found, return None
    if loweridx > upperidx:
        return None

# try out the function with a few examples
print(binarysearch(87, items))    # should be 9
print(binarysearch(25, items))    # should be None
print(binarysearch(41, items))    # should be 5
print(binarysearch(23, items))    # should be 4