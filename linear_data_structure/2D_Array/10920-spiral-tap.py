# solution is correct got TLE, it's more mathematical problem then 2D array

def perform_operation(matrix, row, col, count, num, operation, sz, p):
    for k in range(1, c+1):
        if operation=='-':
            row-=1
        else:
            row+=1
        num+=1
        # print(f" inside row {row} {col}")
        matrix[row][col]=num
        
        if row==0 or row==sz-1 or p==num:
            break
    if c!=sz and p!=num:
        for f in range(1, c+1):
            if operation=='-':
                col-=1
            else:
                col+=1
            num+=1
            # print(f" inside col {row} {col}")
            matrix[row][col]=num
            
            if col==0 or col==sz-1 or p==num:
                break
    # print(matrix)
    return matrix, num, row, col


while True:
    sz, p = map(int, input().split())
    # handle edge case where sz=1
    if sz==p and p==0:
        break
    # matrix = [[None]*sz]*sz due to this command python internally share memory for all sz rows instead use list comprhension when creating 2d stucture
    matrix = [[None]*sz for _ in range(sz)]
    num=1
    row, col = int((sz-1)/2), int((sz-1)/2)
    if p==num:
        print(f"Line = {sz-row}, column = {col+1}.")
    matrix[row][col]=num
    for c in range(1, sz+1):
        if c%2==0:
            operation='+'
        else :
            operation='-'
        matrix, num, row, col = perform_operation(matrix, row, col, c, num, operation, sz, p)
        
        if p==num:
            print(f"Line = {sz-row}, column = {col+1}.")
            break
        
    
    # print(matrix)