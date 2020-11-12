'''Shashank Rao
RUID: 185005733
This is the matrix calculator problem which involves
calculating several characteristics of 1 or more matrices
such as sum, product, and determinants'''

def dimension(M):
    return len(M), len(M[0])

def row(M, i):
    return M[i - 1]

def column(M, j):
    return [row[j - 1] for row in M]

def matrix_sum(A, B):
    if dimension(A) == dimension(B):
        matrix_sums = [[] for r in A]
        for row in matrix_sums:
            for x in A[0]:
                row.append(A[matrix_sums.index(row)][len(row)] +
                           B[matrix_sums.index(row)][len(row)])
        return matrix_sums
    else:
        print('The dimensions of both matrices need to be the same')
        return

def matrix_difference(A, B):
    if dimension(A) == dimension(B):
        matrix_differences = [[] for r in A]
        for row in matrix_differences:
            for x in A[0]:
                row.append(A[matrix_differences.index(row)][len(row)] -
                           B[matrix_differences.index(row)][len(row)])
        return matrix_differences
    else:
        print('The dimensions of both matrices need to be the same')
        return

def matrix_product(A, B):
    if dimension(A)[1] == dimension(B)[0]:
        matrix_products = [[] for r in A]
        counter = 0
        for i in matrix_products:
            temp_row = row(A, counter + 1)
            for x in range(len(temp_row)):
                new_column = column(B, x + 1)
                value = 0
                for r in range(len(new_column)):
                    value += (temp_row[r] * new_column[r])
                i.append(value)
            counter += 1
        return matrix_products
        
    else:
        print('The dimensions do not match for the product calculation')
        return

def reduce_matrix(M, i, j):
    reduce_matrices = [rows[:] for rows in M]
    reduce_matrices.remove(reduce_matrices[i - 1])
    for x in reduce_matrices:
        del x[j - 1]
    return reduce_matrices

def determinant(M):
    if dimension(M)[0] == dimension(M)[1]:
        if dimension(M)[0] == 1:
            return M[0][0]
        elif dimension(M)[0] == 2:
            return (M[0][0] * M[1][1]) - (M[0][1] * M[1][0])
        elif dimension(M)[0] > 2:            
            det_val = 0
            x = 1
            for i in range(1, dimension(M)[0] + 1):
                det_val += (M[0][i - 1] * x * determinant(reduce_matrix(M, 1, i)))
                x *= -1
            return det_val       
    else:
        print('The dimensions do not yield a square')
        return
    

def pretty_print(M):
    for row in M:
        output = ''
        for i in row:
            output = output + str(i) + '\t'
        print(output)
    return



if __name__ == "__main__":
    print("Testing module problem2 (Assignment #3): ")
    A = [[5, 3, -1], [9, 4, 12]]
    B = [[6, 9, 12], [-8, 6, -4], [7, 11, 13]]
    C = [[0, -21, -1], [11, 13, 17]]
    
    print("Three matrices have been created.")
    print("\nMatrix A equals \n")
    pretty_print(A)
    print("\nMatrix B equals \n")
    pretty_print(B)
    print("\nMatrix C equals \n")
    pretty_print(C)

    print("Matrix A has dimension ", dimension(A))
    print("Matrix B has dimension ", dimension(B))
    print("Matrix C has dimension ", dimension(C))

    print()
    print("The second row of matrix A is: ", row(A, 2))
    print("The third column of matrix B is: ", column(B, 3))
    print("The second column of matrix C is: ", column(C, 2))

    print()
    D = matrix_sum(A, C)
    print("The sum of matrices A and C is: \n")
    pretty_print(D)

    D = matrix_difference(C, A)
    print("The difference of matrices C and A is: \n")
    pretty_print(D)

    D = matrix_product(A, B)
    print("The product of  matrices A and B is: \n")
    pretty_print(D)

    D = matrix_product(A, C)
    print()

    D = reduce_matrix(A, 1, 1)
    print("Matrix obtained by removing row 1, column 1 of matrix A: \n")
    pretty_print(D)

    D = reduce_matrix(B, 3, 2)
    print("Matrix obtained by removing row 3, column 2 of matrix B: \n")
    pretty_print(D)

    D = determinant(B)
    print("The determinant of matrix B is: ", D)

    print("\nGoodbye!")
