#sum array

arr = [1,2,3,4]

def sum_arr(arr):
    total = 0

    for i in arr:
        total += i
    return total

# print(sum_arr(arr))
        
#count odd
arr = [1,2,3,4,5]

def count_odd(arr):
    count = 0

    for i in arr:
        if i%2 != 0:
            count +=1

        else: pass
    return count

# print(count_odd(arr))

#find maximum

arr = [3,7,2,9,4]

def find_max(arr):
    letmax = arr[0]

    for i in arr:
        if i>letmax:
            letmax = i

    return letmax

# print(find_max(arr))

arr = [3,7,2,9,4]


def find_min(arr):
    let_min = arr[0]

    for i in arr:
        if i<let_min:
            let_min = i

    return let_min

# print(find_min(arr))


#find duplicates

arr = [1,2,2,3,4,4]

def f_dupes(arr):
    freq = {}

    dupes = []

    for i in arr:
        if i in freq:
            freq[i] += 1

        else:
            freq[i] = 1

    print(freq)
    for key in freq:
        print(freq[key])
        print(key)

        if freq[key]>1:
            # print(freq[key])
            dupes.append(key)

    return dupes

# print(f_dupes(arr))


#find first non repeating element

arr = [1,2,2,3,1,4]


def first_non_repeat(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] +=1
        else: freq[i] = 1

    # return freq

    for key in arr:
        if freq[key] ==1:
            return key
        
    return None


# print(first_non_repeat(arr))

# Check if Duplicate Exists

arr = [1,2,3,4,2]

def dupes_exist(arr):
    seen = set()

    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False

# print(dupes_exist)


# Check if array is sorted

arr1 = [1,2,3,4] 
arr2 = [1,3,2] 

def check_arr_sort(arr):

    for i in range (len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
        
    return True

# print(check_arr_sort(arr1))

#reverse array

arr = [1,2,3,4] 

def reverse_array(arr):
    res = []

    for i in range(len(arr)-1, -1, -1):
        res.append(arr[i])

    return res

# print(reverse_array(arr))


arr = [1,2,3,4,5,6]

def reverse_even(arr):
    ev_res = []
    final_list = []

    
    for i in range(len(arr)-1, -1, -1):
        if arr[i]%2 ==0:
            ev_res.append(arr[i])
            
    idx = 0
    for i in range(len(arr)):
        if arr[i]%2 ==0:
            arr[i] = ev_res[idx]
            idx+=1

    return arr

# print(reverse_even(arr))


arr = [0,1,0,3,12]
def move_zero(arr):
    res = []
    count_zero = 0

    for num in arr:
        if num == 0:
            count_zero+=1

        else: 
            res.append(num)

    for zero in range(count_zero):
        res.append(0)


    return res
        
# print(move_zero(arr))


# Remove Duplicates (keep order)

arr = [1,2,2,3,1]

def r_dupes_o(arr):

    new = []

    for i in arr:
        if i in new:
            pass
        else:
            new.append(i)

    return new

# print(r_dupes_o(arr))

# Majority Element (> n/2 times)

arr = [3,3,4,3,2]

def majority_element(arr):
    freq = {}

    
    for i in arr:
        if i in freq:
            freq[i] += 1

        else:
            freq[i] = 1
 

    for i in freq:
        if freq[i]> 2:
            return i
        
    return None
            

# print(majority_element(arr))


# (Variation of Move Zero)

arr = [0,1,0,3,12]

def move_zero_v2(arr):

    non_zero = []

    for i in arr:
        if i !=0:
            non_zero.append(i)

    for i in arr:
        if i ==0:
            non_zero.append(i)

    return non_zero

# print(move_zero_v2(arr))


def final_move_zero_v2(arr):
    res = []
    zero_count = 0

    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            res.append(num)

    # add zeros
    for _ in range(zero_count):
        res.append(0)

    return res


# Count unique elements

# [1,2,2,3,1] → 3

arr = [1,2,2,3,1]

def unique_elements(arr):

    freq = []
    count = 0

    for i in arr:
        if i not in freq:
            freq.append(i)

        else:
            pass

    return len(freq)


# print(unique_elements(arr))
            

def unique_elements_v2(arr):
    return len(set(arr))
            

# print(unique_elements_v2(arr))

# First Repeating Element

arr = [1,2,3,2,1]