b = set()
def Pal(n):
    for l in range(n):
        a = []
        x = str(l)
        for i in x:
            a.append(i)
        b = len(a)
        if b % 2 == 1:
            c = int((b-1)/2)
            for j in range(c):
                count = 0
                for i in range(c):
                    if a[i] == a[len(a) - i - 1]:
                        count += 1
                if count == c:
                    print(l)
                count += 1
        else:
            c = int(b/2)
            for j in range(c):
                count = 0
                for i in range(c):
                    if a[i] == a[len(a) - i - 1]:
                        count += 1
                if count == c:
                    print(l)
                count += 1
