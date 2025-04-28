"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        is_alive = True
        if self.health > 0:
            is_alive = True
        else:
            is_alive = False
        return is_alive
        

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power
    
    def print_status(self):
        print("The goblin have %d health and %d power." % (self.health, self.power))


def main():

    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and hero.alive():
        #print("You have %d health and %d power." % (hero.health, hero.power))
        #print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()
