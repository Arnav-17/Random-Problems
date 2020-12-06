import random
print('Welcome to Stone-Paper-Scissors Game')
b = ['St', 'Sc', 'P']
d = 0
e = 0
for i in range(10):
    c = random.choice(b)
    a = input('Enter Sc for Scissor, P for Paper, St for Stone\n')
    if c == "St":
        if a == 'P':
            d += 1
        elif a == "Sc":
            e += 1
    elif c == 'Sc':
        if a == 'St':
            d += 1
        elif a == 'P':
            e += 1
    elif c == 'P':
        if a == 'Sc':
            d += 1
        elif a == 'St':
            e += 1
    print(c)
print(f'Your Score is {d}')
print(f"Computer's Score is {e}")
if e > d:
    print("Sorry, You Lost")
elif e == d:
    print("Its a tie")
elif e < d:
    print("Congratulations, You Won!!")