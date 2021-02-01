n, m = map(int, input().split())
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))
print(data)
  
def my_answer(data):
  result=0
  for i in range(n):
      data[i].sort()
      if(int(result)<int(data[i][0])):
        result=data[i][0]
  #반복문에서 정렬을 한다음 비교문을 통해 정답을 도출
  return result


def answer(data):
  result=0
  for i in range(n):
    min_value=min(data[i])
    result=max(result,min_value)
  return result
  #각 배열의 최솟값을 알면 되는 문제이다. 
  #min 함수로 최솟값만 찾고, max로 각 배열의 최솟값중 최댓값을 찾음.
print("my_answer->")
print(my_answer(data))
print("answer->")
print(answer(data))
#print(data[0][m-1])



