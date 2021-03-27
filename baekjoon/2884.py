h, m = input().split()
h=int(h)
m=int(m)

if m < 45:
    h = h-1
    m = 15 + m
    if h < 0:
        print(23, m)
    else:
        print (h, m)
else:
    m = m-45
    print(h, m)