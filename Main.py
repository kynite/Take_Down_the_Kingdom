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
                cp.i = 1
    if mousePressed and mouseButton == LEFT:
        if mouseX > 200 and mouseX < 260:
            if mouseY > 475 and mouseY < 508:
                exit()
