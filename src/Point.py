import math
import random

class Point:
    LIMIT = 1e5
    eucDistCnt = 0
    def __init__(self, dim = 3, arr = None):
        # constuctor berupa init(dim) atau init(arr)
        self.__r = []
        if (arr is not None):
            self.__d = len(arr)
            for i in range(len(arr)):
                self.__r.append(arr[i])
        else:
            self.__d = dim
            for i in range(dim):
                self.__r.append(random.uniform(-Point.LIMIT,Point.LIMIT))


    def getDim(self):
        return self.__d

    def getXi(self,i):
        if (i >= self.__d):
            return 0
        else:
            return self.__r[i]
        
    def getFullCoor(self):
        return self.__r

    def eucDist(self,p):
        # menghitung jarak euclidean dengan titik p
        ans = 0
        for i in range(min(self.__d,p.__d)):
            ans += (self.__r[i]-p.__r[i])**2
        Point.eucDistCnt += 1
        return math.sqrt(ans)

    @staticmethod
    def resetEucDistCnt():
        # mereset perhitungan pemanggilan eucDist
        Point.eucDistCnt = 0

    def __str__(self):
        l = []
        for i in range(self.__d):
            l.append("{:.2f}".format(self.__r[i]))
        return '['+', '.join(l)+']'
    
    def __repr__(self):
        return str(self)

