def nxtsmallestelementtotheright(arr):
    stack=[]
    result=[]
    for num in reversed(arr):
        while stack and stack[-1] >=num:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(num)
    result.reverse()
    return result
arr = [3, 9, 4, 6, 2, 8, 1]
output =nxtsmallestelementtotheright(arr)
print(output)


