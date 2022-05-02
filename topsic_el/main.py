N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))

ans = 0

for i in range(N):
    if A[i] < B[i]:
        ans = i + 1

print(ans)