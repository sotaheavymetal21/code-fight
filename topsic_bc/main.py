S = input()

S_len = len(S)

count = 0

count = S_len

for i in range(S_len):
    for j in range(i+1, S_len):
            if S[i] == S[j]:
                count = count - 1
                break

print(count)