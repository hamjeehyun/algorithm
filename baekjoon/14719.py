h,w=map(int, input().split())
height=list(map(int, input().split()))
area=0

for i in range(w):
    # 현재 위치에서 왼쪽 블럭 중 가장 높은 블럭의 높이를 구한다.
    left_height=height[i]
    for j in range(i-1, -1, -1):
        if left_height<height[j]:
            left_height=height[j]

    # 현재 위치에서 오른쪽 불럭 중 가장 높은 블럭의 높이를 구한다.
    right_height=height[i]
    for j in range(i, w):
        if right_height<height[j]:
            right_height=height[j]

    # 왼쪽 오른쪽 중 더 작은 높이를 구한다.
    final_height=min(right_height, left_height)

    # 채워져 있는 빗물의 양 = 작은 높이-현재높이
    area+=final_height-height[i]

print(area)
