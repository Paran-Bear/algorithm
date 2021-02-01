print("start")
n, m, k = map(int, input().split())
#n,m,k의 값이 맵에 공백으로 구분되어 저장

data = list(map(int, input().split()))
#n의 배열값이 맵으로 저장됨. 공백으로 구분
data.sort()
#배열의 값을 오름차순으로 정렬.
first = data[n - 1]
#이미 정렬된 데이터의 마지막 값(큰수)
second = data[n - 2]
#뒤에서 두번쨰 값(두번째로 큰수)


def my_answer(m, k):
    count = 0
    result = 0
    while (True):
        for j in range(k):
            if (count != m):
                result += first
                count += 1
            else:
                break
        if (count != m):
            result += second
            count += 1
        else:
            break
    return result
#나의 답은 단순히 과정만 생각하여 도출한 코드

def answer(m,k):
  count=int(m/(k+1))*k
  count+=m%(k+1)

  result=0
  result+=(count)*first
  result+=(m-count)*second
  return result
#책에서 제시한 답은 반복되는 수열을 보고,
#반복되는 수열을 구하고 나머지를 따로 계산함.
#시간 복잡도면에서 더 이득이 됨.


print("my answer")
print(answer(m,k))
print("answer")
print(answer(m, k))

