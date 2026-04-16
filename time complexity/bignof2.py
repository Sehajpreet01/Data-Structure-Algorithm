n = 10

for i in range(n):
    for j in range(n):
        print(i, j)

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2


for i in range(n):
    for j in range(i):
        print(i, j)

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2


for i in range(n):
    for j in range(n):
        break

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2



for i in range(n):
    for j in range(i, n):
        print(i, j)

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2



for i in range(n):
    for j in range(n):
        if j == 0:
            break

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2
