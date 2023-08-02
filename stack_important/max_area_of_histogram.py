#concept/Logic - In that question we have to find the max area that can be form by 
# array in the form Histogram. The basic concept we are using is that it will 
#expand it's area Till it gets lower array value / Height than It's current array
#value . so we will find it's nearest smallest to the left and nearest smallest 
#to the right . Then we can substract to find it's width and then multiply with
#array value to get it's Area and then we will maximise area to get maximum area
#value 



def nsl(arr,n): #next smaller to the left
    stack=[]
    ans=[]
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)
    return ans
def nsr(arr,n): # Next smaller to the right 
    stack=[]
    ans=[]
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if not stack:
            ans.append(n)
        else:
            ans.append(stack[-1])
        stack.append(i)
    ans.reverse()
    return ans
def maxarea(arr,n):
    left=nsl(arr,n)
    right=nsr(arr,n)
    maxarea=0
    for i in range (n):
        maxarea=max(maxarea,(arr[i]*(right[i]-left[i]-1)))
    return maxarea
arr = [6,2,5,4,5,1,6]
n = len(arr)

print(maxarea(arr, n))