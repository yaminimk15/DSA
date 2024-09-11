def countsort(arr,exp):
    count=[0]*10
    result=[0]*len(arr)
    for i in range(0,len(arr)):
        index=int((arr[i]/exp)%10)
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    for i in range(len(arr)-1,-1,-1):
        index=int((arr[i]/exp)%10)
        result[count[index]-1]=arr[i]
        count[index]-=1
    for i in range(0,len(arr)):
        arr[i]=result[i]
def radixsort(arr):
    max_ele=max(arr)
    exp=1
    while max_ele//exp>0:
        countsort(arr,exp)
        exp*=10
arr=list(map(int,input("Enter the element with separated space: ").split()))
radixsort(arr)
for i in range(0,len(arr)):
    print(arr[i],end=' ')
    
