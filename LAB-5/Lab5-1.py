def fib(n):
    global count1
    count1+=1
    if n<=1:
        return n
    else:
        f= fib(n-1) + fib(n-2)
        return f

def DP_fib(n):
    global count2
    count2+=1
    mem=[0,1]
    while len(mem)<n+1:
        mem.append(0)
    if n<=1:
        return n
    else:
        if mem[n-1]==0:
            mem[n-1]=DP_fib(n-1)
        if mem[n-2]==0:
            mem[n-2]=DP_fib(n-2)
        mem[n]=mem[n-1]+mem[n-2]
        return mem[n]


def Bottom_UP_fib(n):
    if n<=1:
        return n
    a=0
    b=1
    c=a+b
    for i in range(2,n):
        a=b
        b=c
        c=a+b
    return c

count1=0
count2=0
x = int(input("Enter a number:"))

print("Brute force Approach:")
y=fib(x)
print("The",x,"th element of Fibonacci series is:",y)
print("Number of calls for brute force approach:",count1)



print("Dynamic Programming using Memoization:")
z=DP_fib(x)
print("The",x,"th element of Fibonacci series is:",z)
print("Number of calls for dynamic programming using memoization:",count2)

print("Bottom-Up Approach:")
k=Bottom_UP_fib(x)
print("The",x,"th element of Fibonacci series is:",k)