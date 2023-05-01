# Write a Python function that takes two arguments (a and b) and returns their sum.
def add_values(a, b):
    return(a+b)
print(add_values)

# Write a Python function that takes a string as input and returns the string reversed.
def reverse_string(string):
    return string[::-1]
print(reverse_string("word"))




# Write a Python function that takes a list of integers as input and returns the sum of 
# all the integers in the list.
def sum_list(numbers):
    total = 0
    numbers= [10,20,30,40]
    for num in numbers:
        total += num
    return total
print(sum_list)


# Write a Python function that takes a list of integers as input and returns a new list
#  with all the even numbers removed.
def remove_even(numbers):
    return [num for num in numbers if num % 2 != 0]
print(remove_even(1,2,3,4,5,6,7,8,9,10))





# Write a Python function that takes a list of integers as input and returns the highest 
# value in the list.
def find_highest(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest
print(find_highest(2,13,22,39,1,3,66,78))




# Write a Python function that takes a list of strings as input and returns a new list with
#  all the strings capitalized.
def capitalize_strings(strings):
    return [string.capitalize() for string in strings]
print(capitalize_strings("sheila","lekishon","ann"))
