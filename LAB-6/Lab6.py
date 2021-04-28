import collections

def BFS(s, adj):
    visited=[]
    queue=[]
    visited.append(s)
    queue.append(s)
    while queue:
        s=queue.pop(0)
        print(s, end=" ")
        for v in adj[s]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

    print()
    if collections.Counter(visited)==collections.Counter(adj.keys()):
        print("The graph is strongly connected.")
    else:
        print("The graph is not strongly connected.")

def DFS(s,adj,visited):
    global time
    global pre
    global post

    if s not in visited:
        print(s, end=" ")
        pre.append(time)
        time += 1
        visited.append(s)
        for v in adj[s]:
            DFS(v,adj,visited)
        post.append(time)
        time+=1


time=1
pre=[]
post=[]
v=[]
#Adjacency List
adj={1:[2,3],2:[1,4],3:[1,4,5],4:[2,3],5:[3,6],6:[5]}

print("Breadth First Search:")
BFS(1,adj)

print("Depth First Search:")
DFS(1,adj,v)
print()

print("Pre visited times:")
print(pre)
print("Post visited times:")
print(post)

