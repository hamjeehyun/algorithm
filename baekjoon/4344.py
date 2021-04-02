c=int(input())

for i in range(c):
    arr=list(map(int, input().split()))
    avg=sum(arr[1:])/arr[0]
    cnt=0

    for a in arr[1:]:
        if a>avg:
            cnt+=1

    rate=(cnt/arr[0])*100
    print(str("%.3f" %rate+"%"))
