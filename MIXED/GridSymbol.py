NumOfRows = int(input("Please enter number of rows: "))
NumOfColumns = int(input("Please enter number of columns: "))
Symbol = input("Please enter desired symbol: ")

RowCounter = 0
ColumnCounter = 0

Result = ""

for i in range(0, NumOfRows):
    for z in range(0, NumOfColumns):
        Result = Result + Symbol
    
    Result = Result + "\n"
    
print(Result)