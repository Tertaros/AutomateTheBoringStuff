
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(inputTable):
    colWidths = [0] * len(inputTable)

    for i in range(len(colWidths)):
        colWidths[i] = len(max(inputTable[i], key=len))

    print(colWidths)
    maxWidth = max(colWidths)
    print(maxWidth)

    for y in range(len(inputTable[0])):
        for x in range(len(colWidths)):
            print(inputTable[x][y].rjust(colWidths[0]),end=' ')
        print()

printTable(tableData)

