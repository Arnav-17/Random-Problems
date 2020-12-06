a = []
n = str(input('Enter a number'))
for i in n:
    a.append(i)
b = len(a)
if b % 2 == 1:
    c = int((b-1)/2)
    count = 0
    for j in range(c):
        for i in range(c):
            if a[i] == a[len(a) - i - 1]:
                count += 1
            else:
                print('It is not a palindrome')
                break
        if count == c:
            print('It is a palindrome')
        else:
            pass
        count += 1
else:
    c = int(b/2)
    for j in range(c):
        count = 0
        for i in range(c):
            if a[i] == a[len(a) - i - 1]:
                count += 1
            else:
                print('It is not a palindrome')
                break
        if count == c:
            print('It is a palindrome')
        else:
            break