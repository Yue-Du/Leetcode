max_distance_trip = None
max_distance = -1
pathMap = {}

import fileinput


class Path:
    def init(self, destination, length):
        self.destination = destination
        self.length = length


class PathCalculator:
    max_distance_trip = None
    max_distance = -1
    pathMap = {}

    # You may enter code here.

    def getResult(self):
        if self.max_distance_trip is None:
            return "NONE"
        return str(self.max_distance) + ":" + self.max_distance_trip

    def insertNewPath(self, city1, city2, distance):
        path1 = Path()
        path1.init(city2, distance)
        if city1 not in self.pathMap:
            self.pathMap[city1] = [path1]
        else:
            self.pathMap[city1].append(path1)

        path2 = Path()
        path2.init(city1, distance)
        if city2 not in self.pathMap:
            self.pathMap[city2] = [path2]
        else:
            self.pathMap[city2].append(path2)

    def doUpdateNewMaxTrip(self, city1, city2, city3, distance):
        trip = None
        if city1 < city3:
            trip = city1 + ":" + city2 + ":" + city3
        else:
            trip = city3 + ":" + city2 + ":" + city1
        if distance > self.max_distance:
            self.max_distance = distance
            self.max_distance_trip = trip
            return True
        if trip < self.max_distance_trip:
            self.max_distance_trip = trip
            return True
        return False

    def updateNewMaxTrip(self, city1, city2, distance):
        city1ConnectPathList = self.pathMap.get(city1)
        if city1ConnectPathList is not None:
            for path in city1ConnectPathList:
                if path.destination == city1 or path.destination == city2:
                    continue
                if self.max_distance <= (path.length + distance):
                    self.doUpdateNewMaxTrip(city2, city1, path.destination, path.length + distance)

        city2ConnectPathList = self.pathMap.get(city2)
        if city2ConnectPathList is None:
            return
        for path in city2ConnectPathList:
            if path.destination == city1 or path.destination == city2:
                continue
            if self.max_distance <= (path.length + distance):
                self.doUpdateNewMaxTrip(city1, city2, path.destination, path.length + distance)

    def process(self, line: str) -> str:
        if line is None or len(line) == 0:
            return self.getResult()
        inputArray = line.split(":")
        if len(inputArray) != 3 or inputArray[0] == inputArray[1]:
            return self.getResult()

        city1 = inputArray[0]
        city2 = inputArray[1]
        distance = int(inputArray[2])

        self.updateNewMaxTrip(city1, city2, distance)
        self.insertNewPath(city1, city2, distance)
        return self.getResult()
        # You must enter code here.


if __name__ == "__main__":
    path_calc = PathCalculator()
    for line in fileinput.input():
        cleaned_line = line.replace("\n", "")
        print(path_calc.process(cleaned_line))