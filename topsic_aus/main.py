N = int(input())
A = list(map(int, input().split()))

from_left = 0
from_right = 0

for i in range(1, N):
    from_left += max(0, A[i] - A[i - 1])

for j in reversed(range(1, N)):
    from_right += max(0, A[j - 1] - A[j])

print(min(from_left, from_right))