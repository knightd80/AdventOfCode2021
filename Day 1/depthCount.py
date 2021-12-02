inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()
 
count = 0
depthCount = 0
currentValue = 0

for line in lines:
    if count > 0 and int(line) > currentValue:
        depthCount += 1
    currentValue = int(line)
    count += 1
    # print("line count: {}, line value: {}, depthCount: {}".format(count, line, depthCount))
print("Count of depths greater than preceeding = {} out of {}".format(depthCount, count))
