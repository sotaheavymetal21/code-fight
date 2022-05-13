for i in range(1, 20):
  if i % 2 == 0:
    print(i, ", continue")
    continue
  if i == 13:
    print(i, ", break")
    break
  print(i, ", 通過")
