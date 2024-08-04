'''matrix=[[1,2,3],
        [5,7,8],
        [15,12,41]]
print(matrix[1][2])
print(matrix[0][1])
print(len(matrix))
print(len(matrix[0]))

for i in matrix:
    for j in i:
        print(j)
'''

# matrix=[]

# for i in range(3):
#     temp=[]
#     for o in range(3):
#         value=int(input('Enter the number: '))
#         temp.append(value)
#     matrix.append(temp)

# print(matrix)

matrixA=[[1,4],[2,3]]
matrixB=[[5,8],[6,7]]
matrixC=[[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        matrixC[i][j]=matrixA[i][j]+matrixB[i][j]

print(matrixC)