# Very Good and conceptul question From leetcode 2454 , Next greater Element IV . From stack
                                 
                                    # Solution      


def secondGreaterElement(nums):
    first_greater_stack = []
    second_greater_stack = []
    result = [-1] * len(nums)
        
    for i in range(len(nums)):
        temp = []
        while first_greater_stack and nums[first_greater_stack[-1]] < nums[i]:
            temp.append(first_greater_stack.pop())       
        first_greater_stack.append(i)
                
        while second_greater_stack and nums[second_greater_stack[-1]] < nums[i]:
            result[second_greater_stack.pop()] = nums[i]
                
        while temp:
            second_greater_stack.append(temp.pop())
                
                
    return result
nums = [2,4,0,9,6]
ayush=secondGreaterElement(nums)
print(ayush)
                 