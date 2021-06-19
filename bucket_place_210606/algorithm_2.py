import sys
input = sys.stdin.readline

n = int(input())
arr = [n]

for _ in range(n):
    a = int(input())
    arr.append(a)

left = n
steps = 0

def go(arr, start, end):
    global left, steps

    if left < 4:
        if left == 3:
            left -= 3

            steps += arr[start] + arr[start + 1] + arr[3]

        if left == 2:
            left -= 2
            steps += arr[start + 1]
        print(steps)
        return

    left -= 2
    steps += arr[start + 1]

    left += 1
    steps += arr[start]

    left -= 2
    steps += arr[end]

    left += 1
    steps += arr[start+1]

    end -= 2
    go(arr, 1, end)

go(arr, 1, arr[0])