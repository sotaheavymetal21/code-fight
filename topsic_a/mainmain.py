N = input()
N_int = int(N)

gohyakuenn = 0
hyakuenn = 0
youkoso = 0

count = 0

if N[-1] != 0 or N[-2] != 0:
    print(-1)
elif N_int >= 500:
    gohyakuenn = N_int / 500
    count = count + round(gohyakuenn)
    youkoso = N_int % 500
    hyakuenn = youkoso / 100
    count = count + hyakuenn
    print(round(count))
else:
    hyakuenn = N_int / 100
    count = count + hyakuenn
    print(round(count))