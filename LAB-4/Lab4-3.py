W = [5,10,12,13,15,18]
target=30


def printList(list):

    for num in list:
        print(num , end=' ')
    print()


def Solve(A, n, sum, target, list):

        if sum == target:
            printList(list)
            return

        if n < 0:
            return
        Solve(A, n - 1, sum, target, list)
        list.append(A[n])
        Solve(A, n - 1, sum + A[n], target, list)
        list.pop()  # backtrack


print("The list of numbers is:")
print(W)
print("the target sum is:",target)
print("The elements for which the sum is",target)
Solve(W, len(W) - 1, 0, target, [])
