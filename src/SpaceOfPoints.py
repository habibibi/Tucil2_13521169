import PointSorter
from Point import Point
import time
import matplotlib.pyplot as plt

class SpaceOfPoints:
    INF = 1e9
    def __init__(self,n,d = 3, points = None, sortedPoints = None):
        if (points is None):
            self.__points = [None for i in range(n)]
            for i in range(n):
                self.__points[i] = Point(True,d)
            self.__n = n
            self.__d = d
            self.__sortedPoints = [None for i in range(d)]
            st = time.time()
            for i in range(d):
                self.__sortedPoints[i] = self.__points.copy()
                PointSorter.sort(self.__sortedPoints[i],i)
            end = time.time()
            self.initTime = end-st
        else:
            self.__points = points
            self.__n = n
            self.__d = d
            self.__sortedPoints = sortedPoints
            self.initTime = 0.0

    def isEmpty(self):
        return self.__n == 0

    def getPoints(self):
        return self.__points

    def getN(self):
        return self.__n
    
    def filterPointsByIdx(self,l,r,di):
        fPoints = self.__sortedPoints[di][l:r+1]
        fSortedPoints = [[] for i in range(self.__d)]
        # print(fPoints)
        # print("-------------")
        minX = self.__sortedPoints[di][l].getXi(di)
        maxX = self.__sortedPoints[di][r].getXi(di)
        for i in range(self.__d):
            for j in range(self.__n):
                if minX <= self.__sortedPoints[i][j].getXi(di) <= maxX:
                    fSortedPoints[i].append(self.__sortedPoints[i][j])
                    # print(self.__sortedPoints[i][j])
            if (len(fPoints) != len(fSortedPoints[i])):
                print(fPoints)
                print(fSortedPoints[i])
                print(len(fPoints),len(fSortedPoints[i]))        
                assert len(fPoints) == len(fSortedPoints[i])
            
        return SpaceOfPoints(len(fPoints),self.__d,fPoints,fSortedPoints)

    def filterPointsByMinMax(self,minX,maxX,di):
        fPoints = []
        # print(self.__points)
        for i in range(self.__n):
            if minX <= self.__points[i].getXi(di) <= maxX:
                # print(self.__points[i])
                fPoints.append(self.__points[i])
        # print("----------------")
        fSortedPoints = [[] for i in range(self.__d)]
        for i in range(self.__d):
            for j in range(self.__n):
                if minX <= self.__sortedPoints[i][j].getXi(di) <= maxX:
                    # print(self.__sortedPoints[i][j])
                    fSortedPoints[i].append(self.__sortedPoints[i][j])
                
            assert len(fPoints) == len(fSortedPoints[i])
        
        return SpaceOfPoints(len(fPoints),self.__d,fPoints,fSortedPoints)

    def dnqClosestPair(self):
        if (self.__n == 1) :
            return SpaceOfPoints.INF
        elif (self.__n == 2):
            return self.__sortedPoints[0][0].eucDist(self.__sortedPoints[0][1])
        else:
            mid = (self.__n-1)//2
            qL = self.filterPointsByIdx(0,mid,0)
            qR = self.filterPointsByIdx(mid+1,self.__n-1,0)
            dL = qL.dnqClosestPair()
            dR = qR.dnqClosestPair()
            #print(qL)
            #print(qR)
            minDist = min(dL,dR)
            #print(minDist)
            xMid = (self.__sortedPoints[0][0].getXi(0) + self.__sortedPoints[0][self.__n-1].getXi(0))/2
            #print("x mid = ", xMid)
            qMid = self.filterPointsByMinMax(xMid-minDist,xMid+minDist,0)
            #print("qmid = ",qMid)
            dMid = qMid.__findClosestSparse(0,minDist)
            return min(minDist,dMid)

    def __findClosestSparse(self,curD,minRange):
        if (self.isEmpty()) :
            return SpaceOfPoints.INF
        elif (curD == self.__d-1):
            minDist = SpaceOfPoints.INF
            for i in range(self.__n):
                j = i+1
                now = self.__sortedPoints[curD][i]
                while (j < self.__n and now.getXi(curD)-self.__sortedPoints[curD][j].getXi(curD) < minRange):
                    minDist = min(minDist,now.eucDist(self.__sortedPoints[curD][j]))
                    j += 1
            return minDist
        else:
            leftX = self.__sortedPoints[curD][0].getXi(curD)
            rightX = self.__sortedPoints[curD][self.__n-1].getXi(curD)
            if (rightX-leftX <= 2*minRange):
                return self.__findClosestSparse(curD+1,minRange)
            else:
                mid = (self.__n-1)//2
                qL = self.filterPointsByIdx(0,mid,curD)
                qR = self.filterPointsByIdx(mid+1,self.__n-1,curD)
                dL = qL.__findClosestSparse(curD,minRange)
                dR = qR.__findClosestSparse(curD,minRange)
                minDist = min(dL,dR)
                xMid = (self.__sortedPoints[curD][0].getXi(0) + self.__sortedPoints[curD][self.__n-1].getXi(0))/2
                qMid = self.filterPointsByMinMax(xMid-minRange,xMid+minRange,curD)
                dMid = qMid.__findClosestSparse(curD,minRange)
                return min(minDist,dMid)
            
    def bruteClosestPair(self):
        minDist = SpaceOfPoints.INF
        for i in range(self.__n-1):
            for j in range(i+1,self.__n):
                minDist = min(minDist,self.__points[i].eucDist(self.__points[j]))
        return minDist
    
    def __str__(self):
        return str(self.__points)
    
    def __repr__(self):
        return str(self)


hehe = SpaceOfPoints(20,3)
st = time.time()
print("brute = ",hehe.bruteClosestPair())
end = time.time()
print(end-st)
print(Point.eucDistCnt)

Point.resetEucDistCnt()

st = time.time()
print("hasil = ",hehe.dnqClosestPair())
end = time.time()
print(end-st+hehe.initTime)
print(Point.eucDistCnt)

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
for i in range(hehe.getN()):
    p = hehe.getPoints()[i]
    ax.scatter(p.getXi(0),p.getXi(1),p.getXi(2),c='blue') # plot the point (2,3,4) on the figure

plt.show()