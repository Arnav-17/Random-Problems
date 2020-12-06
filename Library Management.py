import time


def signup():
    username = input('Enter username: \n')
    password = input('Enter password: \n')
    with open('Login.txt', 'a') as f:
        f.write(username)
        f.write(',')
        f.write(password)
        f.write('\n')
        print('Signed up successfully')


def login():
    username1 = input('Enter username: \n')
    password1 = input('Enter password: \n')
    with open('Login.txt') as f:
        m = []
        for i in f:
            keys = i.split(',')
            username = keys[0]
            password = keys[1]
            char = len(password) - 1
            password2 = password[0:char]
            m.append(username)
            m.append(password2)
        while 1 == 1:
            if username1 in m and password1 in m:
                print('Login Successful')
            elif username1 in m and password1 not in m:
                print('Invalid Password')
                break
            elif username not in m and password1 in m:
                print('Invalid Username')
                break
            elif username not in m and password1 not in m:
                print('Invalid Credentials')
                break
            print(f'Welcome {username1}')
            with open('Login logs.txt', 'a') as xyz:
                xyz.write(f"Name:-{username1}, logged in at {time.asctime(time.localtime(time.time()))}\n")
            d = input('Enter 1 to see books, 2 to issue book, 3 to donate book, 4 to return book\n')
            if d == '1':
                p = input('Enter 1 to see list of all books and 2 to see list of books currently available.\n')
                if p == '1':
                    with open('All Books.txt') as nbc:
                        print(f"The books available are:- \n")
                        print(nbc.read())
                elif p == '2':
                    with open('Current Books.txt') as nbc:
                        print(f"The books available are:- \n")
                        print(nbc.read())
            elif d == '2':
                b = input(f'Enter book\'s name\n')
                with open('Current Books.txt') as r:
                    x = r.read()
                    if b in x:
                        with open('Issue logs.txt', 'a') as lol:
                            lol.write(f'Name:-{username1}, Book:-{b} issued at {time.asctime(time.localtime(time.time()))}\n')
                            print('Book issued successfully')
                            with open('Current Books.txt', 'r') as xyz:
                                lols = xyz.readlines()
                            with open('Current Books.txt', 'w') as xyz:
                                for line in lols:
                                    if line.strip('\n') != b:
                                        xyz.write(line)
                    else:
                        print('The book you want is currently not available')
            elif d == '3':
                j = input("Enter the book you want to donate\n")
                with open('Current Books.txt', 'a') as y:
                    y.write(f'{j}\n')
                    print('Books donated Successfully')
                    print('Thank You for your donation')
                with open('All Books.txt', 'a') as z:
                    z.write(f'{j}\n')
            elif d == '4':
                m = input('Enter the book\'s name you want to return\n')
                c = []
                with open('All Books.txt', 'r+') as abc:
                    for item in abc:
                        chars = len(item) - 1
                        key = item[0:chars]
                        c.append(key)
                with open('Current Books.txt', 'a') as cde:
                    if m not in c:
                        print('This book doesnt belong to the library')
                    else:
                        cde.write(m)
                        print('Book returned successfully')
            break


a = input('Enter 1 for signup, 2 for login\n')
if a == '1':
    signup()
elif a == '2':
    login()
