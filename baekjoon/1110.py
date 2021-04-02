n=int(input())
m=n
cnt=0

while True:
    a=n%10 # 일의 자리
    b=n//10 # 십의 자리

    n=a*10 + (a+b)%10
    cnt+=1
    
    if(m==n): break

print(cnt)