n = int(input())

for i in range(1, n):
    if i * i > n:
        k = i
        break
print(k)
