# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

# #Brute Force Approach:
# The brute force approach involves trying out all possible combinations of the candidates and checking if any combination sums up to the target.

# We can use recursion to explore all possible combinations.
# At each step, we have two choices: either include the current candidate or exclude it.
# We keep track of the current sum and the current combination of candidates.
# If the current sum equals the target, we add the current combination to our result.
# We continue exploring all combinations until we exhaust all candidates.

def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])
    
    result = []
    backtrack(0, target, [])
    return result

# Example usage:
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

#Optimized Approach:
# The optimized approach involves using a similar idea to the brute-force approach but with some improvements to avoid redundant calculations.

# We can sort the candidates to prune unnecessary branches in the search tree.
# During the recursive exploration, we only consider candidates whose value is less than or equal to the remaining target.
# This helps in avoiding exploring combinations that are guaranteed to exceed the target.
# Additionally, we can stop exploring a branch if the remaining target becomes negative, as it indicates that the current combination cannot sum up to the target.

def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            backtrack(i, target - candidates[i], path + [candidates[i]])
    
    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

# Example usage:
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
