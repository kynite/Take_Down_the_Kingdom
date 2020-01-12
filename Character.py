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
                                 wp.sandwich, wp.sliceofpizza,
                                 wp.bottleosprite, wp.boxofpizza
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
        """Player icon"""
        fill(0, 0, 255)
        rectMode(CENTER)
        rect(self.x, self.y, 10, 10)

    def movenorth(self):
        """player movement north/up"""
        self.y += -4

    def movesouth(self):
        """player movement south/down"""
        self.y += 4

    def movewest(self):
        """player movement west/left"""
        self.x += -4

    def moveeast(self):
        """player movement east/right"""
        self.x += 4

    def showgold(self):
        """Show player health and gold on screen"""
        textSize(20)
        fill(0)
        text('{} Gold'.format(self.gold), 10, 20)
        text('{}HP'.format(self.hp), 10, 50)

    def showinventory(self):
        """
        Display each of the players items, best weapon,
        and what to press to show healing keys.
        """
        # Height of the first item shown
        y = 100
        textSize(20)
        fill(0)
        text('Best Weapon:', 10, 20)
        text('{} Damage'.format(self.most_powerful_weapon().damage), 350, 20)
        text('type [h] to show healing keys', 10, 50)
        text('Consumables:', 10, 100)
        text('{}'.format(self.most_powerful_weapon().name), 150, 20)
        text('Type q to leave', 1450, 890)
        # displays each item, each sperated by 30 spaces
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
        """Shows the key inputs to heal"""
        fill(0)
        text('type [y] to use BottleOSprite', 10, 20)
        text('type [u] to use Slice of Pizza', 10, 50)
        text('type [o] to use Sandwich', 10, 80)
        text('type [p] to use Soup', 10, 110)
        text('type [r] to use Box of Pizza', 10, 140)
        text('Type q to leave', 1450, 890)

    def fight(self, e, g):
        """Player combat with an enemy"""
        # sets the players weapon with their most powerful weapon
        bestweapon = self.most_powerful_weapon()
        # Sets the current enemy
        current_enemy = e
        # Gives the enemy an action number
        enemy_action = random(1, 3)
        # Makes the enemy action integer instead of float
        enemy_action = int(enemy_action)
        # Tells user they came in contact with the current enemy
        text('You came in combat with {}'.format(current_enemy.name), 750, 150)
        # Checks if user right clicked
        if mousePressed and mouseButton == RIGHT:
            # Checks if player and enemies health is above 0
            if self.hp > 0 and current_enemy.hp > 0:
                # Black colour
                fill(0)
                # Tells user how to continue the fight
                text('Press [c] to continue', 1200, 800)
                # Takes away enemy health by the damage players weapon does
                current_enemy.hp = current_enemy.hp - bestweapon.damage
                # no loop so player can attack one at a time
                noLoop()
                # blue color
                fill(0, 0, 255)
                # tells how much damage player did
                text('You \
attacked and dealt {} damage!'.format(bestweapon.damage), 750, 800)
                # red color
                fill(255, 0, 0)
                # tells user how much hp enemy has
                text('Enemy: {}HP'.format(current_enemy.hp), 750, 850)
                # checks if enemy random number equals 1
                if enemy_action == 1:
                    # damage the player
                    self.hp -= current_enemy.damage
                    # tell user how much damage they took
                    text('The \
enemy attacked and dealt {} damage!'.format(current_enemy.damage), 200, 800)
                    # blue color
                    fill(0, 0, 255)
                    # players health
                    text('{}HP'.format(self.hp), 200, 100)
                # checks if enemy random number equals 2
                elif enemy_action == 2:
                    # red color
                    fill(255, 0, 0)
                    # the enemy misses and does no damage
                    text('The enemy missed!', 200, 800)
            # if player health is 0 or less
            elif self.hp <= 0:
                # game exits
                print('You died')
                exit()
            # if enemy health is 0 or less
            elif current_enemy.hp <= 0:
                fill(0, 0, 255)
                # tells player who they defeated and gold earned
                print('You \
defeated {} and gained {}'.format(current_enemy.name, g))
                # add gold to player
                self.gold += g
                # sets it back to map
                cpw.i = 1
                # gives enemy original hp
                current_enemy.hp = current_enemy.originalhp

    def fightking(self):
        """
        Same code as fight() except if you win this one the game ends
        """
        bestweapon = self.most_powerful_weapon()
        current_enemy = king
        enemy_action = random(1, 3)
        enemy_action = int(enemy_action)
        text('You came in combat with {}'.format(current_enemy.name), 750, 150)
        if mousePressed and mouseButton == RIGHT:
            if self.hp > 0 and current_enemy.hp > 0:
                fill(0)
                text('Press [c] to continue', 1200, 800)
                current_enemy.hp = current_enemy.hp - bestweapon.damage
                noLoop()
                fill(0, 0, 255)
                text('You \
attacked and dealt {} damage!'.format(bestweapon.damage), 750, 800)
                fill(255, 0, 0)
                text('Enemy: {}HP'.format(current_enemy.hp), 750, 850)
                if enemy_action == 1:
                    self.hp -= current_enemy.damage
                    text('The \
enemy attacked and dealt {} damage!'.format(current_enemy.damage), 200, 800)
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
        # Check if user has enough gold and has not already purchased item
        if self.gold >= 100 and wp.spear not in self.weaponinventory:
            # Pops item from list to a single variable
            item = self.shopinventory.pop(0)
            # Adds item to player inventory
            self.weaponinventory.append(item)
            # readds the item back into the shop
            self.shopinventory.insert(0, wp.spear)
            # Takes gold from player
            self.gold -= 100
            # Brings them to purchased page
            cpw.i = 8
        # If the item is already in the inventory
        elif wp.spear in self.weaponinventory:
            # Brings them to already purchased screen
            cpw.i = 7
        # If player does not have enough gold and item
        else:
            # Brings them to insufficient funds page
            cpw.i = 6

    def buykopesh(self):
        """Purchases Kopesh if it satisfies constraits"""
        # Check if user has enough gold and has not already purchased item
        if self.gold >= 250 and wp.kopesh not in self.weaponinventory:
            # Pops item from list to a single variable
            item = self.shopinventory.pop(1)
            # Adds item to player inventory
            self.weaponinventory.append(item)
            # readds the item back into the shop
            self.shopinventory.insert(0, wp.kopesh)
            # Takes gold from player
            self.gold -= 250
            # Brings them to purchased page
            cpw.i = 8
        # If the item is already in the inventory
        elif wp.kopesh in self.weaponinventory:
            # Brings them to already purchased screen
            cpw.i = 7
        # If player does not have enough gold and item
        else:
            # Brings them to insufficient funds page
            cpw.i = 6

    def buyshovel(self):
        """Purchases Shovel if it satisfies constraits"""
        # Check if user has enough gold and has not already purchased item
        if self.gold >= 1800 and wp.shovel not in self.weaponinventory:
            # Pops item from list to a single variable
            item = self.shopinventory.pop(2)
            # Adds item to player inventory
            self.weaponinventory.append(item)
            # readds the item back into the shop
            self.shopinventory.insert(0, wp.shovel)
            # Takes gold from player
            self.gold -= 1800
            # Brings them to purchased page
            cpw.i = 8
        # If the item is already in the inventory
        elif wp.shovel in self.weaponinventory:
            # Brings them to already purchased screen
            cpw.i = 7
        # If player does not have enough gold and item
        else:
            # Brings them to insufficient funds page
            cpw.i = 6

    def buyshotel(self):
        """Purchases Shotel if it satisfies constraits"""
        # Check if user has enough gold and has not already purchased item
        if self.gold >= 5000 and wp.shotel not in self.weaponinventory:
            # Pops item from list to a single variable
            item = self.shopinventory.pop(3)
            # Adds item to player inventory
            self.weaponinventory.append(item)
            # readds the item back into the shop
            self.shopinventory.insert(0, wp.shotel)
            # Takes gold from player
            self.gold -= 5000
            # Brings them to purchased page
            cpw.i = 8
        # If the item is already in the inventory
        elif wp.shotel in self.weaponinventory:
            # Brings them to already purchased screen
            cpw.i = 7
        # If player does not have enough gold and item
        else:
            # Brings them to insufficient funds page
            cpw.i = 6

    def buyzweihander(self):
        """Purchases Zweihander if it satisfies constraits"""
        # Check if user has enough gold and has not already purchased item
        if self.gold >= 20000 and wp.zweihander not in self.weaponinventory:
            # Pops item from list to a single variable
            item = self.shopinventory.pop(4)
            # Adds item to player inventory
            self.weaponinventory.append(item)
            # readds the item back into the shop
            self.shopinventory.insert(0, wp.zweihander)
            # Takes gold from player
            self.gold -= 20000
            # Brings them to purchased page
            cpw.i = 8
        # If the item is already in the inventory
        elif wp.zweihander in self.weaponinventory:
            # Brings them to already purchased screen
            cpw.i = 7
        # If player does not have enough gold and item
        else:
            # Brings them to insufficient funds page
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
        """Tells user they don't have enough gold"""
        textSize(20)
        text('insufficient gold', 50, 50)
        text('Type q to leave', 1450, 890)

    def showtext2(self):
        """Tells user they already own the item"""
        textSize(20)
        text('You already own this item', 50, 50)
        text('Type q to leave', 1450, 890)

    def showtext3(self):
        """Tells user they bought the item"""
        textSize(20)
        text('item bought!', 50, 50)
        text('Type q to leave', 1450, 890)

    def showending(self):
        """End of the game text"""
        textSize(50)
        text('You saved your friend from the king, THE END', 10, 450)
        text('Press [ESC] to exit the game', 400, 500)

    def outofbounds(self):
        """
        Checks if player is out of bound and if they are
        then text tells them what to do to get back into the game
        """
        if player.x < 0 or player.x > 1600:
            text('You are \
out of bounds type [t] to teleport back to home', 500, 450)
        if player.y < 0 or player.y > 900:
            text('You \
are out of bounds type [t] to teleport back to home', 500, 450)


# Instance of player
player = Kytizer(1450, 750)
