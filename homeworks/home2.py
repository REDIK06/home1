class SuperHero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.fly = False

    def attack(self):
        self.health **= 2
        self.fly = True

    def true_in_true_phrase(self):
        return "True in the True_phrase"


class AirHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


class SpaceHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


class DarkMonster(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


air_hero = AirHero("SkyMaster", 101, 21)
space_hero = SpaceHero("StellarPilot", 122, 40)
dark_monster = DarkMonster("DarkMonster", 222, 11)


air_hero.attack()
print(air_hero.fly)
print(air_hero.true_in_true_phrase())

space_hero.attack()
print(space_hero.fly)
print(space_hero.true_in_true_phrase())

dark_monster.attack()
print(dark_monster.fly)
print(dark_monster.true_in_true_phrase())
dark_monster.crit()
print(dark_monster.damage)