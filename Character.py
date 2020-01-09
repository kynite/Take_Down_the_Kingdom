import Items as wp
from Index import changingpicture as cpw
from Enemies import *


class Kytizer:
    """The player that the user controls"""
    def __init__(self, x, y):
        # Player weapon inventory
        self.weaponinventory = [wp.kitchenknife]
        # Player Consumable inventory
        self.healinginventory = [
                                 wp.sandwich, wp.sliceofpizza, wp.bottleosprite
                                 ]
        # Player x coordinate
        self.x = x
        # Player y coordinate
        self.y = y
        # Amount of gold player has
        self.gold = 0
        # Health of the player
        self.hp = 100
        # Inventory of the shop
        self.shopinventory = [
                              wp.spear, wp.kopesh, wp.shovel, wp.shotel,
                              wp.zweihander, wp.sandwich, wp.sliceofpizza,
                              wp.boxofpizza, wp.bottleosprite, wp.soup
                              ]
        
    def playericon(self):
        fill(0, 0, 255)
        rectMode(CENTER)
        rect(self.x, self.y, 10, 10) 
    
    def movenorth(self):
        self.y += -3

    def movesouth(self):
        self.y += 3

    def movewest(self):
        self.x += -3
            
    def moveeast(self):
        self.x += 3
        
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
        text('{} Damage'.format(self.most_powerful_weapon().damage), 350, 20)
        text('type [h] to show healing keys', 10, 50)
        text('Consumables:', 10, 100)
        text('{}'.format(self.most_powerful_weapon().name), 150, 20)
        text('Type q to leave', 1450, 890)
        for item in self.healinginventory:
            text('{} {}HP'.format(item.name, item.healing_value), 160, y)
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
        """Heals players hp for the amount Sandwich provides"""
        # Checks to see if the item is in inventory
        if wp.sandwich in self.healinginventory:
            # Adds the items healing value to player HP
            self.hp = self.hp + wp.sandwich.healing_value
            # Removes the item from the inventory
            self.healinginventory.remove(wp.sandwich)
            # If the players health goes above 100, this sets players
            # health back to 100
            if self.hp > 100:
                self.hp = 100
        # If the item is not in the inventory
        else:
            # Tells user they dont have the item
            print('no sandwich in inventory')

    def sliceofpizzaheal(self):
        """Heals players hp for the amount Slice of pizza provides"""
        # Checks to see if the item is in inventory
        if wp.sliceofpizza in self.healinginventory:
            # Adds the items healing value to player HP
            self.hp = self.hp + wp.sliceofpizza.healing_value
            # Removes the item from the inventory
            self.healinginventory.remove(wp.sliceofpizza)
            # If the players health goes above 100, this sets players
            # health back to 100
            if self.hp > 100:
                self.hp = 100
        # If the item is not in the inventory
        else:
            # Tells user they dont have the item
            print('no slice of pizza in inventory')

    def bottleospriteheal(self):
        """Heals players hp for the amount BottleOSprite provides"""
        # Checks to see if the item is in inventory
        if wp.bottleosprite in self.healinginventory:
            # Adds the items healing value to player HP
            self.hp = self.hp + wp.bottleosprite.healing_value
            # Removes the item from the inventory
            self.healinginventory.remove(wp.bottleosprite)
            # If the players health goes above 100, this sets players
            # health back to 100
            if self.hp > 100:
                self.hp = 100
        # If the item is not in the inventory
        else:
            # Tells user they dont have the item
            print('no bottleosprite in inventory')

    def boxofpizzaheal(self):
        """Heals players hp for the amount Box of Pizza provides"""
        # Checks to see if the item is in inventory
        if wp.boxofpizza in self.healinginventory:
            # Adds the items healing value to player HP
            self.hp = self.hp + wp.boxofpizza.healing_value
            # Removes the item from the inventory
            self.healinginventory.remove(wp.boxofpizza)
            # If the players health goes above 100, this sets players
            # health back to 100
            if self.hp > 100:
                self.hp = 100
        # If the item is not in the inventory
        else:
            # Tells user they dont have the item
            print('no box of pizza in inventory')

    def soupheal(self):
        """Heals players hp for the amount Soup provides"""
        # Checks to see if the item is in inventory
        if wp.soup in self.healinginventory:
            # Adds the items healing value to player HP
            self.hp = self.hp + wp.soup.healing_value
            # Removes the item from the inventory
            self.healinginventory.remove(wp.soup)
            # If the players health goes above 100, this sets players
            # health back to 100
            if self.hp > 100:
                self.hp = 100
        # If the item is not in the inventory
        else:
            # Tells user they dont have the item
            print('no soup in inventory')

    def showhealing(self):
        fill(0)
        text('type y to use BottleOSprite', 10, 20)
        text('type u to use Slice of Pizza', 10, 50)
        text('type o to use Sandwich', 10, 70)
        text('type p to use Soup', 10, 100)
        text('type L to use Box of Pizza', 10, 130)
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
                print('You died')
                exit()
            elif current_enemy.hp <= 0:
                fill(0, 0, 255)
                print('You defeated {} and gained {}'.format(current_enemy.name, g))
                self.gold += g
                cpw.i = 1
                current_enemy.hp = current_enemy.originalhp

    def fightking(self):
        bestweapon = self.most_powerful_weapon()
        current_enemy = king
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
                print('You died')
                exit()
            elif current_enemy.hp <= 0:
                cpw.i = 10

    def buyspear(self):
        """Purchases Spear if it satisfies constraits"""
        if self.gold >= 100 and wp.spear not in self.weaponinventory:
            item = self.shopinventory.pop(0)
            self.weaponinventory.append(item)
            self.gold -= 100
            cpw.i = 8
        elif wp.spear in self.weaponinventory:
            cpw.i = 7
        else:
            cpw.i = 6

    def buykopesh(self):
        """Purchases Kopesh if it satisfies constraits"""
        if self.gold >= 250 and wp.kopesh not in self.weaponinventory:
            item = self.shopinventory.pop(1)
            self.weaponinventory.append(item)
            self.gold -= 250
            cpw.i = 8
        elif wp.kopesh in self.weaponinventory:
            cpw.i = 7
        else:
            cpw.i = 6

    def buyshovel(self):
        """Purchases Shovel if it satisfies constraits"""
        if self.gold >= 1800 and wp.shovel not in self.weaponinventory:
            item = self.shopinventory.pop(2)
            self.weaponinventory.append(item)
            self.gold -= 1800
            cpw.i = 8
        elif wp.shovel in self.weaponinventory:
            cpw.i = 7
        else:
            cpw.i = 6
            
    def buyshotel(self):
        """Purchases Shotel if it satisfies constraits"""
        if self.gold >= 5000 and wp.shotel not in self.weaponinventory:
            item = self.shopinventory.pop(3)
            self.weaponinventory.append(item)
            self.gold -= 5000
            cpw.i = 8
        elif wp.shotel in self.weaponinventory:
            cpw.i = 7
        else:
            cpw.i = 6
            
    def buyzweihander(self):
        """Purchases Zweihander if it satisfies constraits"""
        if self.gold >= 20000 and wp.zweihander not in self.weaponinventory:
            item = self.shopinventory.pop(4)
            self.weaponinventory.append(item)
            self.gold -= 20000
            cpw.i = 8
        elif wp.zweihander in self.weaponinventory:
            cpw.i = 7
        else:
            cpw.i = 6
            
    def buysandwich(self):
        """Purchases Sandwich if it satisfies constraits"""
        # Checks to see if player has enough gold
        if self.gold >= 100:
            # Pops item into a single value variable
            item = self.shopinventory.pop(5)
            # Adds the item the players healing inventory
            self.healinginventory.append(item)
            # Adds the item back into the shop for purchase again
            self.shopinventory.insert(5, wp.sandwich)
            # Removes players gold
            self.gold -= 100
            # Goes to thanks for purchase page
            cpw.i = 8
        # If player does not have enough gold
        else:
            # Brings player to insufficient gold page
            cpw.i = 6

    def buysliceofpizza(self):
        """Purchases Slice of Pizza if it satisfies constraits"""
        # Checks to see if player has enough gold
        if self.gold >= 60:
            # Pops item into a single value variable
            item = self.shopinventory.pop(6)
            # Adds the item the players healing inventory
            self.healinginventory.append(item)
            # Adds the item back into the shop for purchase again
            self.shopinventory.insert(6, wp.sliceofpizza)
            # Removes players gold
            self.gold -= 60
            # Goes to thanks for purchase page
            cpw.i = 8
        # If player does not have enough gold
        else:
            # Brings player to insufficient gold page
            cpw.i = 6

    def buyboxofpizza(self):
        """Purchases Box of Pizza if it satisfies constraits"""
        # Checks to see if player has enough gold
        if self.gold >= 900:
            # Pops item into a single value variable
            item = self.shopinventory.pop(7)
            # Adds the item the players healing inventory
            self.healinginventory.append(item)
            # Adds the item back into the shop for purchase again
            self.shopinventory.insert(7, wp.boxofpizza)
            # Removes players gold
            self.gold -= 900
            # Goes to thanks for purchase page
            cpw.i = 8
        # If player does not have enough gold
        else:
            # Brings player to insufficient gold page
            cpw.i = 6

    def buybottleosprite(self):
        """Purchases BottleOSprite if it satisfies constraits"""
        # Checks to see if player has enough gold
        if self.gold >= 25:
            # Pops item into a single value variable
            item = self.shopinventory.pop(8)
            # Adds the item the players healing inventory
            self.healinginventory.append(item)
            # Adds the item back into the shop for purchase again
            self.shopinventory.insert(8, wp.bottleosprite)
            # Removes players gold
            self.gold -= 25
            # Goes to thanks for purchase page
            cpw.i = 8
        # If player does not have enough gold
        else:
            # Brings player to insufficient gold page
            cpw.i = 6

    def buysoup(self):
        """Purchases Soup if it satisfies constraits"""
        # Checks to see if player has enough gold
        if self.gold >= 300:
            # Pops item into a single value variable
            item = self.shopinventory.pop(9)
            # Adds the item the players healing inventory
            self.healinginventory.append(item)
            # Adds the item back into the shop for purchase again
            self.shopinventory.insert(9, wp.soup)
            # Removes players gold
            self.gold -= 300
            # Goes to thanks for purchase page
            cpw.i = 8
        # If player does not have enough gold
        else:
            # Brings player to insufficient gold page
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
    
    def showending(self):
        textSize(50)
        text('You saved your friend from the king, THE END', 10, 450)
        text('Press [ESC] to exit the game', 400, 500)
    
    def outofbounds(self):
        if player.x < 0 or player.x > 1600:
            text('You are out of bounds type [t] to teleport back to home', 500, 450)
        if player.y < 0 or player.y > 900:
            text('You are out of bounds type [t] to teleport back to home', 500, 450)
        
player = Kytizer(1450, 750)
