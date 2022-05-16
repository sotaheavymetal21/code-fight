N = int(input())
S = [int(input()) for _ in range(N)]

x_coordinate = 0
y_coordinate = 0

for i in range(1, N+1):
    if i % 4 == 0:
        y_coordinate = y_coordinate + S[i-1]
    elif i % 4 == 3:
        x_coordinate = x_coordinate - S[i-1]
    elif i % 4 == 2:
        y_coordinate = y_coordinate - S[i-1]
    else:
        x_coordinate = x_coordinate + S[i-1]

print(x_coordinate, y_coordinate)

N = int(input())
D = [int(input()) for i in range(N)]
print(D)
x = 0
y = 0
for j in range(N):
    x = sum(D[::4]) - sum(D[2::4])
    y = sum(D[3::4]) - sum(D[1::4])
print(D[::4])
print(D[2::4])
print(D[3::4])
print(D[1::4])
print(x, y)
# [3, 1, 4, 1, 5, 9]
# [3, 5]
# [4]
# [1]
# [1, 9]
# 4 -9