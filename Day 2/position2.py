inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

horizontalPos = 0
aimPos = 0
depthPos = 0

for line in lines:
    items = line.split()
    if items[0] == "forward":
        horizontalPos += int(items[1])
        depthPos += int(items[1]) * aimPos
    elif items[0] == "up":
        aimPos -= int(items[1])
    elif items[0] == "down":
        aimPos += int(items[1])
print("Horizontal Position: {}; Depth: {}; Aim: {}; Multiplied: {};".format(horizontalPos, depthPos, aimPos, horizontalPos * depthPos))