from SpaceOfPoints import *
from Point import *
import time
import matplotlib.pyplot as plt
import numpy as np
import os

print("Pilihan metode membangkitkan titik")
print("1. Random")
print("2. Membaca file")

while (True):
    pil = str(input("Masukkan pilihan anda: "))
    if (pil == '1'):
        n = int(input("Masukkan banyak poin (n >= 2) : "))
        while (n < 2):
            print("Masukkan nilai yang valid!")
            n = int(input("Masukkan banyak poin (n) : "))
        d = int(input("Masukkan banyak dimensi (d >= 1) : "))
        while (d < 1):
            print("Masukkan nilai yang valid!")
            d = int(input("Masukkan banyak dimensi (d >= 1) : "))
        A = SpaceOfPoints(d,n)
        break
    elif (pil == '2'):
        print("Format file input adalah sebagai berikut : ")
        print("n d")
        print("x0,0 x0,1 x0,2 ...")
        print("x1,0 x1,1 x1,2 ...")
        print("dengan n banyak poin, d banyak dimensi, dan xi,j koordinat dari axis ke-j dari titik ke-i")
        fileDir = str(input("Masukkan lokasi file (absolute) : "))
        A = SpaceOfPoints(fileDir=fileDir)
        break
    print("Masukan tidak valid!")
print()

st = time.time()
dist = A.bruteClosestPair()
end = time.time()
print("Hasil bruteforce = ", dist)
print("Banyak eucDist dipanggil = ", Point.eucDistCnt)
print("Runtime = ", end-st)
print()

Point.resetEucDistCnt()
st = time.time()
dist, pA, pB = A.dncClosestPair()
end = time.time()
print("Hasil DnC = ", dist)
print("Banyak eucDist dipanggil = ", Point.eucDistCnt)
print("Runtime = ", end-st)
print()

if (A.getD() == 3):
    pil = input("Apakah Anda ingin melihat visualisasi titik? (y/n)\n")
    if (pil == 'y'):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        for i in range(A.getN()):
            p = A.getPoints()[i]
            if (p != pA and p != pB):
                col = 'blue'
            else:
                col = 'red'
            ax.scatter(p.getXi(0),p.getXi(1),p.getXi(2),c=col) 
        x = np.linspace(pA.getXi(0),pB.getXi(0))
        y = np.linspace(pA.getXi(1),pB.getXi(1))
        z = np.linspace(pA.getXi(2),pB.getXi(2))
        plt.plot(x,y,z,c='red')
        plt.show()

print("Program selesai...")