inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

STEPCOUNT = 100
octopuses = []
octopusFlashCount = 0

def checkSurroundingCells(index, index2):
    # Top
    if index > 0:
        octopuses[index-1][index2] += 1
        if octopuses[index-1][index2] == 10:
            checkSurroundingCells(index-1, index2)
        if index2 > 0:
            octopuses[index-1][index2-1] += 1
            if octopuses[index-1][index2-1] == 10:
                checkSurroundingCells(index-1, index2-1)
        if index2 < len(octopusLine) - 1:
            octopuses[index-1][index2+1] += 1
            if octopuses[index-1][index2+1] == 10:
                checkSurroundingCells(index-1, index2+1)
    # Bottom
    if index < len(octopuses) - 1:
        octopuses[index+1][index2] += 1
        if octopuses[index+1][index2] == 10:
            checkSurroundingCells(index+1, index2)
        if index2 > 0:
            octopuses[index+1][index2-1] += 1
            if octopuses[index+1][index2-1] == 10:
                checkSurroundingCells(index+1, index2-1)
        if index2 < len(octopusLine) - 1:
            octopuses[index+1][index2+1] += 1
            if octopuses[index+1][index2+1] == 10:
                checkSurroundingCells(index+1, index2+1)
    # Left
    if index2 > 0:
        octopuses[index][index2-1] += 1
        if octopuses[index][index2-1] == 10:
            checkSurroundingCells(index, index2-1)
    # Right
    if index2 < len(octopuses) - 1:
        octopuses[index][index2+1] += 1
        if octopuses[index][index2+1] == 10:
            checkSurroundingCells(index, index2+1)

for line in lines:
    octopusLine = []
    octopusLine = list(map(int, line))
    octopuses.append(octopusLine)

print("Initial Grid: {};".format(octopuses))
for step in range(STEPCOUNT):
    # Update octopusCounts
    for index, octopusLine in enumerate(octopuses):
        for index2, octopus in enumerate(octopusLine):
            octopuses[index][index2] += 1
            if octopuses[index][index2] == 10:
                checkSurroundingCells(index, index2)
    # Determine octopus flashes
    for index, octopusLine in enumerate(octopuses):
        for index2, octopus in enumerate(octopusLine):
            if octopuses[index][index2] > 9:
                octopusFlashCount += 1
                octopuses[index][index2] = 0
    print("After Step {}: {};".format(step + 1, octopuses))

print("Octopus Flash count: {};".format(octopusFlashCount))