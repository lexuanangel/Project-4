# Author: Angel Le
# GitHub username: lexuanangel
# Date: 1/31/2023
# Description: Create a function that takes in a number and returns
# the sum of the Fibonacci sequence

# define the function so that it returns the number in Fibonacci sequence
def fib(num):
    func_a = 0
    func_b = 1
    all_in_one = 0
    for i in range(num):
        func_a = func_b
        func_b = all_in_one
        all_in_one = func_a + func_b
    return all_in_one


# print(fib(10)) to make sure I get the correct return value
