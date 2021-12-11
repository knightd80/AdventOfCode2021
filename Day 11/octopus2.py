inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

octopuses = []
octopusFlashStep = 0

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

#print("Initial Grid: {};".format(octopuses))
step = 1
synchronousFlash = False
while not synchronousFlash:
    # Update octopusCounts
    for index, octopusLine in enumerate(octopuses):
        for index2, octopus in enumerate(octopusLine):
            octopuses[index][index2] += 1
            if octopuses[index][index2] == 10:
                checkSurroundingCells(index, index2)
    # Determine octopus flashes
    synchronousFlash = True
    for index, octopusLine in enumerate(octopuses):
        for index2, octopus in enumerate(octopusLine):
            if octopuses[index][index2] <= 9:
                synchronousFlash = False
            if octopuses[index][index2] > 9:
                octopuses[index][index2] = 0
    if synchronousFlash:
        octopusFlashStep = step
        break
    step += 1
    #print("After Step {}: {};".format(step + 1, octopuses))

print("First Octopus Synchronous Flash at step: {};".format(octopusFlashStep))