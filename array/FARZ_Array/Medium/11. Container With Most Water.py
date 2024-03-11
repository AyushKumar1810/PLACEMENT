# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

#Brute Force Approach:The approach is quite simple and we have to use two loop in which we will traverse to whole array and we will take difference for weight and for height we will take minimun between i and j loop index array value and we will calculate area by using formula "height*width"

def max_area(height):
    max_water = 0
    for i in range (len(height)):
        for j in range(i+1,len(height)):
            h=min(height[i] , height[j])
            w=j-1
            max_water = max(max_water , w*h )#calculate area by using formula "height*width"
    return max_water
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))

#Optimized Approach:using two pointer approach, In the optimized approach, we start with the widest possible container and gradually move the pointers towards each other. This way, we eliminate possibilities where the height of the container would be limited by the shorter of the two lines. The time complexity of this solution is O(n) where n is the length of the array.

def max_area(height):
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
height = [1,8,6,2,5,4,8,3,7,9]
print(max_area(height))
