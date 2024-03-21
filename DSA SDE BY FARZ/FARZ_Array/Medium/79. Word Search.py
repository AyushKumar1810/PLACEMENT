# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

def exist(board, word):
    def dfs(i, j, k):
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        tmp, board[i][j] = board[i][j], '/'
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in directions:
            if dfs(i + x, j + y, k + 1):
                return True

        board[i][j] = tmp
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True

    return False
# Example Input
board_example = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word_example = "ABCCED"

# Using the exist function
result = exist(board_example, word_example)

# Displaying the result
print(result)  # This will print True or False based on whether the word can be formed or not
