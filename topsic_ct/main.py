N = int(input())
S = [int(input()) for _ in range(N)]
print(S)


x_coordinate = 0
y_coordinate = 0

for i in range(1, N+1):
    if i % 4 ==0:
        y_coordinate = y_coordinate + S[i-1]
    elif i % 4 == 3:
        x_coordinate = x_coordinate - S[i-1]
    elif i % 4 == 2:
        y_coordinate = y_coordinate - S[i-1]
    else:
        x_coordinate = x_coordinate + S[i-1]

print(x_coordinate, y_coordinate)