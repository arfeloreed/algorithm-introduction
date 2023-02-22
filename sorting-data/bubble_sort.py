# example of a bubble sort algorithm

# def bubble_sort(dataset):
#     for i in range(len(dataset)-1,0,-1):
#         for j in range(i):
#             if dataset[j]>dataset[j+1]:
#                 temp = dataset[j]
#                 dataset[j] = dataset[j+1]
#                 dataset[j+1] = temp

#         print("Current state: ", dataset)

# def main():
#     list1 = [54,26,93,17,77,31,44,55,20]
#     bubble_sort(list1)
#     print("Final state: ", list1)


# from chatgpt
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# def main():
#     arr = [64, 34, 25, 12, 22, 11, 90]
#     bubble_sort(arr)
#     print("Sorted array is:")
#     for i in range(len(arr)):
#         print("%d" % arr[i]),

def main():
    list1 = [54,26,93,17,77,31,44,55,20]
    bubble_sort(list1)
    print("Final state: ", list1)

if __name__ == "__main__":
    main()
