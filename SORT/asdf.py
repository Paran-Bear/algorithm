arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print(arr)
arr=[7,5,9,0,3,1,6,2,4,8]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    tail=arr[1:]
    left_side=[x for x in tail if x <=pivot]
    right_side=[x for x in tail if x > pivot]
    
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)
print(quick_sort(arr))
arr=[7,5,9,0,3,1,6,2,4,8]
def quick_sort(arr,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and arr[left]<=arr[pivot]:
            left+=1
        while right> start and arr[right]>=arr[pivot]:
            right-=1
        if left>right:
            arr[right],arr[pivot]=arr[pivot],arr[right]
        else:
            arr[left],arr[right]=arr[right],arr[left]
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)
quick_sort(arr,0,len(arr)-1)
print(arr)
arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i] #Swap
print(arr)
 
