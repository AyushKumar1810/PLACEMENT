#Question : Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

# Example 1:

# Input:
# txt = forxxorfxdofr
# pat = for
# Output: 3
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.
# Example 2:

# Input:
# txt = aabaabaa
# pat = aaba
# Output: 4
# Explanation: aaba is present 4 times
# in txt. . 

#NOTE-Gist of the logic:

# 1.	Create an unordered map for the given pattern. The map stores all the distinct characters of the pattern as keys, and their frequencies as values. Create a variable count, which has the count of all the distinct characters in the pattern, which is the size of the map. Create another variable for storing the actual answer.
# 2.	Inside the while loop, compare the jth character with the keys of the map. If this character is found in the map, decrement its corresponding value. If the value of any of the keys becomes 0, decrement the value of count. It means that you’ve found one character in its required quantity in your current window. Like this if for every character in the map, the value becomes 0, then the value of count becomes 0, and it signifies that the current window is an anagram of the pattern. We’re using this count variable to signify whether the window is an anagram or not(in O(1) time), otherwise we have to traverse the whole map for checking if every corresponding value has become 0 or not, and it would have taken O(K) time. 
# 3.	When you’ve reached the window size, you need to do 2 things:-
# a)	Retrieving the answer- if the count becomes 0, anagram is found, increment the value of ans variable.
# b)	Sliding the window- before sliding the window, we need to remove all the calculations regarding the first element in the current window. If it exists in the map, then we need to increment the corresponding value in the map. Why we’re incrementing its value because, this character is not going to be there in our next window, so if it has contributed in making an anagram for our previous window, we need to delete its appearance or significance in the map, which tells that there’s a gap which needs to be filled by the next incoming character to complete this incomplete anagram. And only if the corresponding value in the map has become 1, we’ll increment the value of count, and not for any other case.
# For eg:-
# Pattern- aaba
# Current state of Map – a->3
# 	      			     b->1
# count=2

# window has:- acbe
# Current state of Map – a->2 
# 	      			          b->0
# count=1 (what current state of the map signifies is, we need 2 more a's to complete an anagram)
# We have to remove this 'a', as it is the first element of the current window, because we need to move ahead now:-
# window is: cbe_
# Current state of the map- a->3
#                                               b->0
# count=1  (this state of the map signifies that we need 3 a's to find an anagram)


# In such case we’re removing this ‘a’ from the window, so we increment its value to 3, we shouldn’t increment the value of count in this case. Increment the count only if the corresponding value becomes 1 after incrementing it. Because the whole part of ‘a’ is not gone by removing the first element of the previous window, some part of it is gone with it. When the whole part is gone, then we can say that okay, there’s one more character which needs to be found in the next window in its whole quantity.

def countOccurencesOfAnagrams(string, pattern):
    ans = 0
    k = len(pattern)
    # Initialize a Hash Map to store the frequency of characters in the pattern
    patternFreq = {}

    # Build the frequency map for the pattern
    for char in pattern:
        if char in patternFreq:
            patternFreq[char] += 1
        else:
            patternFreq[char] = 1

    # Sliding window approach
    windowStart = 0
    windowFreq = {}

    for windowEnd in range(len(string)):
        # Expand the window by adding the current character to the frequency map
        if string[windowEnd] in windowFreq:
            windowFreq[string[windowEnd]] += 1
        else:
            windowFreq[string[windowEnd]] = 1

        # Shrink the window if its size exceeds the pattern size
        if windowEnd - windowStart + 1 > k:
            leftChar = string[windowStart]
            windowFreq[leftChar] -= 1
            if windowFreq[leftChar] == 0:
                del windowFreq[leftChar]
            windowStart += 1

        # Check if the frequency maps of the pattern and window match
        if windowFreq == patternFreq: # we have created two hash map to count window Freq and patternFreq to count the given pattern string latter occurance of when we are traversing the string and storing it's value into window Freq , if both count are eual then we will increase our answer and will movw ahead 
            ans += 1

    return ans
string = "forxxorfxdofr"
pattern = "for"
result=countOccurencesOfAnagrams(string,pattern)
print (result)