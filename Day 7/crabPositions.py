inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

crabPositions = []
highestHorizontalPosition = 0
bestPosition = 0
totalFuel = 0

for crab in lines[0].split(","):
    crabPositions.append(int(crab))

for position in crabPositions:
    if position > highestHorizontalPosition:
        highestHorizontalPosition = position

for position in range(highestHorizontalPosition + 1):
    totalFuelTemp = 0
    for crab in crabPositions:
        totalFuelTemp += abs(crab - position)
    if totalFuel == 0 or totalFuelTemp < totalFuel:
        totalFuel = totalFuelTemp
        bestPosition = position

print("Best Horizontal Position: {}; Total Fuel: {};".format(bestPosition, totalFuel))