inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

# TODO: consider using numpys for this problem

RANGE = 1000
ventsGrid = []
overlapCount = 0

for column in range(RANGE):
    ventsGrid.append([])
    for row in range(RANGE):
        ventsGrid[column].append(0)

for line in lines:
    segment = line.split("->")
    segmentStart = segment[0].split(",")
    segmentFinish = segment[1].split(",")

    if int(segmentStart[0]) == int(segmentFinish[0]) or int(segmentStart[1]) == int(segmentFinish[1]):
        rowStart = int(segmentStart[0]) if int(segmentStart[0]) < int(segmentFinish[0]) else int(segmentFinish[0])
        rowFinish = int(segmentFinish[0]) if int(segmentFinish[0]) > int(segmentStart[0]) else int(segmentStart[0])
        colStart = int(segmentStart[1]) if int(segmentStart[1]) < int(segmentFinish[1]) else int(segmentFinish[1])
        colFinish = int(segmentFinish[1]) if int(segmentFinish[1]) > int(segmentStart[1]) else int(segmentStart[1])
        for column in range(colStart, colFinish + 1):
            #print("segmentRowStart: {}; segmentRowFinish: {};".format(rowStart,rowFinish))
            for row in range(rowStart, rowFinish + 1):
                #print("segmentColStart: {}; segmentColFinish: {};".format(colStart,colFinish))
                ventsGrid[column][row] += 1

for row in range(RANGE):
    for column in range(RANGE):
        if ventsGrid[row][column] >= 2:
            overlapCount += 1

#print("Vents Grid: {}; Overlap Count: {};".format(ventsGrid, overlapCount))
print("Overlap Count: {};".format(overlapCount))