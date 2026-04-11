n=10

for i in range(n):
    print(i)

# O(n) time complexity of above code is n which is bigger then 1<loglogn<logn<n

for i in range(n):
    for j in range(n):
        print(i, j)

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2



i = 1
while i < n:
    i = i * 2

# O(logn) time complexity of the above code is logn and it is logrithmic function I guess which comes here 1<loglogn<logn


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


i = n
while i > 0:
    i = i // 2
# O(logn) time complexity of the above code is logn and it is logrithmic function I guess which comes here 1<loglogn<logn


for i in range(n):
    print(i)

for j in range(n):
    print(j)

# O(1) time complexity of the above code is contant 


for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

# 0(n**3) time complexity of the above code is cubic


for i in range(n):
    for j in range(n):
        if j == 0:
            break

# O(n**2) time complexity of the above code is n**2 and it is quadratic function which is bigger then 1<loglogn<logn<n<n**2
