matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
#Checking the number of rows

print(len(matrix))
print(len(matrix[0]))  #Checking the number of columns in the first row

#Accessing specific elements
print(matrix[1][2])  # Should print 6
print(matrix[2][2])  # Should print 9

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = "")
    print("\n")
        
