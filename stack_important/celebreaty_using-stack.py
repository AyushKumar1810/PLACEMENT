def celebrity(M, n):
    stack = []

    # Step 1: Push all people onto the stack
    for i in range(n):
        stack.append(i)

    # Step 2: Pop two people from the stack until only one person remains
    while len(stack) > 1:
        person1 = stack.pop()
        person2 = stack.pop()

        # Check if person1 knows person2
        if M[person1][person2] == 1:
            # person1 knows person2, so person1 cannot be the celebrity
            stack.append(person2)
        else:
            # person1 does not know person2, so person2 cannot be the celebrity
            stack.append(person1)

    # Step 3: Check if the remaining person is a celebrity
    celebrity_candidate = stack.pop()
    for i in range(n):
        if i != celebrity_candidate:
            # Check if the remaining person knows anyone else, or someone does not know the remaining person
            if M[celebrity_candidate][i] == 1 or M[i][celebrity_candidate] == 0:
                return -1

    return celebrity_candidate
input_matrix = [[0, 1, 0],
                [0, 0, 0],
                [1, 1, 1]]

n = 3

output = celebrity(input_matrix, n)
print("Celebrity index:", output)
