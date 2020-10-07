CELL_INIT_VALUE = -1
CELL_SEARCHED = 0   
MAX_CELL_SIZE = 26 + 1
CELLS = []

for i in range(MAX_CELL_SIZE):
    CELLS.append([CELL_INIT_VALUE] * MAX_CELL_SIZE)


def letterToNumber(letter):
    return ord(letter) - 64


def getCoordination(cordinationString):
    if len(cordinationString) == 2:
        return [int(cordinationString[0]), letterToNumber(cordinationString[1])]
    return [int(cordinationString[0:2]), letterToNumber(cordinationString[2])]


# artifact cells,artifact id start from 1
def markArtifactCells(N, rtifacts):
    artifacts = rtifacts.split(",")
    artifactNumber = 1
    for artifact in artifacts:
        artifact = artifact.split(" ")
        lefTop = getCoordination(artifact[0])
        rightBottom = getCoordination(artifact[1])
        for i in range(lefTop[0], rightBottom[0] + 1):
            for j in range(lefTop[1], rightBottom[1] + 1):
                CELLS[i][j] = artifactNumber
        artifactNumber += 1


# mark cells to initial value after searched
def searchArtifact(searched):
    coordinationList = searched.split(" ")
    for coordination in coordinationList:
        coordination = getCoordination(coordination)
        CELLS[coordination[0]][coordination[1]] = CELL_SEARCHED


# 1: partialSearched, 2: allSearched, 3: nothing searched
def isReconstructed(artifactCoordination):
    coordination = artifactCoordination.split(" ")
    somePieceSearched = False
    somePieceMissed = False
    coordination[0] = getCoordination(coordination[0])
    coordination[1] = getCoordination(coordination[1])
    for i in range(coordination[0][0], coordination[1][0] + 1):
        for j in range(coordination[0][1], coordination[1][1] + 1):
            if (CELLS[i][j] == CELL_SEARCHED):
                somePieceSearched = True
            else:
                somePieceMissed = True
    if somePieceMissed and somePieceSearched:
        return 1
    if somePieceSearched:
        return 2
    return 3


def solution(N, artifacts, searched):
    # write your code in Python
    if artifacts == "" or searched == "":
        return [0, 0]
    markArtifactCells(N, artifacts)
    searchArtifact(searched)
    completed = 0
    notCompleted = 0
    artifactList = artifacts.split(",")
    for artifact in artifactList:
        isRecon = isReconstructed(artifact)
        if isRecon == 2:
            completed = completed + 1
        elif isRecon == 1:
            notCompleted = notCompleted + 1
    return [completed, notCompleted]


# artifacts = "1B 2C,2D 4D"
# searched = "2B 2D 3D 4D 4A"
# print(solution(4, artifacts, searched))

artifacts = "26Z 26Z"
searched = "26B"
print(solution(3, artifacts, searched))
markArtifactCells(4, "1B 2C,2D 4D")