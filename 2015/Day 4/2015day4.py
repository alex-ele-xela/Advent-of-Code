import hashlib
from time import time

puzzleInput = 'ckczppom'

def getHexHash(string):
    hashedString = hashlib.md5(string.encode('utf-8')).hexdigest()

    return hashedString


def startsWithn0s (n, string) :
    if string[:n] == '0'*n:
        return True
    else :
        return False

def main(puzzleInput):
    answer = 1
    while True :
        stringToCheck = puzzleInput + str(answer)

        hexHash = getHexHash(stringToCheck)

        if startsWithn0s(5, hexHash) :
            return answer
            
        answer += 1

print("Answer =", main(puzzleInput))