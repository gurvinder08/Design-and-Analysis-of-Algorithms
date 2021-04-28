def LCS(x,y,m,n):
    L = [[[] for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                L[i - 1][j - 1].append(x[i - 1])
                L[i][j] = L[i - 1][j - 1].copy()
            else:
                temp = max(L[i][j - 1], L[i - 1][j], key=len)
                L[i][j] = temp.copy()
    return L[m][n]

A=input("Enter String 1:")
B=input("Enter String 2:")
dp=LCS(A,B,len(A),len(B))
print("The longest common sub-sequence is:",''.join(dp))
