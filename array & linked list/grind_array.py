# Count Even Numbers

arr = [1,2,3,4,5,6]

def count_even(arr):

    count = 0

    for num in arr:
        if num %2 ==0:
            count+=1

    return count

# print(count_even(arr))


# Count numbers greater than 3

arr = [1,5,2,6,3]

def count_num_greater_three(arr):

    count = 0

    for num in arr:
        if num >3:
            count+=1

    return count

# print(count_num_greater_three(arr))



# Return all even numbers

arr = [1,2,3,4]

def all_even_num(arr):

    even = []
    for num in arr:
        if num %2==0:
            even.append(num)

    return even

# print(all_even_num(arr))


# Return numbers greater than 3
arr = [1,5,2,6,3]

def return_num_then_three(arr):


    numbers = []

    for num in arr:
        if num>3:
            numbers.append(num)

    return numbers

# print(return_num_then_three(arr))


# Count zeros


arr = [0,1,0,2,0]

def count_zeros(arr):

    count = 0

    for num in arr:
        if num == 0:
            count+=1

    return count


# print(count_zeros(arr))







# Count numbers divisible by 3

arr = [1,3,6,7,9]

def divided_three(arr):

    count = 0

    for num in arr:
        if num%3==0:
            count+=1

    return count


# print(divided_three(arr))


# Return numbers divisible by 3


arr = [1,3,6,7,9]

def return_number_divide_three(arr):

    number = []

    for num in arr:
        if num%3==0:
            number.append(num)

    return number

# print(return_number_divide_three(arr))



# Count numbers between 2 and 6

arr = [1,3,5,7,2]

def between_two_six(arr):
    count = 0

    for num in arr:
        if num>=2 and num<=6:
            count+=1

    return count

# print(between_two_six(arr))


# Return numbers between 2 and 6

arr = [1,3,5,7,2]

def return_numbers_between_two_three(arr):
    numbers = []

    for num in arr:
        if num>=2 and num<=6:
            numbers.append(num)
    
    return numbers

# print(return_numbers_between_two_three(arr))


# Count negative numbers

arr = [-1,2,-3,4]

def count_negative(arr):
    count = 0

    for num in arr:
        if num<0:
            count+=1

    return count

# print(count_negative(arr))









# Count even numbers greater than 3

arr = [1,2,4,6,3]

def count_even_for_greater_three(arr):

    count = 0

    for num in arr:
        if num>3 and num%2==0:
            count+=1

    return count

# print(count_even_for_greater_three(arr))


# Return odd numbers less than 5

arr = [1,2,3,4,5,6]

def return_odd_less_then_five(arr):

    numbers = []
    for num in arr:
        if num<5 and num%2!=0:
            numbers.append(num)

    return numbers


# print(return_odd_less_then_three(arr))


# Count numbers divisible by 2 AND 3

arr = [1,2,3,4,6,12]

def numbers_divisible_two_three(arr):
    count = 0

    for num in arr:
        if num%2==0 and num%3==0:
            count+=1

    return count

# print(numbers_divisible_two_three(arr))



# Return numbers NOT divisible by 2

arr = [1,2,3,4]

def return_not_divisible_two(arr):
    numbers = []

    for num in arr:
        if num%2!=0:
            numbers.append(num)

    return numbers



# print(return_not_divisible_two(arr))











# Return squares of all numbers

arr = [1,2,3]

def return_square(arr):

    square = []

    for num in arr:
        square.append(num**2)

    return square

# print(return_square(arr))



# Return double of even numbers


arr = [1,2,3,4]

def return_double_of_even(arr):

    double = []

    for num in arr:
        if num%2==0:
            double.append(num+num)

    return double

# print(return_double_of_even(arr))



# Return negative of all numbers

arr = [1,-2,3]

def negative_of_numbers(arr):

    numbers = []

    for num in arr:
        numbers.append(-num) #did lttle bit cheating here

    return numbers

# print(negative_of_numbers(arr))


# Return absolute values

arr = [-1,2,-3]

def absolute_values(arr):

    result= [abs(x) for x in arr]

    return result
    

# print(absolute_values(arr))


# Return square of ONLY even numbers

arr = [1,2,3,4]

def square_only_even(arr):

    result = [num**2 for num in arr if num%2==0]

    return result

# print(square_only_even(arr))








# Count squares of even numbers > 10

arr = [1,2,3,4,5]

def count_square_even_greater_10(arr):
    count = 0

    result = [num**2 for num in arr if num%2==0]
    for num in result:
        if num>10:
            count+=1
    
    return count
    
print(count_square_even_greater_10(arr))




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
