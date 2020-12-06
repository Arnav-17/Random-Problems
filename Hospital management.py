import time
print('Welcome to Hospital Management System')
a = input("Enter 1 for Log, 2 for Retrieve\n")
b = input("Enter 1 for Arnav, 2 for Harsh, 3 for Pranav\n")
c = input('Enter 1 for Diet, 2 for Exercise\n')


def Hospital(x, y, z):
    p = time.asctime(time.localtime(time.time()))
    if a == '1':
        if b == '1':
            if c == '1':
                d = input('Enter the data\n')
                with open('Arnav Diet.txt', 'a') as f:
                    f.write(f'{p} {d}\n')
                    print('Data entered successfully')
            elif c == '2':
                d = input('Enter the data\n')
                with open('Arnav Exercise.txt', 'a') as f:
                    f.write(f'{p} {d}\n')
                    print('Data entered successfully')
            else:
                print('Enter valid number')
        elif b == '2':
            if c == '1':
                d = input('Enter the data\n')
                with open('Harsh Diet.txt', 'a') as f:
                    f.write(f'{p} {d} \n')
                    print('Data entered successfully')
            elif c == '2':
                d = input('Enter the data\n')
                with open('Harsh Exercise.txt', 'a') as f:
                    f.write(f'{p} {d} \n')
                    print('Data entered successfully')
            else:
                print('Enter valid number')
        elif b == '3':
            if c == '1':
                d = input('Enter the data\n')
                with open('Pranav Diet.txt', 'a') as f:
                    f.write(f'{p} {d} \n')
                    print('Data entered successfully')
            elif c == '2':
                d = input('Enter the data\n')
                with open('Pranav Exercise.txt', 'a') as f:
                    f.write(f'{p} {d} \n')
                    print('Data entered successfully')
            else:
                print('Enter valid number')
    elif a == '2':
        if b == '1':
            if c == '1':
                with open('Arnav Diet.txt') as f:
                    print(f.read())
            elif c == '2':
                with open('Arnav Exercise.txt') as f:
                    print(f.read())
            else:
                print('Enter valid number')
        elif b == '2':
            if c == '1':
                with open('Harsh Diet.txt') as f:
                    print(f.read())
            elif c == '2':
                with open('Harsh Exercise.txt') as f:
                    print(f.read())
            else:
                print('Enter valid number')
        elif b == '3':
            if c == '1':
                with open('Pranav Diet.txt') as f:
                    print(f.read())
            elif c == '2':
                with open('Pranav Exercise.txt') as f:
                    print(f.read())
            else:
                print('Enter valid number')


Hospital(a, b, c)
