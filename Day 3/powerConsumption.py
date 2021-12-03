inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

onCount = []
offCount = []
gammaRateBin = []
epsilonRateBin = []
gammaRate = 0
epsilonRate = 0

for line in lines:
    items = list(line)
    if not onCount:
        onCount = [0] * len(items)
        offCount = [0] * len(items)
        gammaRateBin = [0] * len(items)
        epsilonRateBin = [0] * len(items)
    pos = 0
    for item in items:
        if int(item) == 0:
            offCount[pos] += 1
        if int(item) == 1:
            onCount[pos] += 1
        pos += 1

for index in range(len(onCount)):
    if onCount[index] > offCount[index]:
        gammaRateBin[index] = 1
    if offCount[index] > onCount[index]:
        epsilonRateBin[index] = 1

gammaRate = int(''.join(str(int) for int in gammaRateBin),2)
epsilonRate = int(''.join(str(int) for int in epsilonRateBin),2)
    
print("Gamma Rate: {}; Epsilon Rate: {}; Power Consumption: {};".format(gammaRate, epsilonRate, gammaRate * epsilonRate))