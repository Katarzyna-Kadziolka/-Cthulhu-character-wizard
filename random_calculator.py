import math
import random

from Enums.ability import Ability
from database import Database


class RandomCalculator:

    def __init__(self):
        self.database = Database()

#personal_data_window
    def get_random_gender(self):
        gender = ["male", "female"]
        return random.choice(gender)

    def get_random_name(self, gender):
        if gender == "male":
            return random.choice(self.database.get_male_name_list())
        if gender == "female":
            return random.choice(self.database.get_female_name_list())

    def get_surname(self):
        return random.choice(self.database.get_surname_list())

    def get_age(self):
        return random.randint(15, 100)

#abilities_window
    def half_value (self, num):
        result = math.floor(num/2)
        return result

    def one_fifth (self, num):
        result = math.floor(num/5)
        return result

    def calculate_ability(self, dice: int) -> int:
        if dice == 2:
            random_value = (random.randint(1, 6) + random.randint(1, 6) + 6) * 5
        elif dice == 3:
            random_value = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 5
        else:
            raise ValueError

        return random_value

    def calculate_age_impact(self, age: int, ability: Ability, value: int):
        if ability == Ability.STRENGTH:
            if age <= 19:
                return value - 5
            elif 40 <= age <= 49:
                return value - 5
            elif 50 <= age <= 59:
                return value - 10
            elif 60 <= age <= 69:
                return value - 20
            elif 70 <= age <= 79:
                return value - 40
            elif age >= 80:
                return value - 80
            else:
                return value
        elif ability == Ability.CONDITION:
            if 40 <= age <= 49:
                return value - 5
            elif 50 <= age <= 59:
                return value - 10
            elif 60 <= age <= 69:
                return value - 20
            elif 70 <= age <= 79:
                return value - 40
            elif age >= 80:
                return value - 80
            else:
                return value
        elif ability == Ability.SIZE:
            if age <= 19:
                return value - 5
            else:
                return value
        elif ability == Ability.DEXTERITY:
            if 40 <= age <= 49:
                return value - 5
            elif 50 <= age <= 59:
                return value - 10
            elif 60 <= age <= 69:
                return value - 20
            elif 70 <= age <= 79:
                return value - 40
            elif age >= 80:
                return value - 80
            else:
                return value
        elif ability == Ability.APPEARANCE:
            if 40 <= age <= 49:
                return value - 5
            elif 50 <= age <= 59:
                return value - 10
            elif 60 <= age <= 69:
                return value - 15
            elif 70 <= age <= 79:
                return value - 20
            elif age >= 80:
                return value - 25
            else:
                return value
        elif ability == Ability.INTELLIGENCE or ability == Ability.POWER:
            return value
        elif ability == Ability.EDUCATION:
            if age <= 19:
                return value - 5
            elif 20 <= age <= 39:
                return self.make_improvement_check(value)
            elif 40 <= age <= 49:
                return self.make_multiple_improvement_checks(value, 2)
            elif 50 <= age <= 59:
                return self.make_multiple_improvement_checks(value, 3)
            elif age >= 60:
                return self.make_multiple_improvement_checks(value, 4)
        elif ability == Ability.LUCK:
            if age <= 19:
                second_roll = self.calculate_ability(2)
                if second_roll > value:
                    return second_roll
                else:
                    return value
        else:
            raise ValueError("Ability not supported")

    def make_improvement_check(self, value: int) -> int:
        roll_d100 = random.randint(1, 100)
        if roll_d100 > value:
            roll_d10 = random.randint(1, 10)
            if value + roll_d10 <= 99:
                return value + roll_d10
            else:
                return 99
        else:
            return value

    def make_multiple_improvement_checks(self, value: int, number_of_improvement_checks: int) -> int:
        for _ in range(number_of_improvement_checks):
            value = self.make_improvement_check(value)
        return value

    def deduct_points_among_abilities(self, points: int, abilities: dict):
        for i in abilities.values():
            if type(i) is not int:
                raise TypeError("Value should be int")
            if i <= 0:
                raise ValueError("Value should be more than 0")
        if sum(dict.values(abilities)) >= points + len(abilities):
            while points > 0:
                key = random.choice(list(abilities))
                if abilities[key] - 1 >= 1:
                    abilities[key] = abilities[key] - 1
                    points -= 1
        else:
            raise ValueError("The values given are too small")

        return abilities

    def calculate_all_age_impact(self, age: int, abilities):
        if age <=19:
            short_list_of_abilities = {
                Ability.STRENGTH: abilities[Ability.STRENGTH],
                Ability.SIZE: abilities[Ability.SIZE]
            }
            abilities.update(self.deduct_points_among_abilities(5, short_list_of_abilities))
            abilities[Ability.EDUCATION] = self.calculate_age_impact(age, Ability.EDUCATION, abilities[Ability.EDUCATION])

        elif 20 <= age <= 39:
            abilities[Ability.EDUCATION] = self.make_multiple_improvement_checks(abilities[Ability.EDUCATION], 1)

        elif 40 <= age <= 49:
            abilities[Ability.EDUCATION] = self.make_multiple_improvement_checks(abilities[Ability.EDUCATION], 2)
            abilities[Ability.APPEARANCE] = self.calculate_age_impact(age, Ability.APPEARANCE,
                                                                     abilities[Ability.APPEARANCE])
            short_list_of_abilities = {
                Ability.STRENGTH: abilities[Ability.STRENGTH],
                Ability.CONDITION: abilities[Ability.CONDITION],
                Ability.DEXTERITY: abilities[Ability.DEXTERITY]
            }
            abilities.update(self.deduct_points_among_abilities(5, short_list_of_abilities))

        elif 50 <= age <= 59:
            abilities[Ability.EDUCATION] = self.make_multiple_improvement_checks(abilities[Ability.EDUCATION], 3)
            abilities[Ability.APPEARANCE] = self.calculate_age_impact(age, Ability.APPEARANCE,
                                                                      abilities[Ability.APPEARANCE])
            short_list_of_abilities = {
                Ability.STRENGTH: abilities[Ability.STRENGTH],
                Ability.CONDITION: abilities[Ability.CONDITION],
                Ability.DEXTERITY: abilities[Ability.DEXTERITY]
            }
            abilities.update(self.deduct_points_among_abilities(10, short_list_of_abilities))

        elif 60 <= age <= 69:
            abilities[Ability.EDUCATION] = self.make_multiple_improvement_checks(abilities[Ability.EDUCATION], 4)
            abilities[Ability.APPEARANCE] = self.calculate_age_impact(age, Ability.APPEARANCE,
                                                                      abilities[Ability.APPEARANCE])
            short_list_of_abilities = {
                Ability.STRENGTH: abilities[Ability.STRENGTH],
                Ability.CONDITION: abilities[Ability.CONDITION],
                Ability.DEXTERITY: abilities[Ability.DEXTERITY]
            }
            abilities.update(self.deduct_points_among_abilities(15, short_list_of_abilities))

        elif 70 <= age <= 79:
            abilities[Ability.EDUCATION] = self.make_multiple_improvement_checks(abilities[Ability.EDUCATION], 4)
            abilities[Ability.APPEARANCE] = self.calculate_age_impact(age, Ability.APPEARANCE,
                                                                      abilities[Ability.APPEARANCE])
            short_list_of_abilities = {
                Ability.STRENGTH: abilities[Ability.STRENGTH],
                Ability.CONDITION: abilities[Ability.CONDITION],
                Ability.DEXTERITY: abilities[Ability.DEXTERITY]
            }
            abilities.update(self.deduct_points_among_abilities(40, short_list_of_abilities))

        elif age >= 80:
            abilities[Ability.EDUCATION] = self.make_multiple_improvement_checks(abilities[Ability.EDUCATION], 4)
            abilities[Ability.APPEARANCE] = self.calculate_age_impact(age, Ability.APPEARANCE,
                                                                      abilities[Ability.APPEARANCE])
            short_list_of_abilities = {
                Ability.STRENGTH: abilities[Ability.STRENGTH],
                Ability.CONDITION: abilities[Ability.CONDITION],
                Ability.DEXTERITY: abilities[Ability.DEXTERITY]
            }
            abilities.update(self.deduct_points_among_abilities(80, short_list_of_abilities))

        return abilities

    def get_all_random_abilities(self, age):
        abilities = {
            Ability.STRENGTH: self.calculate_ability(3),
            Ability.DEXTERITY: self.calculate_ability(3),
            Ability.CONDITION: self.calculate_ability(3),
            Ability.SIZE: self.calculate_ability(2),
            Ability.APPEARANCE: self.calculate_ability(3),
            Ability.EDUCATION: self.calculate_ability(2),
            Ability.INTELLIGENCE: self.calculate_ability(2),
            Ability.POWER: self.calculate_ability(3),
            Ability.LUCK: self.calculate_ability(2)
        }
        return self.calculate_all_age_impact(age, abilities)

#other_abilities_window

    def get_move_rate(self, strength: int, dexterity: int, size: int, age: int) ->int:

        move_rate = 0

        if strength < size and dexterity < size:
            move_rate = 7
        elif (strength == size == dexterity) or (strength >= size > dexterity) or (dexterity >= size > strength):
            move_rate = 8
        elif strength > size and dexterity > size:
            move_rate = 9

        if age <= 39:
            return move_rate
        elif 40 <= age <= 49:
            return move_rate - 1
        elif 50 <= age <= 59:
            return move_rate - 2
        elif 60 <= age <= 69:
            return move_rate - 3
        elif 70 <= age <= 79:
            return move_rate - 4
        elif age >= 80:
            return move_rate - 5

    def get_hp(self, size, condition):
        hp = math.floor((size + condition)/10)
        return hp

    def get_sanity(self, power):
        return power

    def get_magic_points(self, power):
        return self.one_fifth(power)

    def get_build(self, strength, size):
        build = 0
        if 2 <= strength + size <= 64:
            build = -2
        elif 65 <= strength + size <= 84:
            build = -1
        elif 85 <= strength + size <= 124:
            build = 0
        elif 125 <= strength + size <= 164:
            build = 1
        elif 165 <= strength + size <= 204:
            build = 2
        return build

    def get_damage_bonus(self, strength, size):
        damage_bonus = None
        if 2 <= strength + size <= 64:
            damage_bonus = -2
        elif 65 <= strength + size <= 84:
            damage_bonus = -1
        elif 85 <= strength + size <= 124:
            damage_bonus = 0
        elif 125 <= strength + size <= 164:
            damage_bonus = "+1D4"
        elif 165 <= strength + size <= 204:
            damage_bonus = "+1D6"
        return damage_bonus