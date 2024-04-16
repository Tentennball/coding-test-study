N = int(input())
child = [[]*N for _ in range(N)]
leafs = 0
inputs = list(map(int, input().split()))

def dfs(n):
    global leafs
    if not child[n]: 
        leafs+=1
        return
    for i in range(len(child[n])):
        dfs(child[n][i])

for i in range(N):
    if(inputs[i] == -1):
       root = i 
       continue
    child[inputs[i]].append(i)
erase = int(input())

for i in range(N):
    if(erase in child[i]):
        child[i].remove(erase)
if(root!=erase):
    dfs(root)

print(leafs)

