# Instead of counting the occurrences every time, using the hashing technique, we will store the frequency of each element between 1 to N. Now, the element with frequency 2 will be the repeating number and the element with frequency 0 will be the missing number.

# Note: Here, we can solve this problem using a hash array.

# Approach:
# The steps are as follows:

# The range of the number is 1 to N. So, we need a hash array of size N+1 (as we want to store the frequency of N as well).
# We will iterate all the elements of the given array and update the hash array accordingly i.e. hash[a[i]] = hash[a[i]]+1.
# Now, we will iterate on the hash array and return the two elements with frequencies 2 and 0.



def findMissingRepeatingNumbers(a):
    n = len(a) # size of the array
    hash = [0] * (n + 1) # hash array

    #update the hash array:
    for i in range(n):
        hash[a[i]] += 1

    #Find the repeating and missing number:
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbers(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")

