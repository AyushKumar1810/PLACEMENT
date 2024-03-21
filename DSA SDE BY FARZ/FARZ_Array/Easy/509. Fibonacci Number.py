# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

#Here's a simple recursive solution to calculate Fibonacci numbers:
import time
# Record the start time
start_time = time.time()
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(10))
# Record the end time
end_time = time.time()

# Calculate and print the runtime
runtime_seconds = end_time - start_time
runtime_milliseconds = runtime_seconds * 1000
print(f"Runtime: {runtime_milliseconds:.2f} milliseconds")

#NOTE: the above recursive approach will take timeComplexivity in Factorial so for better approach we will use dynamic programming concept
import time
# Record the start time
start_time = time.time()
def Fab(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    fib_array=[0]*(n+1)# We predefined the 0th index element 
    fib_array[1]=1 # We predefined the 1st index element 
    for i in range(2,n+1):
        fib_array[i] = fib_array[i-1] + fib_array[i-2]
    return fib_array[n]
print(Fab(100))
end_time = time.time()

# Calculate and print the runtime
runtime_seconds = end_time - start_time
runtime_milliseconds = runtime_seconds * 1000
print(f"Runtime: {runtime_milliseconds:.2f} milliseconds")

import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_array = [0] * (n + 1)
    fib_array[1] = 1

    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]

    return fib_array[n]

# Measure the time
start_time = time.time()

# Call your function
result = fib(30)  # Replace 30 with the desired value

# Calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Result: {result}")
print(f"Elapsed Time: {elapsed_time} seconds")
