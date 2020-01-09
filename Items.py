class KitchenKnife:
    """A weapon the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = "Kitchen Knife"
        # Damage the weapon does
        self.damage = 1


class Spear:
    """A weapon the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = "Spear"
        # Damage the weapon does
        self.damage = 5


class Kopesh:
    """A weapon the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = "Kopesh"
        # Damage the weapon does
        self.damage = 20


class Shovel:
    """A weapon the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = "Shovel"
        # Damage the weapon does
        self.damage = 80


class Shotel:
    """A weapon the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = "Shotel"
        # Damage the weapon does
        self.damage = 250


class Zweihander:
    """A weapon the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = "Zweihander"
        # Damage the weapon does
        self.damage = 1000


class Sandwich:
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Sandwich'
        # Healing value of the consumable
        self.healing_value = 10


class SliceofPizza:
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Slice of Pizza'
        # Healing value of the consumable
        self.healing_value = 5


class BoxofPizza:
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Box of Pizza'
        # Healing value of the consumable
        self.healing_value = 100



class BottleOSprite:
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Bottle O Sprite'
        # Healing value of the consumable
        self.healing_value = 3


class Soup:
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Soup'
        # Healing value of the consumable
        self.healing_value = 35



# Weapon instances
kitchenknife = KitchenKnife()
spear = Spear()
kopesh = Kopesh()
shovel = Shovel()
shotel = Shotel()
zweihander = Zweihander()

# Consumable instances
sandwich = Sandwich()
sliceofpizza = SliceofPizza()
boxofpizza = BoxofPizza()
bottleosprite = BottleOSprite()
soup = Soup()
