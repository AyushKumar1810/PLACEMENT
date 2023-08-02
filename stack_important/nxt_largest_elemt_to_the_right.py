def nxtlargestelementtotheright(arr):
    stack=[]
    result=[]
    for num in reversed(nums):
        while stack and stack[-1] <=num:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(num)
    result.reverse()
    return result
nums = [2,4,0,9,6]

output =nxtlargestelementtotheright(nums)
print(output)


