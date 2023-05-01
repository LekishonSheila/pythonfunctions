def year_of_birth(name,age):
    year = 2023 -age
    print(f"Hello {name},you were born in {year}")
def my_country(country="Kenya"):
        print(f"Hello you are from {country}")
def hello(*names):
            for name in names:
                print(f"Hello {name}")
def sum(*nums):
       sum=0
       for num in nums:
        answer+=nums
        return(answer)
def multiply_many(**kwargs):
    answer = 1
    for num in kwargs.values():
      answer*=num
    return answer

# Assignments

# A function named concatenate_args that takes any
#  number of string arguments in positional arguments format 
# and concatenates them into a single string
def concatenate_strings(*args):
    result = " "
    for arg in args:
        result += arg
    return result
# A function named concatenate_kwargs that takes any number
#  of string arguments in keyword arguments  format
#  and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    return ''.join(kwargs.values())



