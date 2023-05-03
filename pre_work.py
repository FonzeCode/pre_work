# Question 1
# Write a function to print "hello_USERNAME!" is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name='username'):
    print("hello_" + user_name.upper() + "!")

hello_name()


def hello_name(user_name):
    print("hello_" + user_name.upper()+"!")

hello_name("username")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and
# returns nothing

def first_odds():
    for number in range(1,101):
        if number % 2 == 1:
            print(number)
    return
first_odds()

# Quedtion 3
# Please write a Python function, max_num_in_list to return the max number of a given
# list. The first line of the code has been defined as below

def max_num_in_list(a_list):
        
        print(max(a_list))
max_num_in_list(a_list=[2, 34, 45, 67, 656, 2334, 23])


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4,
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean
# Type (true/false)

def is_leap_year(a_year):
     return a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0)

          
print(is_leap_year(a_year=1600))
print(is_leap_year(a_year=1900))
print(is_leap_year(a_year=2024))







# Question 5
# Write a function top check to se if all numbers in list are consecutive numbers. For
# example,[2,3,4,5,6,7] are consecutive numbers. but [1,2,4,5] are not consecutive
# numbers. The return should be boolean Type.

def is_consecutive(a_list):
     return all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))

print(is_consecutive(a_list= [2, 3, 4, 5, 6, 7]))
print(is_consecutive(a_list= [1,2,4,5]))

