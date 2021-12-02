inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

lineCount = 0
groupValue = 0
currentGroupValue = 0
depthCount = 0

while lineCount < (len(lines) - 2):
    if currentGroupValue == 0:
        currentGroupValue = int(lines[lineCount]) + int(lines[lineCount + 1]) + int(lines[lineCount + 2])
    else:
        groupValue = int(lines[lineCount]) + int(lines[lineCount + 1]) + int(lines[lineCount + 2])
        if groupValue > currentGroupValue:
            depthCount += 1
        currentGroupValue = groupValue
    lineCount += 1
    print("line count: {}, group value: {}, depthCount: {}".format(lineCount, groupValue, depthCount))

print("Count of depths greater than preceeding group = {} out of {}".format(depthCount, lineCount))
