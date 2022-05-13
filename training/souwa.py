N = int(input())

ans = 0

for i in range(1, N + 1):
    print(f"iは{i}")
    ans += N // i * i
    print(f"代入する数字は{N // i * i}")
    print(f"ansは{ans}")

print(ans)
