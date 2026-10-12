import numpy as np



"""
# Defining an array
arr1 = np.array([1, 2, 3, 4, 'a', 'b', 10])



# Printing an arrray and its type
print(arr1, type(arr1))


# Looping inside the array
for x in arr1:
    print(x)
    


# Defining a higher dimension matrix
mat1 = np.array([
    [1, 2, 3, 4], ['a', 'b', 'c', 'd'], [2, 4, 8, 16],
    [1, 2, 3, 4], ['a', 'b', 'c', 'd'], [2, 4, 8, 16],
    [1, 2, 3, 4], ['a', 'b', 'c', 'd'], [2, 4, 8, 16]
])

for x in mat1:
    for y in x:
        print(y, end=" ")
    print()
    

# Concatenating ( Joining the two arrays one after the another ) and stacking two arrays ( Piling up the matrix on top of each other )

arrx = np.array(
    [
     [1, 2], [3, 4]
    ]
)

arry = np.array(
    [
     ['a', 'b'], [2, 16]
    ]
)


arr_conc = np.concatenate((arrx, arry))
arr_stack = np.stack((arrx, arry), axis=0) # axis = 0 --> (top, bottom) stacking; axis = 1 --> (front, behind) stacking; axis = 2 --> (left, right) stracking

print(arr_stack)


# Zero matrix
arr_zer = np.zeros((4, 3, 2)) 

print(arr_zer) # here the (i, j, k) defines the matrix shape and it says that the matrix is made in 3 dimensions with 4 sheets on top of each other, 3 sheets from left to right, 2 sheets from front to back


# Identity matrix
arr_iden = np.eye(3, 3)

print(arr_iden)


# matrix algebra

A = np.array([
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 3]
])
B = np.array([
    [2, 4, 64],
    [8, 16, 10],
    [32, 64, 0.01]
])

mat_em = A * B # It is the multiplication of matrix element wise
mat_ed  = A / B # It is the division of matrix element wise
mat_cross = A @ B # It is the matrix algebra multiplication
mat_mul = np.matmul(A, B) # Alternative to matrix algebra multiplication


print(mat_em)
print(mat_ed)
print(mat_cross)
print(mat_mul)

v1 = np.array([
    [1, 2, 3],
    [2, 3, 4]
])

print(np.ndim(v1))

v2 = np.array([
    [4, 2, 3],
    [2, 3, 1],
    [6, 4, 3]
])
print(np.ndim(v2))


# Dot Product of two vectors
A_dot_B = np.dot(v1, v2)

print(A_dot_B) # Prints the dot product of the two vectors (Matrix algebra multiplication)
print(np.ndim(A_dot_B)) # Prints the dimension of the matrix
"""




















## Linear Algebra





# more tools from numpy reference on linear algebra "https://numpy.org/doc/stable/reference/routines.linalg.html"


