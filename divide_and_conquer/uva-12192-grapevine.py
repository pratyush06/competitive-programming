def binary_search(lower_bound, search_space):
    if not search_space:
        return None
    mid = len(search_space)//2

    if search_space[mid]>lower_bound:
        return binary_search(lower_bound, search_space[:mid])
    else:
        answer = binary_search(lower_bound, search_space[mid+1:])
        if answer is None:
            return mid
        return answer

row, column =map(int, input().split(" "))
# matrix = [[None] * column for _ in range(row)]
# for i in range(row):
#     for j in range(column):
#         matrix[i][j]=int(input())
matrix = [[13, 21, 25, 33, 34], [16, 21, 33, 35, 35], [16, 33, 33, 45, 60], [23, 51, 66, 83, 93]]
print(matrix)
num_of_quiries = int(input())
for k in range(num_of_quiries):
    L, U = map(int, input().split(" "))
    answer_to_the_first_query = None
    for N in range(row):
        # find the first value which greater than and equal to L
        # print(matrix[N])
        starting_pointer = binary_search(L, matrix[N])
        # import pdb;pdb.set_trace()
        # print(starting_pointer)
        k=1
        max_square=1
        # traverse diagonaly to find the value which is lower than to equal to U
        while (N+k)<row and (starting_pointer+k)<column:
            if matrix[N+k][starting_pointer+k]<=U:
                # print("inside if")
                max_square+=1
                k+=1
            else:
                # print(" inside else")
                break
        # print(f"max_square {max_square} and current ros {N}")

        if max_square>1 and (answer_to_the_first_query is None or answer_to_the_first_query<max_square):
            # import pdb;pdb.set_trace()
            answer_to_the_first_query = max_square
    print(f"answer to lower bound {L} and upper bound {U} is {answer_to_the_first_query}")
