import queue

N, M = map(int, input().split())
maze = [[0]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0
for i in range(N):
    input_str = input()
    inputs = [int(char) for char in input_str]
    for j in range(M):
        maze[i][j] = inputs[j]

def bfs():
    queues = queue.Queue()
    queues.put(0)
    queues.put(0)
    dist[0][0] = 1
    while not queues.empty():
        x = queues.get()
        y = queues.get()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if(nx<0 or ny<0 or nx>=N or ny>=M): continue
            if(dist[nx][ny]!=0): continue
            if(maze[nx][ny]==0): continue
            dist[nx][ny]= dist[x][y]+1
            queues.put(nx)
            queues.put(ny)
bfs()
print(dist[N-1][M-1])