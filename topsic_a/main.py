N = int(input())


for i in range(N):
    S[i] = input()
    print(S)

count = 1

for i in range(N):
    if S[i] != S[i+1]:
        count += 1

print(count)