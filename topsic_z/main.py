N = int(input())

# 1つの値について、その約数の和を出す関数
# a...求めたい値
def calc(a: int) -> int:

    j = 1
    total = 0
    while j * j <= a:
        if a % j == 0:
            total += j
            if j != a // j:
                total += (a // j)
            # jはiの約数であることが確定
        j += 1

    return total

ans = 0
# 1〜Nまで約数を出していく
for i in range(1, N+1):
    ans += calc(i)

print(ans)

# N = int(input())

# sum_divisors = 0

# for i in range(1, N + 1):
#     for j in range(1,  i + 1):
#         if i % j == 0:
#             sum_divisors += j

# print(sum_divisors)

# # N = int(input())
# # A = []
# # for x in range(1, N + 1):
# #     A.append(x)
# # print(A) # [1, 2, 3, 4, 5]

# # sum_divisors = 0

# # for i in range(1, N + 1):
# #     if A[i] % i == 0:
# #         sum_divisors += i

# # print(sum_divisors)