import sys
input = sys.stdin.readline

a=int(input())
b=input()

out1 = a * int(b[2])
out2 = a * int(b[1])
out3 = a * int(b[0])
out4 = a * int(b)

print(out1, out2, out3, out4, sep="\n")
