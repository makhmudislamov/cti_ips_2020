"""
A prime number is a number that cannot be formed by multiplying any numbers but 1, and itself. Another way of saying that is that a prime number is only divisible by 1, and itself. Prime numbers are not "composed" of any other numbers, and so we say that numbers that are not Prime, are Composite. All composite numbers can be decomposed into prime factors.

Prompt:
Count the number of prime numbers less than a non-negative number, n.

Given 10, your countPrimes solution should return 4
Given 20, your countPrimes solution should return 8

1 does not count as a prime number.

This problem is best divided into two functions:
Counting Primes - countPrimes()
Determining Primality - isPrime()
"""

print("Input number")
n = int(input())

# Determine if the input number is prime 
def isPrime(n):
  for current_number in range(2,n):
    # if the input number is evenly divisible by the current number?
    if n % current_number == 0:
      return False
  return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):

  counter = 0

  for i in range(2, n+1):
    if isPrime(i):
      counter += 1
  return counter

print(countPrimes(n))

  