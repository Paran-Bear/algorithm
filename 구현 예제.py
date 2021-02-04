import random
import os
import numpy as np
import pprint
from time import sleep
def data_input(n,min,max):
  data=[]
  for i in range(n):
    data.append(random.randrange(min,max))
  return data
  
def my_answer_LRUD():
  # 입력은 난수로 대체
  # n=int(input())
  n=data_input(1,3,10)[0]
  print("입력 N=",n)
  x,y=0,0
  # plans=input().split()
  plans=[]
  data=[]
  for i in range(n):
    data.append(np.zeros(n))
  
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  mv=['L','R','U','D']
  for i in data_input(data_input(1,10,100)[0],0,3):
    plans.append(mv[i])
  print("이동경로 -> ",plans)
  sleep(1)
  os.system('clear')
  count=0
  for plan in plans:
    
    for i in range(len(mv)):
      if plan==mv[i]:
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>n-1 or ny>n-1 or nx<0 or ny<0:
          
          print(plan,"ignore")
          data[y][x]=1
          print(*data,sep='\n')
          data[y][x]=0
          print(plans[count:-1])
          sleep(0.5)
          os.system('clear')
          continue  
        else:
          
            
          print(plan,"move")
          x=nx
          y=ny
          data[y][x]=1
          print(*data,sep='\n')
          print(plans[count:-1])
          data[y][x]=0
          sleep(0.5)
          os.system('clear')
    count+=1

  print(x+1,y+1)
def my_answer_3InTime():
  count=0
  hour=int(input())
  for i in range(hour+1):
    for j in range(60):
      for k in range(60):
        if '3' in str(i)+str(j)+str(k):
          # print(str(i)+str(j)+str(k))
          # sleep(0.001)
          # os.system('clear')
          count+=1
  return count

  
# my_answer_LRUD()
print(my_answer_3InTime())








