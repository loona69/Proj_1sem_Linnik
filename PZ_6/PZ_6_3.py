n = list(map(int,input('Впишите несколько целых чисел в ряд: ').split()))
steps = 1
for i in range(steps):
  n.insert(0, n.pop())
print(n)