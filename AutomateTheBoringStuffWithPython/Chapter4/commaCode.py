# Comma code
# example input ['apples', 'bananas', 'tofu', 'cats'] -> 'apples, bananas, tofu, and cats'

#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []

def commacodef(inputList):
    length = len(inputList)
    if(length == 0):
        return 'Input empty'
    result = ''
    
    for i in range(length):
        if(i < (length-1)):
            #print(inputList[i],end=', ')
            result += (inputList[i] + ', ')
        elif(length == 1):
            result += inputList[i]
        else:
            #print(inputList[i])
            result += ('and ' + inputList[i])
    return result

print(commacodef(spam))
