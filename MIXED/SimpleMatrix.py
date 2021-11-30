
NumberOfRows = int(input("Please enter number of rows of the matrix: "))
NumberOfColumns = int(input("Please enter number of columns of the matrix: "))
MatrixSymbol = input("Please enter the symbol of the matrix: ")
InsertRowPosition = int(input("Please enter the desired row position to insert 23 (EX: 1): "))
InsertColumnPosition = int(input("Please enter the desired column position to insert 23 (EX: 2): "))

if InsertRowPosition > NumberOfRows or InsertColumnPosition > NumberOfColumns:
    raise Exception("Row or column position cannot be greater than number of total rows or columns.")

MatrixArray = []

for i in range(0, NumberOfRows):
    InitialArray = []
    
    for j in range(0, NumberOfColumns):
        if i == InsertRowPosition - 1 and j == InsertColumnPosition - 1:
            InitialArray.append(23)
        else:
            InitialArray.append(MatrixSymbol)
        
    MatrixArray.append(InitialArray)
        
print(MatrixArray)