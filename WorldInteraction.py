from Character import player
from Index import changingpicture as cpw
from Enemies import *

def playerinteracted():
    # guard 1
    if player.x > 1310 and player.x < 1335:
        if player.y > 475 and player.y < 500:
            player.x = 1323
            player.y = 505
            cpw.i = 4
    # guard 2
    if player.x > 785 and player.x < 820:
        if player.y > 475 and player.y < 510:
            player.x = 802
            player.y = 515
            cpw.i = 11
    # guard 3
    if player.x > 300 and player.x < 345:
        if player.y > 475 and player.y < 520:
            player.x = 323
            player.y = 525
            cpw.i = 12
    # guard 4
    if player.x > 1300 and player.x < 1350:
        if player.y > 200 and player.y < 250:
            player.x = 1325
            player.y = 255
            cpw.i = 13
    # guard 5
    if player.x > 300 and player.x < 365:
        if player.y > 200 and player.y < 265:
            player.x = 330
            player.y = 270
            cpw.i = 14
    # guard 6
    if player.x > 770 and player.x < 850:
        if player.y > 200 and player.y < 280:
            player.x = 810
            player.y = 285
            cpw.i = 15
    # King
    if player.x > 750 and player.x < 855:
        if player.y > 25 and player.y < 125:
            cpw.i = 9
    # Shop
    if player.x > 775 and player.x < 815:
        if player.y > 740 and player.y < 780:
            player.x = 800
            player.y = 785
            cpw.i = 5
    # House
    if player.x > 1445 and player.x < 1465:
        if player.y > 710 and player. y < 740:
            player.x = 1455
            player.y = 745
    

def showcombatguard1():
    """Displays Combat for enemy"""
    # Blue Colour
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # Red Colour
    fill(255, 0, 0)
    # Red circle representing enemy
    ellipse(1400, 450, 25, 25)
    # Green colour
    fill(0, 255, 0)
    # Green text for instruction on how to attack
    text('Right click to attack', 850, 200)
    # Initiates battle
    player.fight(castle_guard1, 10)


def showcombatguard2():
    """Displays Combat for enemy"""
    # Blue Colour
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # Red Colour
    fill(255, 0, 0)
    # Red circle representing enemy
    ellipse(1400, 450, 25, 25)
    # Green colour
    fill(0, 255, 0)
    # Green text for instruction on how to attack
    text('Right click to attack', 850, 200)
    # Initiates battle
    player.fight(castle_guard2, 50)
    

def showcombatguard3():
    """Displays Combat for enemy"""
    # Blue Colour
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # Red Colour
    fill(255, 0, 0)
    # Red circle representing enemy
    ellipse(1400, 450, 25, 25)
    # Green colour
    fill(0, 255, 0)
    # Green text for instruction on how to attack
    text('Right click to attack', 850, 200)
    # Initiates battle
    player.fight(castle_guard3, 100)


def showcombatguard4():
    """Displays Combat for enemy"""
    # Blue Colour
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # Red Colour
    fill(255, 0, 0)
    # Red circle representing enemy
    ellipse(1400, 450, 25, 25)
    # Green colour
    fill(0, 255, 0)
    # Green text for instruction on how to attack
    text('Right click to attack', 850, 200)
    # Initiates battle
    player.fight(castle_guard4, 300)


def showcombatguard5():
    """Displays Combat for enemy"""
    # Blue Colour
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # Red Colour
    fill(255, 0, 0)
    # Red circle representing enemy
    ellipse(1400, 450, 25, 25)
    # Green colour
    fill(0, 255, 0)
    # Green text for instruction on how to attack
    text('Right click to attack', 850, 200)
    # Initiates battle
    player.fight(castle_guard5, 800)


def showcombatguard6():
    """Displays Combat for enemy"""
    # Blue Colour
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # Red Colour
    fill(255, 0, 0)
    # Red circle representing enemy
    ellipse(1400, 450, 25, 25)
    # Green colour
    fill(0, 255, 0)
    # Green text for instruction on how to attack
    text('Right click to attack', 850, 200)
    # Initiates battle
    player.fight(castle_guard6, 1500)


def finalcombatking():
    # Blue Color
    fill(0, 0, 255)
    # Blue rectangle representing player
    rect(200, 450, 25, 25)
    # random colours for final boss
    fill(random(0, 255), random(0, 255), random(0, 255))
    # random coloured boss
    ellipse(1400, 450, 25, 25)
    # green color
    fill(0, 255, 0)
    # Showing how to attack
    text('Right click to attack', 850, 200)
    # initiates final fight
    player.fightking()


def shop():
    textSize(20)
    text('* Type [z] to buy Spear (100 GOLD)', 100, 600)
    text('* Type [x] to buy Kopesh (250 GOLD)', 100, 630)
    text('* Type [c] to buy Shovel (1800 GOLD)', 100, 660)
    text('* Type [v] to buy Shotel (5000 GOLD)', 100, 690)
    text('* Type [b] to buy Zweihander (20000 GOLD)', 100, 720)
    text('* Type [f] to buy Sandwich (100 GOLD)', 1000, 600)
    text('* Type [g] to buy Slice of Pizza (60 GOLD)', 1000, 630)
    text('* Type [j] to buy Box of Pizza (900 GOLD)', 1000, 660)
    text('* Type [k] to buy Bottle O Sprite (25 GOLD)', 1000, 690)
    text('* Type [L] to buy Soup (300 GOLD)', 1000, 720)
    rectMode(CORNER)
    fill(0)
    textSize(55)
    text('shop', 650, 150)
    rect(500, 300, 500, 200)
