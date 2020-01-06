import Items as wp
from Index import changingpicture as cpw


class Kytizer:
    def __init__(self, x, y):
        self.weaponinventory = [wp.kitchenknife]
        self.healinginventory = [wp.sandwich, wp.sliceofpizza, wp.sliceofpizza, wp.sliceofpizza, wp.sandwich, wp.sandwich]
        self.x = x
        self.y = y
        self.gold = 0
        self.hp = 80
        
    def playericon(self):
        fill(0, 0, 255)
        rectMode(CENTER)
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
    
    def healingtime(self):
        if wp.sandwich in self.healinginventory:
            self.hp = self.hp + wp.sandwich.healing_value
            self.healinginventory.remove(wp.sandwich)
            if self.hp > 100:
                self.hp = 100
            print('{} HP'.format(self.hp))
        else:
            print('no sandwich in inventory')

    def showhealing(self):
        print('type y to use sandwich')
    
    def fight(self, e, g):
        bestweapon = self.most_powerful_weapon()
        current_enemy = e
        while self.hp > 0 and current_enemy.hp > 0:
            enemy_action = random(1, 2)
            enemy_action = int(enemy_action)
            if mousePressed and mouseButton == LEFT:
                current_enemy.hp -= bestweapon.damage
                print(current_enemy.hp)
                if enemy_action == 1:
                    self.hp -= current_enemy.damage
                    print(self.hp)
                elif enemy_action == 2:
                    pass
        

player = Kytizer(1450, 750)
