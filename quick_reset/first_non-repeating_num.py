arr= [1,2,2,3,1,4]

def non_rep_num(arr):

    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1

        else: freq[i] = 1

    for i in freq:
        print(freq[i])
        

    for i in freq:
        print(i)


    return freq


print(non_rep_num(arr))