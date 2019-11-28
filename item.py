import random

items = ['branch', 'wood shield', 'meat', 'iron axe', 'iron shield', 'bubble']

categoryL = ['Weapon', 'Armor', 'Jewels']

prices = [2, 2, 1, 5, 5, 1]

equipables = [3, 2, -1, 3, 2, -1]

powers = [1, 0, 0, 2, 0, 0]

armors = [0, 1, 0, 0, 2, 0]


class Item:

    def __init__(self, name, description, price):
        """
        :param name: "self"'s name
        :param description: "self"'s description
        :param price: "self"'s price
        """
        self.name = name
        self.description = description
        self.price = price


class Equipment(Item):
    # TODO condition sur category
    def __init__(self, name, description, price, category, mini_level, power, shield):
        super().__init__(name, description, price)
        self.type = category
        self.mini_level = mini_level
        self.power = power
        self.shield = shield
        self.dodge_chance = 0
        self.parry_chance = 0
        self.critic_chance = 0


class Consumable(Item):
    def __init__(self, name, description, price, effect):
        super().__init__(name, description, price)
        self.effect = effect
