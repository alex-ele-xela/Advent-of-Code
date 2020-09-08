from functools import reduce


def getDimensions(dimensionsString):
    dimensions = tuple(map(int, dimensionsString.split('x')))

    return dimensions


def getOrder(dimensionsString):
    dimensions = getDimensions(dimensionsString)

    surfaceAreas = (dimensions[0]*dimensions[1], dimensions[1]*dimensions[2], dimensions[0]*dimensions[2])

    slack = min(surfaceAreas)

    totalSurfaceArea = (2 * surfaceAreas[0]) + (2 * surfaceAreas[1]) + (2 * surfaceAreas[2])

    return slack + totalSurfaceArea


paperOrders = list(map(getOrder, open('dimensionsFile.txt', 'r')))

print("Wrapping Paper Order =", reduce(lambda x, y: x+y, paperOrders, 0))



def getRibbonBow(dimensions) :
    return dimensions[0] * dimensions[1] * dimensions[2]


def getRibbonLength(dimensionsString):
    dimensions = getDimensions(dimensionsString)

    maxDimensionIndex = dimensions.index(max(dimensions))

    ribbonLength = 0
    for i in range(len(dimensions)) :
        if i != maxDimensionIndex :
            ribbonLength += 2 * dimensions[i]
    
    ribbonLength += getRibbonBow(dimensions)

    return ribbonLength


ribbons = list(map(getRibbonLength, open('dimensionsFile.txt', 'r')))

print("Total Ribbon Length =", reduce(lambda x, y: x+y,ribbons, 0))
