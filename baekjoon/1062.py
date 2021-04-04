n, k=map(int, input().split())
cnt=0

for i in range(n):
    char=input()
    char_list=list(char)
    char_list_unique=set(char_list)

    if len(char_list_unique) <= k:
        cnt+=1
print(cnt) 