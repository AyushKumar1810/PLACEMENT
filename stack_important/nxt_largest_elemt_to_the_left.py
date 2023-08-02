def nextlargestelementtotheleft(arr):
    s=[]
    ans=[]
    for i in range (len(arr)):    
        while s  and s[-1] <=arr[i]:
            s.pop()
        if len(s)==0:
            ans.append(-1)
        else:
            ans.append(s[-1])
        s.append(arr[i])
    return ans
input_arr=[3, 9, 4, 6, 2, 8, 5]
ayush=nextlargestelementtotheleft(input_arr)
print(ayush)
