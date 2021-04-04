max_total=0
total=0

for _ in range(10):
    out_train, in_train=map(int, input().split())
    total += in_train - out_train  
    max_total=max(total, max_total)

print(max_total)