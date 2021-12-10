from statistics import median

inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

totalSyntaxScores = []

# Loop through each entry and check adjacent cells to see if it is lowest
for line in lines:
    syntaxValues = []
    syntaxValues[:] = line
    expectedValue = []
    for value in syntaxValues:
        if value == '(':
            expectedValue.append(')')
        elif value == '[':
            expectedValue.append(']')
        elif value == '{':
            expectedValue.append('}')
        elif value == '<':
            expectedValue.append('>')
        else:
            if value == expectedValue[len(expectedValue)-1]:
                expectedValue.pop()
            else:
                expectedValue = []
                break
    if len(expectedValue) > 0:
        expectedValue.reverse()
        totalSyntaxScore = 0
        for value in expectedValue:
            totalSyntaxScore *= 5
            if value == ')':
                totalSyntaxScore += 1
            elif value == ']':
                totalSyntaxScore += 2
            elif value == '}':
                totalSyntaxScore += 3
            elif value == '>':
                totalSyntaxScore += 4
        totalSyntaxScores.append(totalSyntaxScore)

print("Median Syntax Score: {};".format(median(totalSyntaxScores)))