class Home:
    def new(self, value):
        try:
            int_value = int(value)
        except ValueError:
            raise ValueError("Аргумент может быть только целым числом")


class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(f"Имя героя: {self.name}")

    def increases_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    location = 'air'
    damage = 99
    fly = False

    def increases_health(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self):
        return "True in the True_phrase"


class EarthHero(SuperHero):
    location = 'earth'
    damage = 100
    fly = False

    def increases_health(self):
        self.health_points **= 2
        self.fly = True


    def true_in_true_phrase(self):
        return "True in the True_phrase"


class Villain(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, damage):
        self.health_points **= damage


air_hero = AirHero("Кактус",
                 "Котлетка",
                 "Бионавигация",
                 100,
                 "Я вернусь!")

earth_hero = EarthHero("Васька",
                       "Кот в сапогах",
                       "зашита дома ",
                       9,
                       "всегда готов спать!")

villain = Villain("Чабачёк",
                  "Анчоус",
                  "задыхаться",
                  1,
                  "Поймали съели!")

air_hero.increases_health()
earth_hero.increases_health()
villain.increases_health()

print(air_hero.fly)
print(earth_hero.fly)
print(villain.fly)

air_hero.true_in_true_phrase()
earth_hero.true_in_true_phrase()
villain.true_in_true_phrase()

villain.crit(3)
print(villain.health_points)