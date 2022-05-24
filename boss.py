import keyboard
import random
import time
import os
print("start")
max = 50
timeout = 0.01
bosslive = 6
yourlive = 10
start = 1
namy = 1
nam = 0
print("max = " + str(max))
while nam < namy:
    while nam - namy < 10:
        namy = random.randrange(2,(max - 1))
        nam = random.randrange(1,(max - 1))
os.system("cls")
bonus = "b"
player = "p"
def bot():
    global yourlive
    global timeout
    global namy
    global nam
    time.sleep(timeout)
    ran = random.randrange(0,6)
    ran1 = random.randrange(0,20)
    if ran1 < 2:
        if nam - namy < 2:
            yourlive -= 1
            #os.system("cls")
            #print("bot win")
            #time.sleep(0.6)
            #exit() 
    elif ran < 4:
        if namy + 2 == nam:
            ran = random.randrange(0,8)
            if ran < 2:
                namy -= 2
        if not namy - 1 == max:
            if not namy + 1 == nam:
                namy += 1
            else:
                ran = random.randrange(0,6)
                if ran < 3:
                    namy -= 1
                namy += 2
    else:
        if not namy == 1:
            namy -= 1
def main(nam):
    global bosslive
    global yourlive
    line = "|"
    y = 0
    while y < ((nam / 2) - 5):
        line += "."
        y += 1
    y += 1
    line += str((nam + 1))
    while y < 10 :
        line += '*'
        y += 1
    line += player + '|' + bonus
    y = 0
    while y < ((nam / 2) - 5):
        line += "."
        y += 1
    y += 1
    line += str(nam - namy)
    while y < 10 :
        line += '*'
        y += 1
    line += player + '|'
    os.system("cls")
    #...................................
    print(line)
    x = 0
    pr = "|"
    while x < namy:
        pr += "."
        x += 1
    pr += bonus
    while x < nam:
        pr += "~"
        x += 1    
    pr += player
    x += 1
    while x < max:
        pr += '*'
        x += 1
    pr += ('|')
    if bosslive == 0:
        os.system("cls")
        print("your win")
        time.sleep(2)
        exit()
    elif yourlive == 0:
        os.system("cls")
        print("your lost")
        time.sleep(2)
        exit()
    if nam == (namy - 1):
        bosslive -= 1
    elif nam < namy:
        yourlive -= 1
    else:
        print(pr)
        #................
        #global bosslive
        #global yourlive
        px = 'bosslive:'
        ppx1 = 0
        ppx2 = 0
        while ppx1 < bosslive:
            ppx1 += 1
            px += '*'
        px += "  yourlive:"
        while ppx2 < yourlive:
            ppx2 += 1
            px += '*'
        print(px)
time.sleep(0.02)
os.system("cls")
print('hey, the-end')
print('"' + player+ '"' + " = player")
print("\"d\" = right")
print("\"a\" = left")
print("\"e\" = fire")
print("\"end\" = exit")
print('"' + bonus+ '"' + " = boss")
print("please wait \"10s\", for start")
print("_____________")
time.sleep(10)
while 1==1:
    bot()
    if keyboard.is_pressed('d'):
        player = 'p'
        if not nam > (max - 2):
            nam += 1
        else:
            nam = (max - 1)
    elif keyboard.is_pressed('a'):
        player = 'q'
        if not nam < 1:
            nam -= 1
        else:
            nam = 0
    elif keyboard.is_pressed('e'):
        ran = random.randrange(0,10)
        if ran < 4:
            if nam - namy < 10:
                player = ("<<<<<<<<<<< " + player)
                bosslive = 1
                nam = namy
                time.sleep(0.02)
                timeout = 0.001
    elif keyboard.is_pressed('s'):
        main(nam)
    main(nam)