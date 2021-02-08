import pprint
n,m=map(int,input().split())
# 첫째줄 입력
y,x,d=map(int,input().split())
# 둘째줄 입력
filed=[]

for i in range(n):
  filed.append(input().split())
# 셋째줄 필드 입력


plans=[(-1,0),(0,-1),(1,0),(0,1)]
# 북쪽을 본다는 기준하에 왼쪽을 보는 방향이 요소로 구성된 배열

back=[(1,0),(0,1),(-1,0),(0,-1)]
# 북쪽을 본다는 기준하에 뒤로 이동하는 방향이 요소로 구성된 배열

t=0 #4방향을 보고 카운트.

count=0

filed[y][x]='S' #시작지점은 S로 바꿈.
print(*filed,sep='\n')


# 이동 가능 체크
while(True):
  for i in range(4):#확인은 4방향이므로 반복은 4번이면 됨.
    if d>3:#북 동 님 서 방향을 로테이션으로 확인.
      d=0 #ex) d 입력이 2-> 2 3 0 1
    if filed[y+plans[d][0]][x+plans[d][1]] == '0':
      #이동할 방향의 공간 상태 확인
      filed[y+plans[d][0]][x+plans[d][1]]='E' 
      # 이동이 가능하면, 상태 E로 바꿈.
      y=y+plans[d][0]
      x=x+plans[d][1]
      #캐릭터의 위치 업데이트.
      count+=1
      d+=1
      # 바라보는 방향 업데이트
      t=0    
      
      break
    else:#이동이 불가능할 경우.
      t+=1#한 방향 체크완료 (MAX(t)=4)
      d+=1#다음 방향을 바라보도록 업데이트
      
  if t==4:#4방향 모두 바라보았을 경우
    if filed[y+back[d][0]][x+back[d][1]]=='1':
      # 뒤로 이동할 경우 그곳이 바다인 경우
      break#프로그램 종료
    else:#바다가 아닌경우.
      y=y+back[d][0]
      x=x+back[d][1]
      t=0
      # 현재 캐릭터의 위치를 뒤로 이동시킴. 방향은 그대로. 
      
count=0
for i in range(n):
  for j in range(m):
    if filed[i][j] == 'E' or filed[i][j] == 'S':
      count+=1
    # 필드를 확인하고, 방문했던 필드가 몇군데인지 확인.
    
print('count',count)
print(*filed,sep='\n')
