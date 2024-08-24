from collections import deque
from collections import defaultdict


'''
V E
FOR EVERY EDGE
U V
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''
def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmpnode = queue.popleft()
        #TYPE UR CODE HERE
        for neighbour in graph[tmpnode]:
          if not visited[neighbour]:
            path.append(neighbour)
            queue.append(neighbour)
            visited[neighbour]=True
    return path

graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    #TYPE UR CODE HERE
    u,v=input().split()
    graph[u].append(v)
    graph[v].append(u)
start = '0'
path = []
visited = defaultdict(bool)
traversedpath = bfs(graph,start,visited,path)
print(traversedpath)
