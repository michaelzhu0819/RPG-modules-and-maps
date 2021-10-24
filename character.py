""" These functions define the four characters in the game"""


def beserker(hp, damage, focus):
    hp = 100
    damage = 20
    focus = 15
    print("-beserker can do high damage when health and/or focus is low\n")


def healer(hp, damage, focus, heal_boost):
    hp = 150
    damage = 15
    focus = 16
    heal_boost = 5
    print("-healer can heal themselves every 5 rounds")


def mage(hp, damage, focus):
    hp = 80
    damage = 25
    focus = 14
    print("-mage have high damage and can have less cooldown on weapons and" +
          "healing items")


def tank(hp, damage, focus):
    hp = 200
    damage = 15
    focus = 10
    print("-tank can have +100% health as the start of the game")
