# Write a function that uses while, if and continue
#  statements to print all the even numbers between 0 and 50. 

def print_even_numbers():
    x= 0
    while x <= 50:
        if x % 2 != 0:  
            x += 1
            continue
        print(x)   
        x+= 1


# Write a function that takes an integer argument and prints "Prime"
#  if the number is prime, and "Not prime" if the number is not prime.
def prime_numbers():
    x=range(20)
    for i in x:
        if i %5==0:
            print(f"{i} is a prime number")
        else:
            print(f"{i} is not as prime number")

# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.
def sum_even_numbers():
    x = [11,12,13,14,15,16,17,18,19,20] 
    for m in x:
        if m % 2 == 0:   
            print(m)  

# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers between the two
#  integers (inclusive) that are divisible by 3.
def sum_divisible_by_three(start, end):
    total = 0
    for num in range(start, end+1):  
        if num % 3 == 0:   
            total += num   
    print(total)  


