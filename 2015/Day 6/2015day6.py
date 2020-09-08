ON, OFF = 1, -1
lightGrid = [[0 for i in range(1000)] for i in range(1000)]

def getStartAndEndValues(startCoord, endCoord):
    startRow, startCol = startCoord
    endRow, endCol = endCoord

    return (startRow, startCol, endRow, endCol)

def turnOnOrOff(action):
    def takeAction(startCoord, endCoord):
        startRow, startCol, endRow, endCol = getStartAndEndValues(startCoord, endCoord)

        for row in range(startRow, endRow+1):
            for col in range(startCol, endCol+1):
                lightGrid[row][col] += action
                lightGrid[row][col] = 0 if lightGrid[row][col] < 0 else lightGrid[row][col]
    
    return takeAction

def toggle(startCoord, endCoord):
    startRow, startCol, endRow, endCol = getStartAndEndValues(startCoord, endCoord)

    for row in range(startRow, endRow+1):
        for col in range(startCol, endCol+1):
            lightGrid[row][col] += 2

def getAction(instruction):
    if instruction.startswith('turn on'):
        return turnOnOrOff(ON)
    if instruction.startswith('turn off'):
        return turnOnOrOff(OFF)
    if instruction.startswith('toggle'):
        return toggle

def getCoordTuples(instruction):
    instructionList = instruction.split(' ')

    startCoord = tuple( map(int, instructionList[-3].split(',')) )
    endCoord = tuple( map(int, instructionList[-1].split(',')) )

    return (startCoord, endCoord)

def executeInstruction(instruction):
    action = getAction(instruction)

    startCoord, endCoord = getCoordTuples(instruction)

    action(startCoord, endCoord)

def countLitLights():
    counter = 0
    for row in lightGrid:
        for light in row:
            if light == ON:
                counter += 1
    
    return counter

def calculateBrightness():
    brightness = 0
    for row in lightGrid:
        for light in row:
            brightness += light
    
    return brightness

def main():
    for instruction in open('instructionList.txt', 'r'):
        executeInstruction(instruction)
    
    brightness = calculateBrightness()
    print("Brightness =", brightness)

main()