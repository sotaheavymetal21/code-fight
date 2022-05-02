N = int(input())
A = list(map(int, input().split()))

new_list = sorted(A)

flag = True

for i in range(N-1):
    if new_list[i] == new_list[i+1]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")