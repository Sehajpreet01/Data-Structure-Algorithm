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

# print(second_largest(arr))




# [10, 2, 8, 5]


arr = [10, 2, 8, 5]

def second_largest_1(arr):

    max_1 = arr[0]
    max_2 = float('-inf')

    for num in arr:
        if num>max_1:
            max_2 = max_1
            max_1=num
        elif num>max_2 and num!=max_1:
            max_2 = num

    return max_2

# print(second_largest_1(arr))




arr = [5,5]
arr1 = [5,5,4,1,3,4]


def second_largest_2(arr):

    max_1 = float('-inf')
    max_2 = float('-inf')

    for i in arr:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        
        elif i>max_2 and i !=max_1:
            max_2=i

    if max_2 == float('-inf'):
        return None

    return max_2


# print(second_largest_2(arr))
# print(second_largest_2(arr1))




arr = [2, 10, 10, 9]


def second_largest_3(arr):
    max1 = float('-inf')
    max2 = float('-inf')

    for num in arr:
        if num>max1:
            max2 = max1
            max1 = num
        elif num>max2 and num!=max1:
            max2 = num
    
    return max2
# print(second_largest_3(arr))




arr =[3,5,1,4]

def second_smallest(arr):
    small_1 = float('inf')
    small_2 = float('inf')

    for num in arr:
        if num<small_1:
            small_2 = small_1
            small_1=num 
        elif num<small_2 and num!=small_1:
            small_2 = num

    return small_2



# print(second_smallest(arr))



arr = [1,1,2,2,3]

def remove_duplicates(arr):

    freq = {}
    removed_dupes = []

    for num in arr:
        if num in freq:
            freq[num] +=1

        else: freq[num] =1

    for key in freq:

        removed_dupes.append(key)

    return removed_dupes

# print(remove_duplicates(arr))


def remove_duplicates(arr):
    res = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            res.append(arr[i])

    return res


# print(remove_duplicates([1,1,2,2,3]))




arr = [1,1,1,2,3,3,4]

def remove_dupes(arr):

    res = [arr[0]]

    for num in range(1, len(arr)):
        if arr[num] != arr[num-1]:
            print(num)
            res.append(arr[num])

    return res 

# print(remove_dupes(arr))




arr = [1,1,2,2,2,3,4,4]

def removedupes_1(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        print(arr[i-1])
        if arr[i]!= arr[i-1]:
            res.append(arr[i])

    return res

# print(removedupes_1(arr))


arr = [0,1,0,3,12]

def move_zero(arr):
    count = 0
    numbers = []

    for num in arr:
        if num ==0:
            count+=1

        elif num>0:
          numbers.append(num)
        
    for num in range(count):
        numbers.append(0)

    return numbers


print(move_zero(arr))


def move_zero(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr


arr = [0,1,0,3,12]
# print(move_zero(arr))


arr = [2,5]

arr[0], arr[1] = arr[1], arr[0]

print(arr)




# arr = [1, -2, 3, -4, 5]
# def negative_to_left(arr):


# print((arr))





arr = [0,1,0,3,12]

def move_zeros_to_end(arr):

    j = 0
    for num in range(arr)

print(move_zeros_to_end(arr))




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
