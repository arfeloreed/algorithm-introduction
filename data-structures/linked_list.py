# what is a linked list?

# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
# collection of data elements called nodes, each node has a value and a pointer to the next node.
# contains references to the next node in the list.
# hold whatever data the application needs.

# advantages of linked list
# 1. Dynamic size
# 2. Ease of insertion/deletion
# underlying memory doesn't need to be reorganized

# disadvantages of linked list
# 1. Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do a binary search with linked lists efficiently with its default implementation. Read about it here.
# 2. Extra memory space for a pointer is required with each element of the list.
# 3. Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.
# 4. Arrays have better cache locality that can make a pretty big difference in performance.
# 5. Linked list nodes may not be adjacent in memory. Unlike arrays, random access of data elements is not allowed. Nodes are accessed sequentially starting from the first node. So we cannot do a binary search with linked lists efficiently with its default implementation. Read about it here.
# 6. Can't do a constant-time random item access. You can only access the first item in constant time, and then you have to iterate through the list to get to the item you want. This is why linked lists are not a good choice for implementing arrays.
# item lookup is linear in time complexity (O(n)).

# linked list example

# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count
    
    def insert(self, data):
        # insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    def find(self, val):
        # find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None
    
    def deleteAt(self, idx):
        # delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
    
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# exercise the list
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(13))
# print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()
