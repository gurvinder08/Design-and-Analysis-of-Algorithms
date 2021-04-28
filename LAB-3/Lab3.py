import time
import random
import psutil
import os

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


# Finding the lowest common ancestor
def LCA(root, n1, n2):
    if root is None:
        return None
    if root.data > n1 and root.data > n2:
        return LCA(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return LCA(root.right, n1, n2)
    return root.data

# Finding the maximum depth
def maxDepth(root):
    if root is None:
        return 0
    else:
        ld = maxDepth(root.left)
        rd = maxDepth(root.right)

        if ld > rd:
            return ld+1
        else:
            return rd+1

# In-order traversal of the tree
def InOrder(root):
    if root==None:
        return
    InOrder(root.left)
    print(root.data, end=" ")
    InOrder(root.right)

# Finding the minimum depth
def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minDepth(root.right) + 1
    if root.right is None:
        return minDepth(root.left) + 1
    return min(minDepth(root.left), minDepth(root.right)) + 1



def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[i] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        t = A[i]
        A[i] = A[largest]
        A[largest] = t
        heapify(A, n, largest)

# Heap Sort
def heapSort(A):
   n = len(A)

   for i in range(n, -1, -1):
      heapify(A, n, i)

   for i in range(n-1, 0, -1):
       temp=A[i]
       A[i]=A[0]
       A[0]=temp
       heapify(A, i, 0)

# For calculating the memory
def Memory():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

file=open('numbers.txt','r')
content = file.readlines()
array=[]
for line in content:
    array.append(line.rstrip())
print(array)

n1=Node(None)
root=n1
for i in array:
    root.insert(i)

print("The In-order Walk of the Tree:")
InOrder(root)
print()

max=maxDepth(root)
min=minDepth(root)
print("The max depth of the tree is:",max)
print("The min depth of the tree is:",min)

v1 = input("Enter n1:")
v2 = input("Enter n2:")
if v1 or v2 not in array:
    print("Not present in array!!")
    v1 = input("Enter n1:")
    v2 = input("Enter n2:")
d=LCA(root,v1,v2)
print("The lowest common ancestor of ",v1," and ", v2, " is: ",d)


n=int(input("Enter range:"))
print("HEAP SORT:")
A = random.sample(range(1,n+1),n)
print("The number of elements:", n)
print("The input array is",A,end=" ")
print("")
start=time.time()
heapSort(A)
m=Memory()
end=time.time()
print("Sorted Array",A)
print("Runtime of the program is: ", end-start)
print("The memory taken for ",n, " input numbers: ", m)

