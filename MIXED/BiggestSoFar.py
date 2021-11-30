BiggestSoFar = int(input("Enter the number: "))

Counter = 1
MaxCount = 10

for i in range(0, MaxCount):
    NextNumber = int(input("Enter Next Number: "))
    
    Counter = Counter + 1

    if NextNumber > BiggestSoFar:
        BiggestSoFar = NextNumber

print("The Number is Biggest so far is: ", BiggestSoFar)

"""

Pseuducode:

INPUT BiggestSoFar
Counter <- 1
REPEAT
    INPUT NextNumber
    Counter <- Counter + 1
    IF NextNumber > BiggestSoFar
        THEN
            BiggestSoFar <- NextNumber
    ENDIF
UNTIL Counter= 10
OUTPUT BiggestSoFar

"""