"""
Instructions from your teacher:
Given an input, print all numbers up to and including that input, unless they are divisible by 3, then print "fizz" instead, or if they are divisible by 5, print "buzz". If the number is divisible by both, print "fizzbuzz".

For example, given 5:

1
2
fizz
4
buzz


Given 10:
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz

Given 15:
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
"""

def fizzbuzz(n):
    
# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0 :
            print("buzz")
        else:
            print(i)
        i += 1

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)
