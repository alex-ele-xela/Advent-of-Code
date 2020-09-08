currentLocation = {
    'santa' : (0,0),
    'robo' : (0,0)
}
visitedLocations = {
    'santa' : [(0,0)],
    'robo' : [(0,0)]
}

def setNewLocation(person, direction) :
    global currentLocation

    if direction == '^':
        currentLocation[person] = (currentLocation[person][0] - 1, currentLocation[person][1])
    elif direction == '>':
        currentLocation[person] = (currentLocation[person][0], currentLocation[person][1] + 1)
    elif direction == '<':
        currentLocation[person] = (currentLocation[person][0], currentLocation[person][1] - 1)
    elif direction == 'v':
        currentLocation[person] = (currentLocation[person][0] + 1, currentLocation[person][1])

def isCurrentLocationVisited(person):
    flag = currentLocation[person] in visitedLocations[person]
    return flag

def modifyVisitedLocations(person):
    global visitedLocations

    visitedLocations[person].append(currentLocation[person])
    
def travelAndModify(person, direction) :
    setNewLocation(person, direction)

    if not isCurrentLocationVisited(person):
        modifyVisitedLocations(person)

with open('directionsFile.txt', 'r') as source :
    directions = source.read(2)

    while directions:
        travelAndModify('santa', directions[0])
        
        if len(directions) == 2:
            travelAndModify('robo', directions[1])

        directions = source.read(2)
        
uniqueHousesDelivered = set(visitedLocations['santa'] + visitedLocations['robo'])
print("Total Houses Delivered To =", len(uniqueHousesDelivered))