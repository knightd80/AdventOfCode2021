inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

simpleSegmentCount = 0

for segment in lines:
    input, output = segment.split("|")
    for sample in output.split():
        if len(sample) == 2 or len(sample) == 3 or len(sample) == 4 or len(sample) == 7:
            simpleSegmentCount += 1

print("Simple Segment Count: {};".format(simpleSegmentCount))