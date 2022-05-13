# 標準入力
N = int(input())
A = list(map(int, input().split()))

# フラグ定義
flag = True

# N-2で繰り返し処理、足して割ったものの方が大きかったらFalseに変えて終了する
for i in range(1, N - 1):
    # print(i, A[i])
    if (A[i - 1] + A[i + 1]) // 2 >= A[i]:
        flag = False
        break

# 出力
if flag:
    print("YES")
else:
    print("NO")