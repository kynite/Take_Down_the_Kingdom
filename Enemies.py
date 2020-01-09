class CastleGuard1():
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Immortal Castle Guard: Joey'
        # Health of the Enemy
        self.hp = 10
        # Original health of the enemy
        self.originalhp = 10
        # Damage the enemy does
        self.damage = 2


class CastleGuard2():
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Immortal Castle Guard: Robert'
        # Health of the Enemy
        self.hp = 100
        # Original health of the enemy
        self.originalhp = 100
        # Damage the enemy does
        self.damage = 5


class CastleGuard3():
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Immortal Castle Guard: Kingston'
        # Health of the Enemy
        self.hp = 300
        # Original health of the enemy
        self.originalhp = 300
        # Damage the enemy does
        self.damage = 3


class CastleGuard4():
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Immortal Castle Guardian: Zytile'
        # Health of the Enemy
        self.hp = 750
        # Original health of the enemy
        self.originalhp = 750
        # Damage the enemy does
        self.damage = 10
        
        
class CastleGuard5():
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Immortal Castle Guardian: Postie'
        # Health of the Enemy
        self.hp = 1200
        # Original health of the enemy
        self.originalhp = 750
        # Damage the enemy does
        self.damage = 12


class CastleGuard6():
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Immortal Castle Guardian: Zeke'
        # Health of the Enemy
        self.hp = 2000
        # Original health of the enemy
        self.originalhp = 2000
        # Damage the enemy does
        self.damage = 15


class King():
    """The final boss to win the game"""
    def __init__(self):
        # Name of the final boss
        self.name = 'Oden The King'
        # Health of the final boss 
        self.hp = 5000
        # Damage of the final boss
        self.damage = 20
        
        

# Instances of enemies
castle_guard1 = CastleGuard1()
castle_guard2 = CastleGuard2()
castle_guard3 = CastleGuard3()
castle_guard4 = CastleGuard4()
castle_guard5 = CastleGuard5()
castle_guard6 = CastleGuard6()
king = King()
    
