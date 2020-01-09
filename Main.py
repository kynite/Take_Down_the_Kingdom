from Index import changingpicture as cp


def mainmenu():
    textSize(32)
    fill(20, 20, 20)
    text('Take down the Kingdom', 600, 100)
    text('play', 1200, 500)
    text('quit', 200, 500)
    if mousePressed and mouseButton == LEFT:
        if mouseX > 1200 and mouseX < 1269:
            if mouseY > 470 and mouseY < 505:
                cp.i = 21
    if mousePressed and mouseButton == LEFT:
        if mouseX > 200 and mouseX < 260:
            if mouseY > 475 and mouseY < 508:
                exit()

def pretext():
    fill(0)
    text('You wake up one day and see a letter slid under your door', 100, 100)
    text('in the letter it says that your friend has broken the royal rules', 100, 140)
    text('and that he will be executed for his actions', 100, 180)
    text('your friend aparently did not bow as the king was walking by.', 100, 220)
    text('After reading that you decide that you will kill the king.', 100, 260)
    text('He is too corrupt and has too much power', 100, 300)
    text('unfortunately you have no gold and no weapons other than a kitchen knife', 100, 340)
    text('but you heared that there is a store selling weapons', 100, 380)
    text('and that you can get gold by attacking the kings guards', 100, 420)
    text('you decide that you will work your way up to take down the kingdom', 100, 460)
    text('Right click to continue', 100, 500)
    if mousePressed and mouseButton == RIGHT:
        cp.i = 16


def maintext():
    fill(0)
    text("The blue square is you 'The Player'\
 and the house is the players house, LEFT click to continue", 100, 100)
    if mousePressed and mouseButton == LEFT:
        cp.i = 17


def maintext2():
    fill(0)
    text("The red squares are enemy castles,", 400, 800)
    text('the difficulty goes from smallest-biggest,', 400, 840)
    text('which is easiest to hardest, Right click to continue', 400, 880)
    if mousePressed and mouseButton == RIGHT:
        cp.i = 18


def maintext3():
    fill(0)
    text('This is the kings castle, the final boss', 400, 400)
    text('Be prepared this is a hard battle', 400, 440)
    text('LEFT click to continue', 400, 480)
    if mousePressed and mouseButton == LEFT:
        cp.i = 19   


def maintext4():
    fill(0)
    text('This is the store, you can buy healing items', 100, 100)
    text('and weapons from here as long as you have enough gold', 100, 140)
    text('RIGHT click to continue', 100, 180)
    if mousePressed and mouseButton == RIGHT:
        cp.i = 20

def maintext5():
    fill(0)
    text('use [WASD] to move, and press [i] to view inventory', 100, 100)
    text('HAVE FUN :)', 100, 140)
    text('LEFT click to continue', 100, 180)
    if mousePressed and mouseButton == LEFT:
        cp.i = 1
