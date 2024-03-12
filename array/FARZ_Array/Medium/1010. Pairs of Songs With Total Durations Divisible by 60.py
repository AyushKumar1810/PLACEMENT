# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

# Example 1:

# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:

# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.

#NOTE: the Approach is quite simple we will traverse the Array and we wll se if the sum of a[i] and arr[j] is divsible by 60 or not { i<j} if ot's then we will incaese our count variable by 1 . count +=1

#Brute Force Approach 
def numPairsDivisibleBy60(time):
    counts = 0
    n=len(time)
    for i in range(n):
        for j in range(i+1,n):
            if (time[i] + time[j])%60==0:
                counts+=1
    return counts
# Example usage:
time1 = [30, 20, 150, 100, 40]
print("Output for time1:", numPairsDivisibleBy60(time1))

time2 = [60, 60, 60]
print("Output for time2:", numPairsDivisibleBy60(time2))

#Optimized Approach:
# In the optimized approach, we use a dictionary to store the remainders of the song durations when divided by 60. Then, we iterate through the song durations and for each duration t, we check if 60 - t % 60 exists in the dictionary. If it does, it means there exists a song whose duration, when added to t, is divisible by 60.

def numPairsDivisibleBy60(time):
    count = 0
    remainder_dict = {}
    for t in time:
        remainder = t % 60
        complement = (60 - remainder) % 60
        if complement in remainder_dict:
            count += remainder_dict[complement]
        remainder_dict[remainder] = remainder_dict.get(remainder, 0) + 1
    return count

# Example usage:
time1 = [30, 20, 150, 100, 40]
print("Output for time1:", numPairsDivisibleBy60(time1))

time2 = [60, 60, 60]
print("Output for time2:", numPairsDivisibleBy60(time2))
