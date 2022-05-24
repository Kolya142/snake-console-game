import keyboard
import random
import time
import os
print("start")
cols, lines = os.get_terminal_size()
max = ((cols * lines) - 160)
timeout = 0
start = 1
namy = 1
nam = 0
#alog = open('a.log', '+r')
#alog.write('__________\n')
print("max = " + str(max))
while nam < namy:
    while nam - namy < 10:
        namy = random.randrange(150, (max - 1))
        nam = random.randrange(146, (max - 1))
os.system("cls")
score = 0
bonus = "a"
player = "#"


def bot():
    global score
    global namy
    global nam
    os.system('cls')
    print('initialization')
    score += 1
    nam = namy
    while nam - namy < 10:
        time.sleep(0.01)
        namy = random.randrange(100, (max - 1))
        nam = random.randrange(99, (max - 1))
        #alog.write(alog.read() + '\napple:' + str(namy))
        #alog.write(alog.read() + '\nsnake:' + str(nam))
        print(namy)
        print(nam)
    #alog.write(alog.read() + '\n__________')
    time.sleep(0.01)
    os.system('cls')
    main(nam)

def main(nam):
    os.system("cls")
    x = 0
    pr = ""
    if score > 10:
        os.system('cls')
        import boss
    if namy < nam:
        while x < namy:
            pr += "."
            x += 1
        pr += bonus
        while x < nam:
            pr += "."
            x += 1
        pr += player
        x += 1
        while x < max:
            pr += '*'
            x += 1
        pr += ('')
    else:
        while x < nam:
            pr += "."
            x += 1
        pr += player
        while x < namy:
            pr += "."
            x += 1
        pr += bonus
        x += 1
        while x < max:
            pr += '*'
            x += 1
        pr += ('')
    #show
    print(pr)
    print("score:" + str(score))
    #print(namy)
    #print(nam)
time.sleep(0.02)
os.system("cls")
os.system("title snake game")
print('"' + player + '"' + " = player")
print('use "wasd", for move')
print('press "r", for restart')
print('"' + bonus + '"' + " = apple")
print("press \"enter\", for start")
print("_____________")
input()
main(nam)
while 1 < 2:
    if nam == namy:
        bot()
    if nam > max - 1:
        nam = n1
        main(nam)
    if nam < 0:
        nam = n1
        main(nam)
    if keyboard.is_pressed('a'):
        n1 = nam
        nam -= 1
        if nam == namy:
            bot()
        player = '#'
        main(nam)
    if keyboard.is_pressed('d'):
        n1 = nam
        nam += 1
        player = '#'
        main(nam)
    if keyboard.is_pressed('w'):
        n1 = nam
        #if not nam - cols < namy:
        nam = nam - cols
        main(nam)
    if keyboard.is_pressed('s'):
        n1 = nam
        nam = nam + cols
        main(nam)
    if keyboard.is_pressed('r'):
        cols, lines = os.get_terminal_size()
        if cols * lines > 160:
            max = ((cols * lines) - 160)
        elif cols * lines < 160:
            max = ((cols * lines))
        nam = namy - 1000000
        while nam < namy:
            while nam - namy < 10:
                namy = random.randrange(100, (max - 1))
                nam = random.randrange(99, (max - 1))
        main(nam)
    if keyboard.is_pressed('esc'):
        os.system('cls')
        print('exit(yes(y) or no(n)):')
        en = 0
        while en == 0:
            if keyboard.is_pressed('n'):
                en = 1
            elif keyboard.is_pressed('y'):
                alog.close()
                expo = 5
                for x in range(0, 5, 1):
                    os.system('cls')
                    print(expo)
                    expo -= 1
                    time.sleep(0.1)
                exit()
        main(nam)
