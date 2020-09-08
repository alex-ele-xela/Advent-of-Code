wiresDict = {}


def partOne():
    instructionsStrings = []
    for instruction in open('circuit.txt', 'r') :
        instructionsStrings.append(instruction.rstrip('\n'))
    
    run = True
    while run:
        run = False
        for i, instruction in enumerate(instructionsStrings):
            performedInstruction = checkAndExecuteInstruction(instruction)

            if performedInstruction:
                instructionsStrings.pop(i)
            else :
                run = True
    
    return wiresDict['a']


def checkAndExecuteInstruction(instruction):
    instructionList = getInstructionList(instruction)

    if len(instructionList) == 3 :
        return assignSignalAndConfirm(instructionList)

    wireList = getWireList(instructionList)
    if checkWiresExist(wireList):
        if len(instructionList) == 4:
            bitwiseFunc = getBitwiseFunc(instructionList[0])
            func = instructionList[0]
        elif len(instructionList) == 5:
            bitwiseFunc = getBitwiseFunc(instructionList[1])
            func = instructionList[1]
        

        operandList = getOperandList(wireList)

        result = bitwiseFunc(operandList)

        wiresDict[instructionList[-1]] = result


        return True
    
    return False


def getInstructionList(instruction):
    return instruction.split(' ')


def assignSignalAndConfirm(instructionList):
    signalString = instructionList[0]
    if signalString.isdigit():
        signal = int(instructionList[0])
    else:
        try:
            signal = wiresDict[signalString]
        except:
            return False

    wiresDict[instructionList[-1]] = signal
    return True


def getWireList(instructionList):
    if len(instructionList) == 4:
        wireList = [instructionList[1]]
    elif len(instructionList) == 5:
        wireList = [instructionList[0], instructionList[2]]
    
    return wireList


def checkWiresExist(wireList):
    for wire in wireList:
        if (not wire in wiresDict.keys()) and (not wire.isdigit()):
            return False
    
    return True


def getBitwiseFunc(operator):
    if operator == 'AND':
        def func(operands):
            return operands[0] & operands[1]

    elif operator == 'OR':
        def func(operands):
            return operands[0] | operands[1]

    elif operator == 'NOT':
        def func(operands):
            return ~operands[0]

    elif operator == 'RSHIFT':
        def func(operands):
            return operands[0] >> operands[1]

    elif operator == 'LSHIFT':
        def func(operands):
            return operands[0] << operands[1]
    
    return func


def getOperandList(wireList):
    operandList = list(map(assignDigitOrWire, wireList))
    return operandList

def assignDigitOrWire(wire):
    if wire.isdigit():
        return int(wire)
    else:
        return wiresDict[wire]


def partTwo(a1):
    global wiresDict
    wiresDict = {'b' : a1}

    instructionsStrings = []
    for instruction in open('circuit.txt', 'r') :
        if not instruction.endswith('-> b\n') :
            instructionsStrings.append(instruction.rstrip('\n'))
    
    run = True
    while run:
        run = False
        for i, instruction in enumerate(instructionsStrings):
            performedInstruction = checkAndExecuteInstruction(instruction)

            if performedInstruction:
                instructionsStrings.pop(i)
            else :
                run = True
    
    return wiresDict['a']

a1 = partOne()
print("Part One a =", a1)

a2 = partTwo(a1)
print("Part Two a =", a2)