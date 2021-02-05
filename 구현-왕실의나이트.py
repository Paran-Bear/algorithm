input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1

# a~h를 아스키코드로 바꾼후 int로 바꾸게되면 97~105가 됨.
# a~h를 1~8로 표현하기 위해서는
# 입력된 좌표(문자a~h)의 [0]인덱스에서
# 가장 첫 문자열 a를 int로 빼주면?
# ex) c2 -> c -> 99 에서 a인 97 을 뺀다.
# 2가 나옴.
# 문제서 좌표는 1~8로 표현됨을 명시하였다.
# 그러므로 +1을 해줌. 리스트같이 0~7로 표현되면 굳이 +1안해도 됨.


steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
  next_row=row+step[0]
  next_column=column+step[1]

  if next_row>=1 and next_row<=8 and next_column >=1 and next_column <=8:
    result+=1
print(result)

