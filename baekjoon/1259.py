n = int(input())

# 조건
while n != 0:
    n_list = list(map(int, str(n)))

    if n_list == n_list[::-1]:
        print("yes")
    else:
        print("no")
    n = int(input())