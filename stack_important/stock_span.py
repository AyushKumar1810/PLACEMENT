def stockspan(arr):
    stack=[]
    results=[]
    for i in range(len(arr)):
        num=arr[i]
        count=1
        while stack and stack[-1][0]<=num:
            count+=stack.pop()[1]
        stack.append((num,count))
        results.append(count)
    return results
arr=[100, 80, 60, 70, 60, 75, 85]
ayush=stockspan(arr)
print(ayush)