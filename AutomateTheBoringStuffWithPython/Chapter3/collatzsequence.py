#Collatz Sequence

import sys

def collatz(collatzNumber):
    if((collatzNumber % 2) == 0):
        collatzNumber = collatzNumber // 2
    elif((collatzNumber % 2) == 1):
        collatzNumber = 3 * collatzNumber + 1
    else:
        print('I dont know how but I broke it')
        sys.exit()
    if(collatzNumber != 1):
        print(collatzNumber)
        collatz(collatzNumber)
    else:
        print('It ended again in ' + str(collatzNumber))

while True:
    try:
        inputNumber = int(input())
    except ValueError:
        print('Invalid input, only use inputs that can be converted into an int.')
        continue
    collatz(inputNumber)


