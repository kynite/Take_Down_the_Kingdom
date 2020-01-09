class KingsPalace:
    def __init__(self, x, y):
        fill(234)
        rectMode(CENTER)
        # Big Castle
        rect(x, y, 100, 100)
        rectMode(CORNER)
        fill(0)
        # Door
        rect(x - 5, y + 30, 10, 19)
        

class PlayerHouse:
    def __init__(self, x, y):
        # Rectangle of Player house
        fill(186, 164, 138)
        rect(x, y, 20, 20)
        # Roof of house
        fill(14, 100, 237)
        triangle(x, y, x + 20, y, x + 10, y - 10)


class Trader:
    def __init__(self, x, y):
        fill(0, 255, 0)
        rect(x, y, 40, 40)


class GuardHouseNo1:
    def __init__(self, x, y):
        fill(255, 0, 0)
        rect(x, y, 25, 25)
        
        
class GuardHouseNo2:
    def __init__(self, x, y):
        rect(x, y, 35, 35)


class GuardHouseNo3:
    def __init__(self, x, y):
        fill(255, 0, 0)
        rect(x, y, 45, 45)


class GuardHouseNo4:
    def __init__(self, x, y):
        fill(255, 0, 0)
        rect(x, y, 50, 50)


class GuardHouseNo5:
    def __init__(self, x, y):
        fill(255, 0, 0)
        rect(x, y, 65, 65)
        

class GuardHouseNo6:
    def __init__(self, x, y):
        fill(255, 0, 0)
        rect(x, y, 80, 80)
