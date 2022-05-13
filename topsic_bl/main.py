S =list(input())
mydict = {"a": 1, "s": 2, "d": 3, "f": 4, "g": 5, "h": 6, "j": 7, "k": 8, "l": 9}

A = []
for i in range(len(S)):
    A.append(mydict[S[i]])
ans = 0

for i in range(len(S) - 1):
    ans += (abs(A[i] - A[i + 1]) + 1)

ans = ans + A[0]
print(ans)

# ---------------------------------


# S = input()
# S_len = len(S)

# for i in range(S_len):
#     if S[i] == "a":
#         S[i] = 1
#     elif S[i] == "s":
#         S[i] = 2
#     elif S[i] == "d":
#         S[i] = 3
#     elif S[i] == "f":
#         S[i] = 4
#     elif S[i] == "g":
#         S[i] = 5
#     elif S[i] == "h":
#         S[i] = 6
#     elif S[i] == "j":
#         S[i] = 7
#     elif S[i] == "k":
#         S[i] = 8
#     elif S[i] == "l":
#         S[i] = 9

# # ans = 0

# # for j in range(S_len - 1):
# #     ans += (abs(S[j] - S[j + 1]) + 1)

# # ans = ans + S[0]
# # print(ans)

# # S = input()
# # K = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

# # tap = len(S)
# # move = 0
# # now_position = 0

# # for i in range(len(S)):
# #     for j in range(len(K)):
# #         if K[j] == S[i]:
# #             print(f"Sは{S[i]}でKは{K[j]}")
# #             print(f"今いるのは{now_position}で、{j}までいくと")
# #             if now_position > j:
# #                 move += now_position - j
# #             elif now_position < j:
# #                 move += j - now_position
# #             print(f"{move}動くで")
# #             now_position = j

# # ans = tap + move
# # print(ans)
