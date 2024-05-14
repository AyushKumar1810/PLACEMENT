# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtracking(combinational , next_digits):
            if len(next_digits)==0:
                output.append(combinational)
            else:
                for later in mapping[next_digits[0]]:
                    backtracking(combinational+later,next_digits[1:])
        output=[]
        backtracking("" , digits)
        return output
                
# Example usage:
solution = Solution()

# Example 1:
digits_1 = "23"
output_1 = solution.letterCombinations(digits_1)
print("Example 1 Output:", output_1)

# Example 2:
digits_2 = "79"
output_2 = solution.letterCombinations(digits_2)
print("Example 2 Output:", output_2)