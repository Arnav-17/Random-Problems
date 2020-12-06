a = []
n = int(input('Enter the number\n'))
for i in range(1, n):
    if n % i == 0:
        a.append(i)

print(a)