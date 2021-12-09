inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

lavaTubes = []
basins = []

def checkSurroundingCells(index, index2):
    if int(lavaTubes[index][index2].split('b')[0]) != 9:
        # Top
        if index > 0:
            if 'b' in lavaTubes[index-1][index2] and 'b' not in lavaTubes[index][index2]:
                lavaTubes[index][index2] += 'b' + lavaTubes[index-1][index2].split('b')[1]
        # Bottom
        if index < len(lavaTubes) - 1:
            if 'b' in lavaTubes[index+1][index2] and 'b' not in lavaTubes[index][index2]:
                lavaTubes[index][index2] += 'b' + lavaTubes[index+1][index2].split('b')[1]
        # Left
        if index2 > 0:
            if 'b' in lavaTubes[index][index2-1] and 'b' not in lavaTubes[index][index2]:
                lavaTubes[index][index2] += 'b' + lavaTubes[index][index2-1].split('b')[1]
        # Right
        if index2 < len(lavaTube) - 1:
            if 'b' in lavaTubes[index][index2+1] and 'b' not in lavaTubes[index][index2]:
                lavaTubes[index][index2] += 'b' + lavaTubes[index][index2+1].split('b')[1]

for line in lines:
    lavaTubesLine = []
    lavaTubesLine[:] = line
    lavaTubes.append(lavaTubesLine)

# Loop through each entry and check adjacent cells
basinCount = 0
for index, lavaTube in enumerate(lavaTubes):
    for index2, height in enumerate(lavaTube):
        if int(lavaTubes[index][index2].split('b')[0]) != 9:
            checkSurroundingCells(index, index2)
            if 'b' not in lavaTubes[index][index2]:
                basins.append(0)
                lavaTubes[index][index2] += 'b' + str(basinCount)
                basinCount += 1
            for i in range(index, len(lavaTubes), 1):
                for j in range(index2, len(lavaTube), 1):
                    checkSurroundingCells(i,j)

for index, lavaTube in enumerate(lavaTubes):
    for index2, height in enumerate(lavaTube):
        if 'b' in lavaTubes[index][index2]:
            basins[int(lavaTubes[index][index2].split('b')[1])] += 1

basin1 = 0
basin2 = 0
basin3 = 0
for basinValue in basins:
    if basinValue > basin1:
        basin3 = basin2
        basin2 = basin1
        basin1 = basinValue
    elif basinValue > basin2:
        basin3 = basin2
        basin2 = basinValue
    elif basinValue > basin3:
        basin3 = basinValue

print(lavaTubes)
print(basins)
print("basin1: {}; basin2: {}; basin3: {};".format(basin1, basin2, basin3))
print("Three Largest Basins Product: {};".format(basin1 * basin2 * basin3))