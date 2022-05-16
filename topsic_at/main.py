# 標準入力
N, G, A = map(int, input().split())

#反対人数
H = (N * G) - A

M = 0
m = 0

# グループの過半数で賛成人数を割り賛成グループになりうる最大値を取得する。
if A // (N // 2 + 1) > G:
    M = G
else:
    M = A // (N // 2 + 1)

# グループの過半数で反対人数を割り反対グループになりうる最小値を取得する。
if H // (N // 2 + 1) > G:
    m = G
else:
    m = G - H // (N // 2 + 1)

print(M, m)


# W = [[""] * N for _ in range(G)]

# # ans = 0
# # count = 0
# # for i in range(G):
# #     for j in range(N):
# #         W[i][j] = True
# #         if W[i][j] == True:
# #             count += 1
# #             print(f"W[i]の中身は{W[i]}")
# #             if count > N - count and True <= A:
# #                 ans += 1
# #                 print(f"Trueの方が大きいからansは{ans}")
# #             if count == 6:
# #                 count = 0
# #             print(f"Trueの数は{count}")

# # print(ans)
