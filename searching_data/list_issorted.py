# identify whether a list is sorted or not

# create a list of random numbers
items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87, 5]

# function to check if a list is sorted
def issorted(itemlist):
    # get the list size
    # listsize = len(itemlist) - 1
    # start at the two ends of the list
    # loweridx = 0
    # upperidx = listsize
    
    # while we haven't narrowed it down to one element ...
    # while loweridx <= upperidx:
        # ... check the middle most element
        # midval = (loweridx + upperidx) // 2
        
        # found the item, return the index
        # if itemlist[midval] == itemlist[midval + 1]:
        #     return False
        
        # get the next midpoint
        # if itemlist[midval] > itemlist[midval + 1]:
        #     loweridx = midval + 1
        # else:
        #     upperidx = midval - 1
        
    # if the item isn't found, return None
    # if loweridx > upperidx:
    #     return True

    # using the brute force method
    # for i in range(len(itemlist) - 1):
    #     if itemlist[i] > itemlist[i + 1]:
    #         return False
        
    # return True

    # using Python comprehension
    return all(itemlist[i] <= itemlist[i + 1] for i in range(len(itemlist) - 1))  
        # all() return a Boolean value
        # all() returns True if all elements in the iterable are true and False otherwise

# try out the function with a few examples
print(issorted(items1))    # should be True
print(issorted(items2))    # should be False
