N = int(input())

if N % 100 != 0:
    print(-1)
else:
    count = 0
    count = count + N // 500
    count = count + (N % 500) // 100
    print(count)