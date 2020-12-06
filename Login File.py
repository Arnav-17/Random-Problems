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
    with open('Login.txt') as f:
        username1 = input('Enter username: \n')
        password1 = input('Enter password: \n')
        m = []
        for i in f:
            keys = i.split(',')
            username = keys[0]
            password = keys[1]
            char = len(password) - 1
            password2 = password[0:char]
            m.append(username)
            m.append(password2)
        if username1 in m and password1 in m:
            print('Login Successful')
        elif username1 in m and password1 not in m:
            print('Invalid Password')
        elif username not in m and password1 in m:
            print('Invalid Username')
        elif username not in m and password1 not in m:
            print('Invalid Credentials')


a = input('Enter 1 for signup, 2 for login\n')
if a == '1':
    signup()
elif a == '2':
    login()
