import math
import random

class Point:
    LIMIT = 1e5
    eucDistCnt = 0
    def __init__(self, isRandom = False, dim = 3, arr = [0,0,0] ):
        self.__r = []
        if (isRandom):
            self.__d = dim
            for i in range(dim):
                self.__r.append(random.uniform(-Point.LIMIT,Point.LIMIT))
        else:
            self.__d = len(arr)
            for i in range(len(arr)):
                self.__r.append(arr[i])

    def getDim(self):
        return self.__d

    def getXi(self,i):
        return self.__r[i]

    def eucDist(self,p):
        ans = 0
        for i in range(min(self.__d,p.__d)):
            ans += (self.__r[i]-p.__r[i])**2
        Point.eucDistCnt += 1
        return math.sqrt(ans)

    @staticmethod
    def resetEucDistCnt():
        Point.eucDistCnt = 0

    def __str__(self):
        l = []
        for i in range(self.__d):
            l.append(str(self.__r[i]))
        return '('+','.join(l)+')'
    
    def __repr__(self):
        return str(self)

