# Second Largest Element (again, properly)

arr = [3,5,1,4]

def second_largest(arr):
    max1 = arr[0]
    max2 = float('-inf')

    for num in arr[1:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max2

print(second_largest(arr))




[10, 2, 8, 5]


arr = [[10, 2, 8, 5]]

def second_largest_1(arr):

    max_1 = arr[0]:
    max_2 = float('-inf')

print(second_largest_1(arr))



# arr = []

# def (arr):

# print((arr))



# arr = []

# def (arr):

# print((arr))



# arr = []

# def (arr):

# print((arr))



# arr = []

# def (arr):

# print((arr))



# arr = []

# def (arr):

# print((arr))



# arr = []

# def (arr):

# print((arr))



# arr = []

# def (arr):

# print((arr))
