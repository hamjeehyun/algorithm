import sys
input = sys.stdin.readline
st = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
s = input().strip()
result = 0
s = s[::-1]
for i in range(1, len(s)):
    result += st.index(s[i]) * (16 ** i)
result += st.index(s[0])
print(result)