def longestDecreasingPath(i, j):
    if i < 0 or j < 0 or i >= size or j >= size:
        return 0
    if state[i][j] != -1:
        return state[i][j]
    right = -1
    left = -1
    up = -1
    down = -1
    if j < size - 1 and matrix[i][j] > matrix[i][j + 1]:
        #print(str(matrix[i][j]) + "to" +  str(matrix[i][j+1]))
        right = 1 + longestDecreasingPath(i, j + 1)
    if j > 0 and matrix[i][j] > matrix[i][j - 1]:
        #print(str(matrix[i][j]) + "to" + str(matrix[i][j-1]))
        left = 1 + longestDecreasingPath(i, j - 1)
    if i > 0 and matrix[i][j] > matrix[i - 1][j]:
        #print(str(matrix[i][j]) + "to" + str(matrix[i-1][j]))
        up = 1 + longestDecreasingPath(i - 1, j)
    if i < size - 1 and matrix[i][j] > matrix[i + 1][j]:
        #print(str(matrix[i][j]) + "to" + str(matrix[i+1][j]))
        down = 1 + longestDecreasingPath(i + 1, j)
    state[i][j] = max(right, max(left, max(up, max(down, 1))))
    # print(state)
    return state[i][j]

num_input = input()
num_input = int(num_input)
for i in range(num_input):
    name, dimension_y, dimension_x = input().strip().split()
    dimension_y = int(dimension_y)
    dimension_x = int(dimension_x)
    matrix = [[0 for m in range(dimension_y)] for m in range(dimension_x)]
    for a in range(dimension_y):
        temp_list = input()
        example_list = [int(k) for k in temp_list.strip().split(' ')] #casting empty string
        matrix[a] = example_list
    result = 1
    size = dimension_x
    state = [[-1 for i in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            if state[i][j] == -1:
                longestDecreasingPath(i, j)
            result = max(result, state[i][j])
    print(name +  ": " +  str(result))
