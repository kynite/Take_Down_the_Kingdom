from Character import *
import Main
from Index import changingpicture as cp
from World import *
import WorldInteraction as wi


def setup():
    """Sets up window of game"""
    # Window/game size is 1600x900
    size(1600, 900)
    # Background set to white
    background(255)


def keyPressed():
    """
    If a certain key is pressed only run the command once,
    some only run in certain events/screens
    """
    # Moving
    if key == 'w' and cp.i == 1:
        loop()
        player.movenorth()
    if key == 's' and cp.i == 1:
        loop()
        player.movesouth()
    if key == 'a' and cp.i == 1:
        loop()
        player.movewest()
    if key == 'd' and cp.i == 1:
        loop()
        player.moveeast()
    # Inventory
    if key == "i" and cp.i == 1 or cp.i == 3:
        loop()
        cpw.i = 2
    if key == 'q' and not cp.i == 9 or cp.i == 10:
        redraw()
        cpw.i = 1
    # Healing screen
    if key == 'h' and cp.i == 2:
        redraw()
        cpw.i = 3
    # Healing
    if key == 'y':
        player.bottleospriteheal()
    if key == 'u':
        player.sliceofpizzaheal()
    if key == 'o':
        player.sandwichheal()
    if key == 'p':
        player.soupheal()
    if key == 'r':
        player.boxofpizzaheal()
    # Key to resume loop
    if key == 'c':
        loop()
    # Shop
    if key == 'z'and cp.i == 5:
        player.buyspear()
    if key == 'x'and cp.i == 5:
        player.buykopesh()
    if key == 'c'and cp.i == 5:
        player.buyshovel()
    if key == 'v'and cp.i == 5:
        player.buyshotel()
    if key == 'b'and cp.i == 5:
        player.buyzweihander()
    if key == 'f'and cp.i == 5:
        player.buysandwich()
    if key == 'g'and cp.i == 5:
        player.buysliceofpizza()
    if key == 'j'and cp.i == 5:
        player.buyboxofpizza()
    if key == 'k'and cp.i == 5:
        player.buybottleosprite()
    if key == 'l'and cp.i == 5:
        player.buysoup()
    # Teleport home
    if key == 't' and cp.i == 1:
        player.x = 1445
        player.y = 750


def draw():
    """Draws the images on screen if index matches"""
    if cp.i == 0:
        Main.mainmenu()
    elif cp.i == 1:
        background(255)
        fill(0)
        text('Use [WASD] to move', 1400, 890)
        text('Type [i] to open Inventory', 1350, 870)
        player.outofbounds()
        wi.playerinteracted()
        player.playericon()
        player.showgold()
        KingsPalace(800, 75)
        PlayerHouse(1445, 720)
        GuardHouseNo1(1310, 475)
        GuardHouseNo2(785, 475)
        GuardHouseNo3(300, 475)
        GuardHouseNo4(1300, 200)
        GuardHouseNo5(300, 200)
        GuardHouseNo6(770, 200)
        Trader(775, 740)
    elif cp.i == 2:
        background(255)
        player.showinventory()
    elif cp.i == 3:
        background(255)
        player.showhealing()
    elif cp.i == 4:
        loop()
        background(255)
        wi.showcombatguard1()
    elif cp.i == 5:
        loop()
        background(255)
        wi.shop()
    elif cp.i == 6:
        loop()
        background(255)
        player.showtext1()
    elif cp.i == 7:
        loop()
        background(255)
        player.showtext2()
    elif cp.i == 8:
        loop()
        background(255)
        player.showtext3()
    elif cp.i == 9:
        loop()
        background(255)
        wi.finalcombatking()
    elif cp.i == 10:
        background(255)
        player.showending()
    elif cp.i == 11:
        background(255)
        loop()
        wi.showcombatguard2()
    elif cp.i == 12:
        background(255)
        loop()
        wi.showcombatguard3()
    elif cp.i == 13:
        background(255)
        loop()
        wi.showcombatguard4()
    elif cp.i == 14:
        background(255)
        loop()
        wi.showcombatguard5()
    elif cp.i == 15:
        background(255)
        loop()
        wi.showcombatguard6()
    elif cp.i == 16:
        background(255)
        loop()
        player.playericon()
        rectMode(CORNER)
        PlayerHouse(1445, 720)
        Main.maintext()
    elif cp.i == 17:
        background(255)
        loop()
        Main.maintext2()
        GuardHouseNo1(1310, 475)
        GuardHouseNo2(785, 475)
        GuardHouseNo3(300, 475)
        GuardHouseNo4(1300, 200)
        GuardHouseNo5(300, 200)
        GuardHouseNo6(770, 200)
    elif cp.i == 18:
        background(255)
        loop()
        KingsPalace(800, 75)
        Main.maintext3()
    elif cp.i == 19:
        background(255)
        loop()
        Trader(775, 740)
        Main.maintext4()
    elif cp.i == 20:
        background(255)
        loop()
        Main.maintext5()
    elif cp.i == 21:
        background(255)
        Main.pretext()
