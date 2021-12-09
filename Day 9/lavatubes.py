inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

lavaTubes = []
lowestPointSum = 0

for line in lines:
    lavaTubesLine = []
    lavaTubesLine[:] = line
    lavaTubes.append(lavaTubesLine)

# Loop through each entry and check adjacent cells to see if it is lowest
for index, lavaTube in enumerate(lavaTubes):
    for index2, height in enumerate(lavaTube):
        isLowest = True
        # Top
        if index > 0:
            if lavaTubes[index][index2] >= lavaTubes[index-1][index2]:
                isLowest = False
        # Bottom
        if index < len(lavaTubes) - 1:
            if lavaTubes[index][index2] >= lavaTubes[index+1][index2]:
                isLowest = False
        # Left
        if index2 > 0:
            if lavaTubes[index][index2] >= lavaTubes[index][index2-1]:
                isLowest = False
        # Right
        if index2 < len(lavaTube) - 1:
            if lavaTubes[index][index2] >= lavaTubes[index][index2+1]:
                isLowest = False
        if isLowest:
            lowestPointSum += (int(height) + 1)

print(lavaTubes)
print("Lowest Point Sum: {};".format(lowestPointSum))