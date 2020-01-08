class KitchenKnife:
    def __init__(self):
        self.name = "Kitchen Knife"
        self.damage = 1


class Spear:
    def __init__(self):
        self.name = "Spear"
        self.damage = 5


class Sandwich:
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Sandwich'
        # Healing value of the consumable
        self.healing_value = 10
        # Value of food
        self.value = 100


class SliceofPizza:
    def __init__(self):
        self.name = 'Slice of Pizza'
        self.healing_value = 20
        self.value = 200



kitchenknife = KitchenKnife()
spear = Spear()

sandwich = Sandwich()
sliceofpizza = SliceofPizza()
