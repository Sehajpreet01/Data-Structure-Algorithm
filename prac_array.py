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

arr = [[1,2,3,4,2]]

def dupes_exist(arr):
    
