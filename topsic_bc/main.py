S = input()

len_S = len(S)

count = 1
for i in range(len_S-1):
    if S[i] != S[i+1]:
        count += 1

print(count)
