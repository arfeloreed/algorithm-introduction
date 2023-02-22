# use recursive algorithm to find the max value in a list

# create a list of numbers
numbers = [1, 22, 3, 4, 5, 16, 77, 8, 9, 10]

# define a function to find the max value in a list
def find_max_value(numbers):
    # base case
    if len(numbers) == 1:
        return numbers[0]
    # recursive case
    else:
        # find the max value of the first and second number
        max_value = max(numbers[0], numbers[1])
        # remove the first number
        numbers.pop(0)
        # replace the first number with the max value
        numbers[0] = max_value
        # call the function again with the new list
        return find_max_value(numbers)

    # base case
    # if len(numbers) == 1:
    #     return numbers[0]
    # otherwise get the first item and call the function again
    # op1 = numbers[0]
    # print(op1)
    # op2 = find_max_value(numbers[1:])
    # print(op2)

    # compare the first item with the result of the function
    # if op1 > op2:
    #     return op1
    # else:
    #     return op2

# call the function and print the result
print(find_max_value(numbers))