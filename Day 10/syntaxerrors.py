inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

totalSyntaxScore = 0

# Loop through each entry and check adjacent cells to see if it is lowest
for line in lines:
    syntaxValues = []
    syntaxValues[:] = line
    expectedValue = []
    for value in syntaxValues:
        print(expectedValue)
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
                print("Expected {}, found {};".format(expectedValue[len(expectedValue)-1],value))
                if value == ')':
                    totalSyntaxScore += 3
                elif value == ']':
                    totalSyntaxScore += 57
                elif value == '}':
                    totalSyntaxScore += 1197
                elif value == '>':
                    totalSyntaxScore += 25137
                break     

print("Total Syntax Score: {};".format(totalSyntaxScore))