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
n,target=list(map(int,input().split()))
arr=list(map(int,input().split()))
result=binarySearch(arr,target,0,n-1)

if result==None:
    print("Element does not exist")
else:
    print(result+1)
#############################################################

arr=[1, 3, 5, 7, 9, 11, 13, 15, 17, 18]

def binarySearch_loop(arr,target,s,e):
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return None

