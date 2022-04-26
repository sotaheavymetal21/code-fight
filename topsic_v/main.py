N = int(input())

S = input()
S_list = list(S)

count = 1

for i in range(N-1):
    if S[i] != S[i+1]:
        count += 1

print(count)