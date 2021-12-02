inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

horizontalPos = 0
depthPos = 0

for line in lines:
    items = line.split()
    if items[0] == "forward":
        horizontalPos += int(items[1])
    elif items[0] == "up":
        depthPos -= int(items[1])
    elif items[0] == "down":
        depthPos += int(items[1])
print("Horizontal Position: {}; Depth: {}; Multiplied: {};".format(horizontalPos, depthPos, horizontalPos * depthPos))