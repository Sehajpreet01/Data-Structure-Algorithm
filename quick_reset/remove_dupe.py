arr = [1,1,2,2,3]

def remove_dupe(arr):


    freq = {}
    nodupe = []

    for i in arr:
        if i in freq:
            freq[i]+=1

        else: freq[i] = 1

    for i in freq:
        nodupe.append(i)

    return nodupe


print(remove_dupe(arr))



  