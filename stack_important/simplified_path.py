#So the built-in function .split() come up in my mind, which is a good way to 
#convert string into list, this will help a lot.
#Let's still take Leettcode's example of the path. 
#If path is "/../abc//./def/", then path.split('/') gonna be
# [' ', '..', 'abc', ' ', '.', 'def', ' ']
def simplifyPath(path):
    stack = []
    dirs = path.split('/')

    for directory in dirs:
        if directory == '..':
            if stack:
                stack.pop()
        elif directory and directory != '.':
            stack.append(directory)

    return '/' + '/'.join(stack)

# Example usage
input_path = "/a//b/c/../d/./e"
simplified_path = simplifyPath(input_path)
print("Simplified path:", simplified_path)
