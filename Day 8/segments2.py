inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

LETTERS = ['a','b','c','d','e','f','g']
totalOutputValue = 0

for segment in lines:
    input, output = segment.split("|")
    # Need to determine digits from input

    #  dddd
    # e    a
    # e    a
    #  ffff
    # g    b
    # g    b
    #  cccc

    # To cover all numbers
    # a occurs 8 times, ** b occurs 9 times **, c occurs 7 times, d occurs 8 times
    # ** e occurs 6 times **, f occurs 7 times, ** g occurs 4 times **

    # 2 digits = 1 (a and b above)
    # 3 digits = 7 (d,a and b above)
    # 4 digits = 4 (e,f,a and b above)
    # 7 digits = 8 (all letters above)
    # missing middle = 0 (missing f above)
    # missing bottom left = 9 (missing g above)
    # missing top right = 6 (missing a above)
    # missing top and bottom left = 3 (missing e and g above)
    # missing top left and bottom right = 2 (missing e and b above)
    # missing top right and bottom left = 5 (missing a and g above)

    tempDigits = ["","","","","","","","","",""]
    digitCount = [0,0,0,0,0,0,0]
    positions = ["","","","","","",""]
    leftToProcess = []
    for digit in input.split():
        if 'a' in digit:
            digitCount[0] += 1
        if 'b' in digit:
            digitCount[1] += 1
        if 'c' in digit:
            digitCount[2] += 1
        if 'd' in digit:
            digitCount[3] += 1
        if 'e' in digit:
            digitCount[4] += 1
        if 'f' in digit:
            digitCount[5] += 1
        if 'g' in digit:
            digitCount[6] += 1
        if len(digit) == 2:
            tempDigits[1] = digit
        elif len(digit) == 3:
            tempDigits[7] = digit
        elif len(digit) == 4:
            tempDigits[4] = digit
        elif len(digit) == 7:
            tempDigits[8] = digit
        else:
            leftToProcess.append(digit)
    
    # get position of letters we know based on occurance
    for index, count in enumerate(digitCount):
        if count == 9:
            positions[5] = LETTERS[index]
        elif count == 6:
            positions[1] = LETTERS[index]
        elif count == 4:
            positions[4] = LETTERS[index]
    # work out top letter by getting leftover from 1 and 7
    positions[0] = tempDigits[7].translate({ ord(c): None for c in tempDigits[1] })
    # work out top right based on occurance
    for index, count in enumerate(digitCount):
        if count == 8 and positions[0] != LETTERS[index]:
            positions[2] = LETTERS[index]

    # work out bottom letter by getting leftover from 8 based on positions we already know and #4
    tempEight=tempDigits[8]
    for letter in positions:
        tempEight = tempEight.translate({ ord(c): None for c in letter })
    tempEight = tempEight.translate({ ord(c): None for c in tempDigits[4] })
    positions[6] = tempEight

    # work out middle letter by getting remaining
    tempEight=tempDigits[8]
    for letter in positions:
        tempEight = tempEight.translate({ ord(c): None for c in letter })
    positions[3] = tempEight

    # Determine remaining numbers: 0,2,3,6,5,9
    zero = ""
    two = ""
    three = ""
    five = ""
    six = ""
    nine = ""
    for x in [0,1,2,4,5,6]:
        zero += positions[x]
    for x in [0,2,3,4,6]:
        two += positions[x]
    for x in [0,2,3,5,6]:
        three += positions[x]
    for x in [0,1,3,5,6]:
        five += positions[x]
    for x in [0,1,3,4,5,6]:
        six += positions[x]
    for x in [0,1,2,3,5,6]:
        nine += positions[x]
    for digit in leftToProcess:
        tempZero = digit.translate({ ord(c): None for c in zero }) + zero.translate({ ord(c): None for c in digit })
        tempTwo = digit.translate({ ord(c): None for c in two }) + two.translate({ ord(c): None for c in digit })
        tempThree = digit.translate({ ord(c): None for c in three }) + three.translate({ ord(c): None for c in digit })
        tempFive = digit.translate({ ord(c): None for c in five }) + five.translate({ ord(c): None for c in digit })
        tempSix = digit.translate({ ord(c): None for c in six }) + six.translate({ ord(c): None for c in digit })
        tempNine = digit.translate({ ord(c): None for c in nine }) + nine.translate({ ord(c): None for c in digit })
        if len(tempZero) == 0:
            tempDigits[0] = digit
        if len(tempTwo) == 0:
            tempDigits[2] = digit
        if len(tempThree) == 0:
            tempDigits[3] = digit
        if len(tempFive) == 0:
            tempDigits[5] = digit
        if len(tempSix) == 0:
            tempDigits[6] = digit
        if len(tempNine) == 0:
            tempDigits[9] = digit

    print("positions: {};".format(positions))
    print("Digits: {};".format(tempDigits))

    # Calculate output based on input
    digits = ""
    for digit in output.split():
        for index, value in enumerate(tempDigits):
            temp = value.translate({ ord(c): None for c in digit })
            temp2 = digit.translate({ ord(c): None for c in value })
            if len(temp) == 0 and len(temp2) == 0:
                digits += str(index)
                break
    totalOutputValue += int(digits)

print("Total Output Value: {};".format(totalOutputValue))