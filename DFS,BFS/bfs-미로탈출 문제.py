from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#해당 교제의 저자는 배열에서의 이동을 dx,dy 배열을 이용한다.
#x+=dx[0], y+=dy[0] 이면, 좌로 이동함을 의미한다.
#이용할때 0=L, 1=R, 2=D, 3=U 으로 정의하여 사용하여도 좋을 듯 하다.

dx=[-1,1,0,0]
dy=[0,0,-1,1]
L=0
R=1
D=2
U=3

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:#큐를 사용한다는 뜻->큐에서 꺼낸다
        x,y=queue.popleft()#왼쪽에서 POP한다.(꺼내고 삭제)
        for i in range(4):#0~3(L,R,D,U)
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>= n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))
