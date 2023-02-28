import PointSorter
from Point import Point


class SpaceOfPoints:
    INF = 1e9
    def __init__(self,d = 3, n = 10, points = None, arrPoints = None, fileDir = None):
        # konstructor berupa init(d,n), init(points), init(arrPoints), init(fileDir)
        if (fileDir is not None):
            with open(fileDir) as f:
                self.__n, self.__d = [int(x) for x in next(f).split()]
                self.__points = []
                for line in f:
                    self.__points.append(Point(arr = [int(x) for x in line.split()]))
        elif (arrPoints is not None):
            self.__points = [Point(arr = list(arrPoints[i])) for i in range(len(arrPoints))]
            self.__n = len(arrPoints)
            self.__d = d
        elif (points is not None):
            self.__points = points
            self.__n = len(points)
            self.__d = d
        else :
            self.__points = [None for i in range(n)]
            for i in range(n):
                self.__points[i] = Point(d)
            self.__n = n
            self.__d = d
            
    def isEmpty(self):
        return self.__n == 0

    def getPoints(self):
        return self.__points

    def getN(self):
        return self.__n
    
    def getD(self):
        return self.__d
    
    def getFilteredPointsByIdx(self,l,r):
        # mengembalikan himpunan titik yang dibagi berdasarkan indeks
        fPoints = self.__points[l:r+1]
        return SpaceOfPoints(len(fPoints),self.__d,fPoints)

    def getFilteredPointsByMinMax(self,minX,maxX,di):
        # mengembalikan himpunan titik yang dibagi berdasarkan nilai aksis ke-di
        fPoints = []
        for i in range(self.__n):
            if minX <= self.__points[i].getXi(di) <= maxX:
                fPoints.append(self.__points[i])
        return SpaceOfPoints(self.__d, points = fPoints)

    def dncShortestPair(self):
        # set up solusi divide and conquer
        # melakukan presort sumbu pertama
        sortedPoint = self.__points.copy()
        PointSorter.sort(sortedPoint,0)
        return SpaceOfPoints(self.__d,points=sortedPoint).__dncShortestPairRec()

    def __dncShortestPairRec(self):
        # solusi divide and conquer utama
        if (self.__n == 1) :
            return SpaceOfPoints.INF, None, None
        elif (self.__n == 2):
            return self.__points[0].eucDist(self.__points[1]), self.__points[0], self.__points[1]
        else:
            mid = (self.__n-1)//2
            qL = self.getFilteredPointsByIdx(0,mid)
            qR = self.getFilteredPointsByIdx(mid+1,self.__n-1)
            dL, pLA, pLB = qL.__dncShortestPairRec()
            dR, pRA, pRB = qR.__dncShortestPairRec()
            if (dL < dR):
                pA = pLA
                pB = pLB
                minDist = dL
            else:
                pA = pRA
                pB = pRB
                minDist = dR
            xMid = self.__points[mid].getXi(0)
            qMid = self.getFilteredPointsByMinMax(xMid-minDist,xMid+minDist,0)
            dMid, pMidA, pMidB = qMid.__findClosestSparse(minDist)
            if (dMid < minDist):
                pA = pMidA
                pB = pMidB
                minDist = dMid            
            return minDist, pA, pB

    def __findClosestSparse(self,minRange):
        # mencari jarak terdekat pada kasus titik yang jaraknya <= minRange dari L
        if (self.isEmpty()) :
            return SpaceOfPoints.INF
        else:
            minDist = SpaceOfPoints.INF
            pA = None
            pB = None
            sortedPoints = self.__points.copy()
            PointSorter.sort(sortedPoints,self.__d-1)
            for i in range(self.__n):
                j = i+1
                now = sortedPoints[i]
                while (j < self.__n and sortedPoints[j].getXi(self.__d-1)-now.getXi(self.__d-1) < minRange):
                    dist = now.eucDist(sortedPoints[j])
                    if (dist < minDist):
                        minDist = dist
                        pA = now
                        pB = sortedPoints[j]
                    j += 1
            return minDist, pA, pB
            
    def bruteShortestPair(self):
        # solusi bruteforce
        minDist = SpaceOfPoints.INF
        pA = None
        pB = None
        for i in range(self.__n-1):
            for j in range(i+1,self.__n):
                dist = self.__points[i].eucDist(self.__points[j])
                if (dist < minDist):
                    minDist = dist
                    pA = self.__points[i]
                    pB = self.__points[j]
        return minDist, pA, pB
    
    def printToFile(self,fileDir):
        f = open(fileDir,'w')
        print(self.__n,self.__d,file=f)
        for i in range(self.__n):
            for j in range(self.__d):
                print(self.__points[i].getXi(j),end=' ',file=f)
            print(file=f)


    def __str__(self):
        return str(self.__points)
    
    def __repr__(self):
        return str(self)
