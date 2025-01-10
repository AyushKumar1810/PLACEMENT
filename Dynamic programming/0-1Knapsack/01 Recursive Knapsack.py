def knapsack(wt, val, W, n):
    # Base condition
#*     // every recursive solution will have a base condition 
#*  // for base condition we need to think of the smallest valid input that we can pass 
#*   // array size can be atleast 0 || min weight can be 0 but not negetive; 
    if n == 0 or W == 0:
        return 0

    # Choices
    if wt[n - 1] <= W:
        return max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
                   knapsack(wt, val, W, n - 1)) #* // if the weight is less then the required weight then we have two choices either we can take that value or we can leave that value so we will take the maximum of both the values .
    elif wt[n - 1] > W:#* if the weight is greater then the required weight there is no sence for taking that value. 
        return knapsack(wt, val, W, n - 1)#* // return as it is by redusing the size of array 
    else:
        return -1

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    wt = list(map(int, input("Enter weights: ").split()))
    val = list(map(int, input("Enter values: ").split()))
    W = int(input("Enter knapsack capacity: "))

    print(knapsack(wt, val, W, n))


#Practise::
# every recursive solution will have a base condition
# for base condition we need to think of the smallest valid input that we can pass 
# array size can be atleast 0 || min weight can be 0 but not negetive; 
# Choices 
# if the weight is less then the required weight then we have two choices either we can take that value or we can leave that value so we will take the maximum of both the values . 
# if the weight is greater then the required weight there is no sence for taking that value. 
# return as it is by redusing the size of array 
#CODE
def knapSack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(val[n-1] + knapSack(wt,val,W-wt[n-1] , n-1),knapSack(wt,val,W,n-1)) 
    elif wt[n-1] > W:
        return knapSack(wt , val , W ,n-1)
    else:
        return -1
n = int(input())
wt = list(map(int,input().split())) 
val = list(map(int,input().split())) 
W = int(input()) 
print(knapSack(wt,val,W,n)) # Output: 10
