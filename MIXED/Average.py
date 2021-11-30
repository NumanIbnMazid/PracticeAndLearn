
SumOfNums = 0

Average = 0

TotalNums = 0

MaxNumsToInput = 5

while TotalNums <= (MaxNumsToInput - 1):
    
    TakenNumber = int(input(f"Please Enter a Number {TotalNums + 1}: "))
    
    SumOfNums = TakenNumber + SumOfNums
    Average = SumOfNums / (TotalNums + 1)
    
    TotalNums += 1
    
print("The average is: ", Average)