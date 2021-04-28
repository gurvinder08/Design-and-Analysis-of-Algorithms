import sys
import time
import random


def RPartition(A,p,q):
    x = A[q]
    i = p - 1
    for j in range(p, q):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    t = A[q]
    A[q] = A[i + 1]
    A[i + 1] = t
    return i + 1


# Recursive Quick Sort
def RQuickSort(A,p,q):
    if len(A)==1:
        return A
    if p<q:
        r=RPartition(A,p,q)
        RQuickSort(A,p,r-1)
        RQuickSort(A,r+1,q)


# Recursive Merge Sort
def RMergeSort(A):
    x = len(A)
    if x > 1:
        m = x // 2
        L = A[:m]
        R = A[m:]
        RMergeSort(L)
        RMergeSort(R)

        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(L):
            A[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            A[k] = R[j]
            j = j + 1
            k = k + 1


# Iterative Quick Sort
def IQuickSort(A,p,q):
    size=q-p+1
    stack = [0]*(size)
    top=-1

    top=top+1
    stack[top]=p
    top=top+1
    stack[top]=q

    while top>=0:
        q = stack[top]
        top = top - 1
        p = stack[top]
        top = top - 1
        r=RPartition(A,p,q)
        if r - 1 > p:
            top = top + 1
            stack[top] = p
            top = top + 1
            stack[top] = r - 1
        if r+1 < q:
                top = top + 1
                stack[top] = r + 1
                top = top + 1
                stack[top] = q


# Iterative Merge Sort
def IMergeSort(A):
    size = 1
    while size < len(A) - 1:
        left = 0
        while left < len(A) - 1:
            mid = min((left + size - 1), (len(A) - 1))
            right = ((2 * size + left - 1, len(A) - 1)[2 * size + left - 1 > len(A) - 1])
            merge(A, left, mid, right)
            left = left + size * 2
        size = 2 * size



def merge(a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = a[l + i]
        for i in range(0, n2):
            R[i] = a[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] > R[j]:
                a[k] = R[j]
                j += 1
            else:
                a[k] = L[i]
                i += 1
            k = k+ 1

        while i < n1:
            a[k] = L[i]
            i = i+ 1
            k = k+ 1

        while j < n2:
            a[k] = R[j]
            j = j+ 1
            k = k+ 1


def Memory():
    import psutil
    import os
    process=psutil.Process(os.getpid())
    mem = process.memory_info()[0]/ float(2**20)
    return mem


n= int(sys.argv[1])
print("The number of elements:",n)


A = random.sample(range(1,n+1),n)
print("RECURSIVE QUICK SORT:")
print("The input array is",A,end=" ")
print("")
start=time.time()
RQuickSort(A,0,len(A)-1)
end=time.time()
print("Sorted Array",A)
print("Runtime of the program is: ", end-start)
#print("Memory taken by recursive quick sort:",m1)


B=random.sample(range(1,n+1),n)
print("RECURSIVE MERGE SORT:")
print("The input array is",B, end=" ")
print("")
start1=time.time()
RMergeSort(B)
end1=time.time()
print("Sorted Array",B)
print("Runtime of the program is: ", end1-start1)
#print("Memory taken by recursive Merge sort:",m2)


C= random.sample(range(1,n+1),n)
print("ITERATIVE QUICK SORT:")
print("The input array is",C,end=" ")
print("")
start2=time.time()
IQuickSort(C,0,len(C)-1)
end2=time.time()
print("Sorted Array",C)
print("Runtime of the program is: ", end2-start2)
#print("Memory taken by iterative quick sort:",m3)


D=random.sample(range(1,n+1),n)
print("ITERATIVE MERGE SORT:")
print("The input array is",D, end=" ")
print("")
start3=time.time()
IMergeSort(D)
end3=time.time()
print("Sorted Array",D)
print("Runtime of the program is: ", end3-start3)
#print("Memory taken by iterative merge sort:",m4)
