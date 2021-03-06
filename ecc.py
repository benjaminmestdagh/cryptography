import euclidextended

class EccCalculator:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def calculateLambda(self, pointP, pointQ):
        if(pointP.x == pointQ.x and pointP.y == pointQ.y):
            firstPart = (3 * pointP.x**2 + self.a)
            secondPart = (2 * pointP.y)
        else:
            firstPart = (pointQ.y - pointP.y)
            secondPart = (pointQ.x - pointP.x)

        euclidResult = euclidextended.calculate(secondPart, self.p)
        inverse = euclidResult.x % self.p

        return (firstPart * inverse) % self.p

    def calculateR(self, pointP, pointQ):
        if(pointP.x == pointQ.x and pointP.y != pointQ.y):
            return Point(0,0)
        elif(pointQ.x == 0 and pointQ.y == 0):
            return pointP
        else:
            l = self.calculateLambda(pointP, pointQ)
            xr = (l**2 - pointP.x - pointQ.x) % self.p
            yr = (l * (pointP.x - xr) - pointP.y) % self.p

            return Point(xr, yr)

    def calculateG(self, n, x, y):
        self.checkPointInCurve(x,y)
        pointP = Point(x, y)
        pointQ = pointP
        results = []

        for i in range(1, n):
            pointR = self.calculateR(pointP, pointQ)
            result = '{}G: ({},{})'.format(i + 1, pointR.x, pointR.y)
            results.append(result)
            pointQ = pointR

        return results

    def calculateAllPoints(self):
        results = []
        yValues = []

        for i in range(self.p):
            yValues.append((i**2) % self.p)

        for i in range(self.p):
            y2 = (i**3 + self.a*i + self.b) % self.p
            for j in range(len(yValues)): 
                if yValues[j] == y2:
                    results.append(Point(i,j))

        return results

    def checkPointInCurve(self, x, y):
        for p in self.calculateAllPoints():
            if(p.x == x and p.y == y):
                return True

        raise ValueError('The point you entered is not in the curve!') 

class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

if __name__ == "__main__":
    print('You cannot run this module')
