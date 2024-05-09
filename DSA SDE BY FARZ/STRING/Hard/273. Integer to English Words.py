# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Define lists for words representation
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        def to_words(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + " " + to_words(n % 10)
            else:
                return ones[n // 100] + " Hundred " + to_words(n % 100)
        
        billion = num // 10**9
        million = (num % 10**9) // 10**6
        thousand = (num % 10**6) // 10**3
        rest = num % 10**3
        
        result = ""
        if billion:
            result += to_words(billion) + " Billion "
        if million:
            result += to_words(million) + " Million "
        if thousand:
            result += to_words(thousand) + " Thousand "
        if rest:
            result += to_words(rest)
        
        return result.strip()
