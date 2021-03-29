def Up_to_Down():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))

    arr=sorted(arr,reverse=True4)

    for i in arr:
        print(i,end=' ')
Up_to_Down()
