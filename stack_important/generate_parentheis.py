# leetcode problem No-22

#1 only add open parentesis only when open<n
#2 only add clase parenthesis when open>close
#3 Valid IF open==close==n 
def generateParenthesis(n):
    res = []

    def backtrack(open_n, closed_n, path):
        if open_n == closed_n == n:
            res.append(path)
            return

        if open_n < n:
            backtrack(open_n + 1, closed_n, path + "(")

        if closed_n < open_n:
            backtrack(open_n, closed_n + 1, path + ")")

    backtrack(0, 0, "")
    return res
ayush=generateParenthesis(3)
print(ayush)

#Better and efficient way to solve a problem 
# As we know that total no of Element in that stack will be n*n 
#uses a depth-first search (DFS) approach to generate all possible valid 
# combinations of parentheses for a given value of n. The dfs function keeps track
# of the number of open and closed parentheses encountered so far and constructs
# the combinations recursively.
def generateParenthesis(n):


    def dfs(left,right,s):

        if len(s)==n*2:
            return result.append(s) 
            
        if left<n:
            dfs(left+1,right,s+'(')
            
        if right< left:
            dfs(left,right+1,s+')')
        
    result=[]
    dfs(0,0,'')
    return result
ayush=generateParenthesis(4)
print(ayush)