from Character import *
from MovingPlayer import *
import Main
from Index import changingpicture as cp
from World import *
import WorldInteraction as wi

def setup():
    size(1600, 900)
    background(255)

def keyPressed():
    if key == 'w':
        loop()
        player.movenorth()
    if key == 's':
        loop()
        player.movesouth()
    if key == 'a':
        loop()
        player.movewest()
    if key == 'd':
        loop()
        player.moveeast()
    if key == "i":
        loop()
        cpw.i = 2
    if key == 'q':
        redraw()
        cpw.i = 1
    if key == 'h':
        redraw()
        cpw.i = 3
    if key == 'y':
        player.sandwichheal()
    if key == 'c':
        loop()


def draw():
    if cp.i == 0:
        Main.mainmenu()
    elif cp.i == 1:
        background(255)
        fill(0)
        text('Use [WASD] to move', 1400, 890)
        text('Type [i] to open Inventory', 1350, 870)
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

        
