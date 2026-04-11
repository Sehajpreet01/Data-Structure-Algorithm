# arr = [4, 2, 7, 1, 9]

# def find_min(arr):
#     let_min = arr[-1]
#     for i in range(len(arr)):

#         if arr[i]<let_min:
#             let_min = arr[i]

        
#     return let_min
    

# print(find_min(arr))

# arr = [1,1,2,3,2,1]

# def count_freq(arr):
#     dict = {}

#     for i in range(len(arr)):
#         if arr[i]  in dict:
#             dict = {i:i}

#         elif arr[i] in dict:

# arr_d = dict(arr)
# print(arr_d)



# d = [2,2,2,2]

# freq = {}

# for i in d:
#     if i in freq:
#         freq[i] += 1

#     else:
#         freq[i] = 1

# print(freq)

# f = {}

# f[1] = 1
# f[2] = 1

# print(f)

# f = {1:1}
# f[1]+=1
# print(f)

# arr = [2,1,5,8,1,4]
# for i in arr:
#     print(i)


# arr = [1,2,3,4,5,6]

# freq = {}

# for num in arr:
#     freq[num] = 1
#     print(freq)

# print(freq)

# arr = [1,1,1,2,3,3,2,2,2,1,2,1,4,4]

# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num] += 1
#         print(freq)

#     else:
#         print('about to run else')
#         freq[num] = 1


# print(freq)


s = "apple"
def count_char(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] +=1
        else:
            freq[ch] =1

    return freq

# print(count_char(s))


s = 'abca'

def f_repeat_ch(s):
    seen = {}
    for ch in s:
        if ch in seen:
            return ch
        
        else: seen[ch] = True

# print(f_repeat_ch(s))

s = "apple banana apple"

def w_freq(s):
    freq = {}
    s_up = s.split()

    for w in s_up:
        if w in freq:
            freq[w] +=1

        else: freq[w] = 1

    return freq

# print(w_freq(s))
# freq = {1: 1, 2: 2, 3: 1, 4: 2}
# seen = []

# for key in freq:
#     if freq[key] == 1:
#         print(key)
#         seen.append(key)
     





arr = [1,2,2,3,4,4]

def unique_e(arr):

    freq = {}
    seen = []

    for i in arr:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] =1

    for key in freq:
        if freq[key] ==1:
            # print(key)
            seen.append(key)

    return seen


    
# print(unique_e(arr))

s1 = "listen"
s2 = "silent"

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq_1 = {}
    freq_2 = {}

    for i in s1:
        if i in freq_1:
            freq_1[i] +=1
        else: freq_1[i] =1

    for i in s2:
        if i in freq_2:
            freq_2[i] +=1

        else: freq_2[i] = 1

    if freq_1 == freq_2:
        return True
    else: return False

print(check_anagram(s1,s2))