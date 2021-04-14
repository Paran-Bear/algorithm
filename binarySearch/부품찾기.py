n=int(input())
nArr=list(map(int,input().split()))
m=int(input())
mArr=list(map(int,input().split()))

nArr.sort()

def binarySearch(arr,target,s,e):
    if s>e:
        return None
    mid=(s+e)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binarySearch(arr,target,s,mid-1)
    else:
        return binarySearch(arr,target,mid+1,e)

for i in range(len(mArr)):
    if binarySearch(nArr,mArr[i],0,len(nArr)-1)==None:
        print("No",end=' ')
    else:
        print("Yes",end=' ')
        



    