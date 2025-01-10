# 494. Target Sum
# Medium
# Topics
# Companies

    # You are given an integer array nums and an integer target.

    # You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    #     For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

    # Return the number of different expressions that you can build, which evaluates to target.

    

    # Example 1:

    # Input: nums = [1,1,1,1,1], target = 3
    # Output: 5
    # Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    # -1 + 1 + 1 + 1 + 1 = 3
    # +1 - 1 + 1 + 1 + 1 = 3
    # +1 + 1 - 1 + 1 + 1 = 3
    # +1 + 1 + 1 - 1 + 1 = 3
    # +1 + 1 + 1 + 1 - 1 = 3

    # Example 2:

    # Input: nums = [1], target = 1
    # Output: 1

    

    # Constraints:

    #     1 <= nums.length <= 20
    #     0 <= nums[i] <= 1000
    #     0 <= sum(nums[i]) <= 1000
    #     -1000 <= target <= 1000
class Solution:
    def count_subsets_with_sum(self, nums, target_sum):
        n = len(nums)
        # Initialize DP matrix
        dp = [[0] * (target_sum + 1) for _ in range(n + 1)]# dp[i][j] will be the number of subsets with sum j in the first i elements of the array nums (0-indexed) 
        for i in range(n + 1):
            dp[i][0] = 1 # There's one way to get sum 0 (empty subset) for any number of elements in the array 

        # Build the matrix in bottom-up manner
        for i in range(1, n + 1):
            for j in range(target_sum + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target_sum]

    def find_target_sum_ways(self, nums, target):
        total_sum = sum(nums)
        # Check if (total_sum + target) is even
        if (total_sum + target) % 2 != 0:# If the sum of the array elements and the target sum is odd, we can't find a subset with the given sum 
            return 0
        target_sum = (total_sum + target) // 2# If the sum of the array elements and the target sum is even, we can find a subset with the given sum by finding the number of subsets with half the sum of the array elements and the target sum    
        return self.count_subsets_with_sum(nums, target_sum)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    # nums = list(map(int, input("Enter the elements of the array: ").split()))
    # target = int(input("Enter the target sum: "))
    nums = [1,1,1,1,1]
    target = 3
    print(solution.find_target_sum_ways(nums, target))