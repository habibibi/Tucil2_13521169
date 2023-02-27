from Point import *

def sort(arrP,idxCMP):
    mergeSort(arrP,idxCMP,0,len(arrP)-1)

def mergeSort(arrP, idxCMP, l, r):
    if (l >= r):
        return
    mid = (l+r)//2
    mergeSort(arrP,idxCMP,l,mid)
    mergeSort(arrP,idxCMP,mid+1,r)
    b = []
    i = l
    j = mid+1
    while (i <= mid and j <= r):
        if (arrP[i].getXi(idxCMP) < arrP[j].getXi(idxCMP)):
            b.append(arrP[i])
            i += 1
        else:
            b.append(arrP[j])
            j += 1
    while (i <= mid):
        b.append(arrP[i])
        i += 1
    while (j <= r):
        b.append(arrP[j])
        j += 1
    for i in range(l,r+1):
        arrP[i] = b[i-l]
    return
