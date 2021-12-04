inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

# TODO: consider using numpys for this problem

callOrder = ""
bingoCards = []
unmarkedSum = 0
lastCall = 0
winningCard = []
winningCards = []

def checkForWinningCard(bingoCard):
    # check rows
    for x in range(5):
        for y in range(5):
            if "C" not in bingoCard[x][y]:
                break
            elif y == 4:
                winningCard = bingoCard.copy()
                return bingoCard
    # check columns
    for y in range(5):
        for x in range(5):
            if "C" not in bingoCard[x][y]:
                break
            elif x == 4:
                winningCard = bingoCard.copy()
                return bingoCard
    return []

def checkAllWinningCards():
    for bingoCard in winningCards:
        if bingoCard == "N":
            return False
    return True

def calculateUnmarkedSum(bingoCard):
    unmarkedSum = 0
    for x in range(5):
        for y in range(5):
            if "C" not in bingoCard[x][y]:
                unmarkedSum += int(bingoCard[x][y])
    return unmarkedSum

row = 0
cardNumber = 0
bingoRow = 0
for line in lines:
    if row == 0:
        callOrder = line.split(",")
    elif line == "":
        pass
    else:
        if bingoRow == 0:
            bingoCards.append([])
            winningCards.append("N")
        data = line.split()
        bingoCards[cardNumber].append(data)
        bingoRow += 1
    if bingoRow == 5:
        cardNumber += 1
        bingoRow = 0
    row += 1

for call in callOrder:
    lastCall = int(call)
    bingoCardNumber = 0
    for bingoCard in bingoCards:
        if winningCards[bingoCardNumber] != "W":
            for x in range(5):
                for y in range(5):
                    if bingoCard[x][y] == call:
                        bingoCard[x][y] = bingoCard[x][y] + "C"
            # Check for a winning card
            winningCard = checkForWinningCard(bingoCard)
            if winningCard:
                winningCards[bingoCardNumber] = "W"
                # Check if all other Cards have been winners
                lastWinner = checkAllWinningCards()
                if lastWinner:
                    break
        bingoCardNumber += 1
    else:
        continue
    break

# Calculate unmarkedSum for last Winning Card
unmarkedSum = calculateUnmarkedSum(winningCard)

print("Bingo Card: {}; Last Called: {}; Sum of Unmarked numbers: {}; Final Score: {};".format(winningCard, lastCall, unmarkedSum, lastCall * unmarkedSum))