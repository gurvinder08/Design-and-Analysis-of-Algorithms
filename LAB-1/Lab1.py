import time
import random


def BubbleSort(A):
    x=len(A)

    for i in range(0,x):
        for j in range(0,x-i-1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp



def InsertionSort(A):
    x=len(A)

    for j in range(1,x):
        key =A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key



def SelectionSort(A):
    x=len(A)
    for i in range(0,n-1):
        min=i
        for j in range(i+1, n):
            if A[j]<A[min]:
                min=j
        temp=A[min]
        A[min]=A[i]
        A[i]=temp



def MergeSort(A):
    x=len(A)
    if x>1:
        m=x//2
        L=A[:m]
        R=A[m:]
        MergeSort(L)
        MergeSort(R)

        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                A[k]=L[i]
                i=i+1
            else:
                A[k]=R[j]
                j=j+1
            k=k+1

        while i<len(L):
            A[k]=L[i]
            i=i+1
            k=k+1

        while j<len(R):
            A[k]=R[j]
            j=j+1
            k=k+1





def Partition(A,p,q):
    x=A[q]
    i=p-1
    for j in range(p,q):
        if A[j]<=x:
            i=i+1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
    t=A[q]
    A[q]=A[i+1]
    A[i+1]=t
    return i+1

def QuickSort(A,p,q):
    if len(A)==1:
        return A
    if p<q:
        r=Partition(A,p,q)
        QuickSort(A,p,r-1)
        QuickSort(A,r+1,q)




n = int(input("Enter range:"))
print("The number of elements is :", n)


A = random.sample(range(1,n+1),n)
print("BUBBLE SORT:")
print("The input array is",A,end=" ")
print("")
start=time.time()
BubbleSort(A)
end=time.time()
print("Sorted Array",A)
print("Runtime of the program is: ", end-start)

B = random.sample(range(1,n+1),n)
print("INSERTION SORT:")
print("The input array is",B, end=" ")
print("")
start1=time.time()
InsertionSort(B)
end1=time.time()
print("Sorted Array",B)
print("Runtime of the program is: ", end1-start1)

C = random.sample(range(1,n+1),n)
print("SELECTION SORT:")
print("The input array is",C, end=" ")
print("")
start2=time.time()
SelectionSort(C)
end2=time.time()
print("Sorted Array",C)
print("Runtime of the program is: ", end2-start2)


D = random.sample(range(1,n+1),n)
print("MERGE SORT:")
print("The input array is",D, end=" ")
print("")
start3=time.time()
MergeSort(D)
end3=time.time()
print("Sorted Array",D)
print("Runtime of the program is: ", end3-start3)

E=random.sample(range(1,n+1),n)
print("QUICK SORT:")
print("The input array is",E, end=" ")
print("")
start4=time.time()
QuickSort(E,0,len(E)-1)
end4=time.time()
print("Sorted Array",E)
print("Runtime of the program is: ", end4-start4)





