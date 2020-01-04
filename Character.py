import Items as wp
from Index import changingpicture as cpw


class Kytizer:
    def __init__(self, x, y):
        self.weaponinventory = [wp.kitchenknife]
        self.healinginventory = [wp.sliceofpizza, wp.sliceofpizza, wp.sliceofpizza]
        self.x = x
        self.y = y
        self.gold = 0
        self.hp = 100
        
    def playericon(self):
        fill(0, 0, 255)
        rect(self.x, self.y, 10, 10)
    
    def movenorth(self):
        self.y += -2

    def movesouth(self):
        self.y += 2

    def movewest(self):
        self.x += -2
            
    def moveeast(self):
        self.x += 2
        
    def openinventory(self):
        textSize(20)
        fill(0)
        text('Inventory', 10, 20)
        if mousePressed and mouseButton == LEFT:
            if mouseX > 10 and mouseX < 100:
                if mouseY > 5 and mouseY < 25:
                    cpw.i = 2
        
    def showinventory(self):
        y = 100
        textSize(20)
        fill(0)
        text('Best Weapon:', 10, 50)
        text('Consumables:', 10, 100)
        text('{}'.format(self.most_powerful_weapon().name), 150, 50)
        text('Backpack:', 10, 20)
        text('Leave', 1540, 890)
        for item in self.healinginventory:
            text('{}'.format(item.name), 160, y)
            y = y + 30
            noLoop()

    def most_powerful_weapon(self):
        """Determines the most damaging weapon in Players inventory"""
        # sets inital damge to 0
        max_damage = 0
        # sets the best weapon to nothing
        best_weapon = None
        # Loop for each item in inventory
        for item in self.weaponinventory:
            # Code adapted from Make Your own Python Text Based Adventure
            # tries to see if the item damage is greator than the current max
            # damage and then replaces the best weapon in inventory
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        # sends the best weapon to function
        return best_weapon
    
    def playerinteracted(self):
        # guard 1
        if self.x > 1310 and self.x < 1335:
            if self.y > 475 and self.y < 500:
                print('a')
        # guard 2
        if self.x > 785 and self.x < 820:
            if self.y > 475 and self.y < 510:
                print('b')
        # guard 3
        if self.x > 300 and self.x < 345:
            if self.y > 475 and self.y < 520:
                print('c')
        # guard 4
        if self.x > 1300 and self.x < 1350:
            if self.y > 200 and self.y < 250:
                print('d')
        # guard 5
        if self.x > 300 and self.x < 355:
            if self.y > 200 and self.y < 255:
                print('e')
        # guard 6
        if self.x > 770 and self.x < 830:
            if self.y > 200 and self.y < 260:
                print('f')
    
    def healingtime(self):
        print('type [s] for sandwich')
        while True:
            if key == "s":
                if wp.sandwich in self.healinginventory:
                    print('hello')
                else:
                    print('no sandwich in inventory')

player = Kytizer(1450, 750)
