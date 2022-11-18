import random
import sys
from time import sleep

# dprint() prints out characters individually to terminal to simulate typing.
print_speed = 0.015
def dprint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(print_speed)

class Characters:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        self.maxhealth = 100
        self.isdead = False
    def __repr__(self):
        return 'The {name} character has {strength} attack power and {health} Health Points!'.format(name = self.name,
        strength = self.strength, health = self.health)
    def death(self):
        self.isdead = True
        if self.health != 0:
            self.health = 0
            dprint('\nThe {name} is defeated!\n\n'.format(name = self.name))
    def gain_health(self, amount):
        self.health += amount
        if self.health >= self.maxhealth:
            self.health = self.maxhealth
        return 'Your {name} now has {health} HP.'.format(self.name, self.health)
    def lose_health(self, amount):
        self.health -= amount
        if self.health == 0:
            self.death()
    def attack(self, enemy):
        while self.health > 0 and enemy.health > 0:
            enemy.lose_health(self.strength)
            sleep(1)
            dprint("\nThe {name} attacked the {enemy} for {damage} DMG!\n".format(name = self.name, enemy = enemy.name, damage = self.strength))
            if enemy.health > 0:
                self.lose_health(enemy.strength)
                dprint("\nThe {enemy} attacked your {name} for {damage} DMG!\n".format(enemy = enemy.name, name = self.name, damage = enemy.strength))
                sleep(1)
        else: 
            if self.health <= 0:
                dprint('\nYOU DIED\nGAME OVER!\n')
            elif enemy.health <= 0:
                enemy.death()

def generate_enemy():
    chance = random.randint(0, 20)
    if chance > 15 and chance < 20:
        ogre = Characters('Ogre', 8, 15)
        enemy = ogre
        sleep(1)
        dprint("\nAn ogre appears. This is a very strong foe! It has {} attack and {} HP\n".format(enemy.strength, enemy.health))
    elif chance >= 10 and chance <= 15:
        goblin = Characters('Goblin Warrior', 4, 10)
        enemy = goblin
        sleep(1)
        dprint("\nA goblin warrior appears. It has {} attack and {} HP!\n".format(enemy.strength, enemy.health))
    elif chance < 10:
        skeleton = Characters('Skeleton', 2, 8)
        enemy = skeleton
        sleep(1)
        dprint("\nA skeleton appears. This is a weak foe. It has {} attack and {} HP!\n".format(enemy.strength, enemy.health))
    elif chance == 20:
        dragon = Characters('Dragon', 50, 100)
        enemy = dragon
        sleep(1)
        dprint("\nA dragon appears! It was nice knowing you!\n")
    return enemy
# Our Heroes!
knight = Characters('Knight', 6, 20)
archer = Characters('Archer', 9, 10)
viking = Characters('Viking', 3, 40)

dprint("""
Welcome to the pit!\n
How long will you survive? \n
Who will be your hero? You may pick between a mighty knight, a cunning archer, and a brutish viking!\n\n""")
sleep(1)

print(knight)
print(archer)
print(viking)

character_choice = input("\nWhich character would you like to choose?\nType 1 for knight, 2 for archer, or 3 for viking: ")
while character_choice != '1' and character_choice != '2'  and character_choice != '3':
    character_choice = input("You did not pick a valid number.\nTry again: ")

dprint("\nInto the pit you go. Good Luck!\n\n")
sleep(3)
count = []
if character_choice == '1':
    while knight.health > 0:
        count.append(knight.attack(generate_enemy()))
elif character_choice == '2':
    while archer.health > 0:
        count.append(archer.attack(generate_enemy()))
elif character_choice == '3':
    while viking.health > 0:
        count.append(viking.attack(generate_enemy()))

sleep(1)
dprint("NUMBER OF ENEMIES SLAIN: " + str(len(count) - 1)+'\n')
