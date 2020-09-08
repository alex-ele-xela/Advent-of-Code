def isVowel(char) :
    vowels = ('a', 'e', 'i', 'o', 'u')
    return char in vowels

def hasThreeVowels(string) :
    vowelCount = 0

    for char in string:
        if isVowel(char):
            vowelCount += 1
    
    if vowelCount >= 3:
        return True
    else:
        return False

def hasDoubleLetter(string) :
    firstChar = string[0]

    for secondChar in string[1:]:
        if secondChar == firstChar:
            return True
        
        firstChar = secondChar
    
    return False

def doesNotHaveRestrictedString(string) :
    restrictedStrings = ('ab', 'cd', 'pq', 'xy')

    for restrictedString in restrictedStrings:
        if restrictedString in string:
            return False
    
    return True

def satisfiesConditions(string, conditionList) :
    flag = True

    for condition in conditionList:
        flag = flag and condition(string)
    
    return flag

def partOne() :
    niceStringsCount = 0
    for string in open('stringsFile.txt', 'r'):
        if satisfiesConditions(string, [hasThreeVowels, hasDoubleLetter, doesNotHaveRestrictedString]):
            niceStringsCount += 1

    print("Number of Nice Strings by Part One =", niceStringsCount)



def hasRepeatedLetterPair(string) :
    for i in range(len(string)-1):
        letterPair = string[i:i+2]

        stringBefore = string[:i]
        stringAfter = string[i+2:]

        if (letterPair in stringBefore) or (letterPair in stringAfter) :
            return True
    
    return False

def hasRepeatedLetter(string) :
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    
    return False

def partTwo() :
    niceStringsCount = 0
    for string in open('stringsFile.txt', 'r'):
        if satisfiesConditions(string, [hasRepeatedLetter, hasRepeatedLetterPair]):
            niceStringsCount += 1

    print("Number of Nice Strings by Part Two =", niceStringsCount)


partOne()
partTwo()