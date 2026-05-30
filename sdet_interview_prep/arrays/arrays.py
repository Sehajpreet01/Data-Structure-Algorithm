# =============================================================================
# TOPIC: ARRAYS
# =============================================================================
#
# WHAT IS AN ARRAY?
# An array is a collection of elements stored at contiguous memory locations.
# In Python, lists act as dynamic arrays.
#
# KEY CONCEPTS TO KNOW:
# - Indexing: arr[0] = first element, arr[-1] = last element
# - Slicing: arr[start:end:step]
# - Length: len(arr)
# - Common operations: append, insert, remove, pop, sort, reverse
#
# HOW TO THINK ABOUT ARRAY PROBLEMS:
# 1. Can I solve it by iterating once? (O(n))
# 2. Do I need to track indices or values?
# 3. Should I use a second array or modify in-place?
# 4. Is sorting the array helpful before solving?
# 5. Can two pointers reduce complexity?
#
# TIME COMPLEXITIES:
# Access by index   -> O(1)
# Search (unsorted) -> O(n)
# Insert at end     -> O(1)
# Insert at middle  -> O(n)
# Delete            -> O(n)
#
# COMMON PATTERNS IN INTERVIEWS:
# - Frequency counting (use a dict/hashmap)
# - Two pointers (left/right or slow/fast)
# - Prefix sum
# - Sliding window
# - Sorting first, then applying logic
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Find all duplicates in an array
# Input:  [1, 2, 3, 2, 4, 1]
# Output: [2, 1]  (elements that appear more than once)

def find_duplicates(arr):
    freq = {}
    duplicates = []

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

# print("Q1 - Find Duplicates:", find_duplicates([1, 2, 3, 2, 4, 1]))

def find_duplicates(arr):

    freq = {}
    return_dupes = []

    for num in arr:
        if num in freq:
            freq[num] +=1

        else: freq[num] =1

    for i in freq:
        if freq[i]>=2:
            return_dupes.append(i)

    return  return_dupes

print(find_duplicates([1, 2, 3, 2, 4, 1]))


# Q2: Find the maximum and minimum element in an array
# Input:  [3, 1, 7, 2, 9, 4]
# Output: Max = 9, Min = 1

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

max_val, min_val = find_max_min([3, 1, 7, 2, 9, 4])
# print("Q2 - Max:", max_val, "| Min:", min_val)


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Reverse an array in-place (without using slicing or built-in reverse)
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# Q4: Move all zeros to the end while maintaining order of non-zero elements
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# Q5: Remove duplicates from a sorted array (in-place)
# Input:  [1, 1, 2, 3, 3, 4]
# Output: [1, 2, 3, 4]

# Q6: Find the second largest element in an array
# Input:  [10, 5, 8, 20, 15]
# Output: 15

# Q7: Rotate an array to the right by k positions
# Input:  arr = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Q8: Find if there exists a pair with a given sum
# Input:  arr = [2, 7, 11, 15], target = 9
# Output: True  (2 + 7 = 9)

# Q9: Find the first non-repeating element in an array
# Input:  [4, 5, 1, 2, 0, 4, 1, 2, 5, 3]
# Output: 0   (first element with frequency 1)

# Q10: Merge two sorted arrays into one sorted array
# Input:  [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]




# Q1 - Sum of array
arr = [1,2,3,4]

def sum_arr(arr):
    total = 0

    for i in arr:

        total +=i

    return total

print(sum_arr(arr)) 


# Q2 - Count even numbers

arr = [1,2,3,4,6]

def count_even(arr):
    total_even = 0

    for i in arr:
        if i%2 == 0:
            total_even+=1

    return total_even

print(count_even(arr))


# Q3 — Return numbers greater than 5

arr = [2,7,1,9,4]

def greater_then5(arr):
    total = []

    for i in arr:
        if i>5:
            total.append(i)

    return total

print(greater_then5(arr))



#Q4 — Return squares of numbers

arr = [1,2,3]

def return_square(arr):
    squ = []

    for i in arr:
        squ.append(i**2)

    return squ

print(return_square(arr))


# Q5 - Count negative numbers

arr = [-1,2,-3,4,-5]

def negative_count(arr):
    nev = 0

    for i in arr:
        if i <0:
            nev+=1

    return nev

print(negative_count(arr))
    


#Q6 — Return odd numbers

arr = [1,2,3,4,5]

def return_odd(arr):
    odd = []

    for i in arr:
        if i%2 != 0:
            odd.append(i)

    return odd

print(return_odd(arr))



# Q7 — Count numbers greater than 10

arr = [5,12,18,2,20]

def greater_then_10(arr):

    count = 0

    for i in arr:
        if i>10:
            count+=1

    return count

print(greater_then_10(arr))



# Q8 - Return absolute values


arr = [-1,2,-3]

def absolute_v(arr):

    absval = [abs(i) for i in arr]

    return absval

print(absolute_v(arr))


# Q9 - Count zeros

arr = [0,1,0,2,0]

def count_z(arr):
    count = 0

    for i in arr:
        if i ==0:
            count+=1

    return count

print("zero count: ",count_z(arr))


# Q10 — Return numbers divisible by 3

arr = [1,3,6,7,9]

def div_b_3(arr):

    div3val = []

    for i in arr:
        if i%3 ==0:
            div3val.append(i)


    return div3val

print(div_b_3(arr))


# Q11 — Count numbers between 5 and 15 (inclusive)

arr = [2,5,10,16,15]

def count_between_inclusive(arr):
    count = 0

    for i in arr:
        if i >= 5 and i <=15:
            count +=  1

    return count

print(count_between_inclusive(arr))


# Q12 — Count frequency of numbers

arr = [1,2,2,3,1]

def count_freq(arr):
    
    freq = {}
    
    for i in arr:
        if i in freq:
            freq[i] += 1
        else: 
            freq[i] = 1

    return freq

print(count_freq(arr))


# Q13 — First non-repeating element

arr = [1,2,2,3,1,4]

def first_non_repeating(arr):


    freq = {}

    element = []

    for i in arr:

        if i in freq:
            freq[i]+=1

        else: freq[i] = 1

    for i in freq:
        
        

    return freq
        
print(first_non_repeating(arr))
