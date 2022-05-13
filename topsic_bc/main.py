S = list(input())
print(S) # ['a', 'a', 'b', 'b', 'c', 'c']

set_S = set(S)
print(set_S) # {'b', 'a', 'c'}

ans = len(set_S)
print(ans)


# S = input()

# S_len = len(S)

# count = 0

# count = S_len

# for i in range(S_len):
    # for j in range(i+1, S_len):
            # if S[i] == S[j]:
                # count = count - 1
                # break

# print(count)