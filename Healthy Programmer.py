from pygame import mixer
import time
c = input('Enter 1 for logging and starting program, 2 for retrieving\n')
if c == '1':
    def eyes():
        mixer.init()
        mixer.music.load('Eyes.wav')
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        p = time.asctime(time.localtime(time.time()))
        while True:
            d = input("Press 'Eydone' to exit the program\n")
            if d == 'Eydone':
                mixer.music.stop()
                break
        with open('Eyes.txt', 'a') as file:
            file.write(f'{p} \n')


    def Water():
        mixer.init()
        mixer.music.load('Water.wav')
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        p = time.asctime(time.localtime(time.time()))
        while True:
            d = input("Press 'Drank' to exit the program\n")
            if d == 'Drank':
                mixer.music.stop()
                break
        with open('Water.txt', 'a') as foo:
            foo.write(f'{p}\n')

    def Physical():
        mixer.init()
        mixer.music.load('Physical.wav')
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        p = time.asctime(time.localtime(time.time()))
        while True:
            d = input("Press 'Exdone' to exit the program\n")
            if d == 'Exdone':
                mixer.music.stop()
                break
        with open('Physical.txt', 'a') as loo:
            loo.write(f'{p} \n')

    a = int(time.time())

    for i in range(28880):
        time.sleep(1)
        b = int(time.time())
        if (b-a) % 5400 == 0:
            eyes()
            Water()
            Physical()
        elif (b-a) % 1800 == 0:
            eyes()
            Water()
        elif (b-a) % 2700 == 0:
            Physical()
elif c == '2':
    x = input('Enter 1 for Eyes.txt, 2 for Water.txt, 3 for Physical.txt')
    if x == '1':
        with open('Eyes.txt') as f:
            f.read()
    elif x == '2':
        with open('Water.txt') as f:
            f.read()
    elif x == '3':
        with open('Physical.txt') as f:
            f.read()
