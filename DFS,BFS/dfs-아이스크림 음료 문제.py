#n,m공백 구분하여 입력 받음
n,m=map(int,input().split())

#2차원 리스트 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>= n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        #------------0에서 시작하면 결국 최소단위여도 1개가 result에 카운트 된다.
        graph[x][y]=1
        #--------------위 두 코드를 계속 반복한다. 한 방향으로 쭉 바꾸면서 진행
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        #--------------------------------------------
        return True #반환되는것은 True
    return False
result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)

#해설
#예를 들어
# 11100
# 10011
# 10010
# 10111
# 00100
# 이 배열로 문제를 해결한다고 가정한다.
# N = 0~5, M= 0~5 이다.
# 함수의 첫 줄은 x, y 즉 현재위치가 맵의 범위에서 벗어나는지 검사하는 코드이다.
# 2번째 if는 현재 공간이 0일경우 현재 위치를 1로 바꾼다. 
# 그리고 인접한 모든 공간에서 이와같은 검사를 진행한다. 
# 이렇게 모든 인접한 곳의 0을 1로 바꾼다. 
# 해당 문제의 DFS는 네 방향에서 한방향을 쭈~욱 훑어보고, 0->1로 바꾸는 작업을 수행한다.


    