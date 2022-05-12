# 標準入力
H, W, Q = map(int, input().split())
A = [input().split() for _ in range(Q)]

# 二次元配列 “.”を配置
dot = [["."] * W for _ in range(H)]

# S配列の該当番地に文字列置き換え
for i in range(Q):
    dot[int(A[i][0])-1][int(A[i][1])-1] = A[i][2]

# 配列を文字列結合してそれぞれ出力
for j in range(H):
    print("".join(dot[j]))