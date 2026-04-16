arr = [1,2,3,4]

def sum_it(arr):

    total = 0
    for i in arr:
        total+= i 
        

    return total

# print(sum_it(arr))


# Count odd numbers

def count_odd(arr):

    odd = 0

    for num in arr:
        if num % 2 != 0:
            odd+=1

    return odd

# print(count_odd(arr))

# Find Duplicates


arr = [1,2,2,3,4,4]

def dupes(arr):
    freq = {}

    dupe = []

    for num in arr:
        if num in freq:
            freq[num] += 1

        else:
            freq[num] = 1

    for i in freq:
        if freq[i]>1:

            dupe.append(i)
            
    return dupe  

# print(dupes(arr))


# First Non-Repeating

arr = [1,2,2,3,1,4]

def f_non_rep(arr):

    freq = {}

    num = 0

    for i in arr:
        if i in freq:
            freq[i] +=1

        else:
            freq[i] =1

    for i in arr:
        if freq[i] ==1:
           return i


# print(f_non_rep(arr))


# First Repeating Element

arr = [1,2,3,2,1]

def f_rep_elemet(arr):
    
    seen = set()

    for num in arr:
        if num in seen:
            return num
        
        seen.add(num)

    return None



# print(f_rep_elemet(arr))


# Check if array is sorted

arr = [1,2,3,4]  
arr_1 = [1,3,2] 
def c_arr_sorted(arr):
    
    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            return False
        
    return True


# print(c_arr_sorted(arr))
# print(c_arr_sorted(arr_1))


# Second Largest Element

arr = [3,5,1,4]

def second_l_ele(arr):
    letmax = arr[0]
    max_1 = arr[0]
    max_2 = arr[0]

    for i in range (len(arr) ):
        if max_1>arr[i]:
            letmax = max_1

    return letmax

print(second_l_ele(arr))
