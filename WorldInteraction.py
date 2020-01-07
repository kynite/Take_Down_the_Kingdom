from Character import player
from Index import changingpicture as cpw
from Enemies import *

def playerinteracted():
    # guard 1
    number = random(0, 10)
    if player.x > 1310 and player.x < 1335:
        if player.y > 475 and player.y < 500:
            player.x = 1323
            player.y = 505
            if number > 0 and number < 4:
                cpw.i = 4
    # guard 2
    if player.x > 785 and player.x < 820:
        if player.y > 475 and player.y < 510:
            print('b')
    # guard 3
    if player.x > 300 and player.x < 345:
        if player.y > 475 and player.y < 520:
            print('c')
    # guard 4
    if player.x > 1300 and player.x < 1350:
        if player.y > 200 and player.y < 250:
            print('d')
    # guard 5
    if player.x > 300 and player.x < 355:
        if player.y > 200 and player.y < 255:
            print('e')
    # guard 6
    if player.x > 770 and player.x < 830:
        if player.y > 200 and player.y < 260:
            print('f')
    

def showcombatguard1():
    fill(0, 0, 255)
    rect(200, 450, 25, 25)
    fill(255, 0, 0)
    ellipse(1400, 450, 25, 25)
    fill(0, 255, 0)
    text('Right click to attack', 850, 200)
    player.fight(castle_guard, 10)
