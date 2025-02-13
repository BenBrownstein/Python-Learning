
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    colWidths[0] = len(tableData[0][0])
    counter = len(tableData[0])
    counter2 = 0
    while counter != 0:
        for x in range(len(tableData)):
            if colWidths[x] < len(tableData[x][counter2]):
                colWidths[x] = len(tableData[x][counter2])
        counter -= 1
        counter2 += 1    

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end=" ")
        print()
printTable()
