import Items as wp
from Index import changingpicture as cpw
from Enemies import *


class Kytizer:
    def __init__(self, x, y):
        self.weaponinventory = [wp.kitchenknife]
        self.healinginventory = [wp.sandwich, wp.sliceofpizza, wp.sliceofpizza, wp.sliceofpizza, wp.sandwich, wp.sandwich]
        self.x = x
        self.y = y
        self.gold = 50
        self.hp = 80
        self.shopinventory = [wp.spear]
        
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
        
    def showgold(self):
        textSize(20)
        fill(0)
        text('{} Gold'.format(self.gold), 10, 20)
        text('{}HP'.format(self.hp), 10, 50)

        
    def showinventory(self):
        y = 100
        textSize(20)
        fill(0)
        text('Best Weapon:', 10, 20)
        text('type [h] to show healing keys', 10, 50)
        text('Consumables:', 10, 100)
        text('{}'.format(self.most_powerful_weapon().name), 150, 20)
        text('Type q to leave', 1450, 890)
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
    
    def sandwichheal(self):
        if wp.sandwich in self.healinginventory:
            self.hp = self.hp + wp.sandwich.healing_value
            self.healinginventory.remove(wp.sandwich)
            if self.hp > 100:
                self.hp = 100
            print('{} HP'.format(self.hp))
        else:
            print('no sandwich in inventory')

    def showhealing(self):
        fill(0)
        text('type y to use sandwich', 10, 20)
        text('Type q to leave', 1450, 890)
    
    def fight(self, e, g):
        bestweapon = self.most_powerful_weapon()
        current_enemy = e
        enemy_action = random(1, 3)
        enemy_action = int(enemy_action)
        text('You came in combat with {}'.format(current_enemy.name), 750, 150)
        if mousePressed and mouseButton == RIGHT:
            if self.hp > 0 and current_enemy.hp > 0:
                text('Press [c] to continue', 1200, 800)
                current_enemy.hp = current_enemy.hp - bestweapon.damage
                noLoop()
                fill(0, 0, 255)
                text('You attacked and dealt {} damage!'.format(bestweapon.damage), 750, 800)
                fill(255, 0, 0)
                text('Enemy: {}HP'.format(current_enemy.hp), 750, 850)
                if enemy_action == 1:
                    self.hp -= current_enemy.damage
                    text('The enemy attacked and dealt {} damage!'.format(current_enemy.damage), 200, 800)
                    fill(0, 0, 255)
                    text('{}HP'.format(self.hp), 200, 100)
                elif enemy_action == 2:
                    fill(255, 0, 0)
                    text('The enemy missed!', 200, 800)
            elif self.hp <= 0:
                print('you died')
                exit()
            elif current_enemy.hp <= 0:
                fill(0, 0, 255)
                print('you defeated {} and gained {}'.format(current_enemy.name, g))
                self.gold += g
                cpw.i = 1
                current_enemy.hp = current_enemy.originalhp

    def buyitem1(self):
        if self.gold >= 100 and wp.spear not in self.weaponinventory:
            item = self.shopinventory.pop(0)
            self.weaponinventory.append(item)
            self.shopinventory.insert(0, None)
            self.gold -= 100
            cpw.i = 8
        elif wp.spear in self.weaponinventory:
            cpw.i = 7
        else:
            cpw.i = 6
    
    def showtext1(self):
        text('insufficient gold', 50, 50)
        text('Type q to leave', 1450, 890)
    
    def showtext2(self):
        text('You already own this item', 50, 50)
        text('Type q to leave', 1450, 890)
    
    def showtext3(self):
        text('item bought!', 50, 50)
        text('Type q to leave', 1450, 890)
        
player = Kytizer(1450, 750)
