n=int(input())
arr=list(map(int, input().split()))

arr2=[]
max=max(arr)
for i in range(n):
    arr2.append(arr[i]/max*100)

print(sum(arr2)/n)