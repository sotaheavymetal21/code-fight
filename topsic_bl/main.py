S = list(input())
S_len = len(S)
for i in range(S_len):
    if S[i] == "a":
        S[i] = 1
    elif S[i] == "s":
        S[i] = 2
    elif S[i] == "d":
        S[i] = 3
    elif S[i] == "f":
        S[i] = 4
    elif S[i] == "g":
        S[i] = 5
    elif S[i] == "h":
        S[i] = 6
    elif S[i] == "j":
        S[i] = 7
    elif S[i] == "k":
        S[i] = 8
    elif S[i] == "l":
        S[i] = 9
ans = 0
for j in range(S_len - 1):
    print(j)
    ans += (abs(S[j] - S[j + 1]) + 1)
    print(ans)
ans = ans + S[0]
print(ans)