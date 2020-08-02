import math
import random
import re

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
        calculated_value = value
        if ability == Ability.STRENGTH:
            if age <= 19:
                calculated_value = value - 5
            elif 40 <= age <= 49:
                calculated_value = value - 5
            elif 50 <= age <= 59:
                calculated_value = value - 10
            elif 60 <= age <= 69:
                calculated_value = value - 20
            elif 70 <= age <= 79:
                calculated_value = value - 40
            elif age >= 80:
                calculated_value = value - 80
            else:
                calculated_value = value
        elif ability == Ability.CONDITION:
            if 40 <= age <= 49:
                calculated_value = value - 5
            elif 50 <= age <= 59:
                calculated_value = value - 10
            elif 60 <= age <= 69:
                calculated_value = value - 20
            elif 70 <= age <= 79:
                calculated_value = value - 40
            elif age >= 80:
                calculated_value = value - 80
            else:
                calculated_value = value
        elif ability == Ability.SIZE:
            if age <= 19:
                calculated_value = value - 5
            else:
                calculated_value = value
        elif ability == Ability.DEXTERITY:
            if 40 <= age <= 49:
                calculated_value = value - 5
            elif 50 <= age <= 59:
                calculated_value = value - 10
            elif 60 <= age <= 69:
                calculated_value = value - 20
            elif 70 <= age <= 79:
                calculated_value = value - 40
            elif age >= 80:
                calculated_value = value - 80
            else:
                calculated_value = value
        elif ability == Ability.APPEARANCE:
            if 40 <= age <= 49:
                calculated_value = value - 5
            elif 50 <= age <= 59:
                calculated_value = value - 10
            elif 60 <= age <= 69:
                calculated_value = value - 15
            elif 70 <= age <= 79:
                calculated_value = value - 20
            elif age >= 80:
                calculated_value = value - 25
            else:
                calculated_value = value
        elif ability == Ability.INTELLIGENCE or ability == Ability.POWER:
            calculated_value = value
        elif ability == Ability.EDUCATION:
            if age <= 19:
                calculated_value = value - 5
            elif 20 <= age <= 39:
                calculated_value = self.make_improvement_check(value)
            elif 40 <= age <= 49:
                calculated_value = self.make_multiple_improvement_checks(value, 2)
            elif 50 <= age <= 59:
                calculated_value = self.make_multiple_improvement_checks(value, 3)
            elif age >= 60:
                calculated_value = self.make_multiple_improvement_checks(value, 4)
        elif ability == Ability.LUCK:
            if age <= 19:
                second_roll = self.calculate_ability(2)
                if second_roll > value:
                    calculated_value = second_roll
                else:
                    calculated_value = value
        else:
            raise ValueError("Ability not supported")

        return max(calculated_value, 1)

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

#occupation_select_window

    def get_occupation_skills_points(self, occupation_points_formula: str, abilities: dict):
        short_ability_dict = {
            "EDU": Ability.EDUCATION,
            "DEX": Ability.DEXTERITY,
            "APP": Ability.APPEARANCE,
            "STR": Ability.STRENGTH,
            "POW": Ability.POWER
        }

        occupation_skills_points = 0
        matches = re.findall("([A-z][A-z][A-z]) *[×x] (\d)", occupation_points_formula)
        tuple_EDU = matches[0]
        occupation_skills_points += abilities[short_ability_dict[tuple_EDU[0]]] * int(tuple_EDU[1])
        occupation_skills_points += max([abilities[short_ability_dict[i[0]]] * int(i[1]) for i in matches[1:]] if matches[1:] else [0])

        return occupation_skills_points

    def get_intelligence_skill_points(self, intelligence_points: int) -> int:
        return intelligence_points*2

# occupation_skills_window
    def get_random_skills_points(self, base_skill_points: int, skill_dict: dict, type_base_points):

        # choose specialization
        if type_base_points == "occupation_skill_points":
            specialization = random.choice(list(skill_dict.keys()))
            specialization_points = random.choice([70, 75, 80])
            if max(skill_dict.values()) < specialization_points:
                if skill_dict[specialization] > specialization_points:
                    specialization = random.choice(list(skill_dict.keys()))
                if base_skill_points < specialization_points:
                    skill_dict[specialization] = skill_dict[specialization] + base_skill_points
                    return skill_dict
                up_to_specialization = (specialization_points - skill_dict[specialization] % specialization_points)
                skill_dict[specialization] = skill_dict[specialization] + up_to_specialization
                base_skill_points = base_skill_points - up_to_specialization

        # up to five skill points
        for key in skill_dict:
            current_points = skill_dict[key]
            up_to_five = 5 - current_points % 5
            if up_to_five == 5:
                continue
            if base_skill_points - up_to_five < 0:
                current_points = current_points + base_skill_points
                skill_dict[key] = current_points
                return skill_dict
            base_skill_points = base_skill_points - up_to_five
            skill_dict[key] = current_points + up_to_five

        while base_skill_points >= 5:
            skill = random.choice(list(skill_dict.keys()))
            if skill_dict[skill] == 99:
                continue
            elif 99 > skill_dict[skill] >= 95:
                base_skill_points -= (99 - skill_dict[skill])
                skill_dict[skill] = 99
            elif skill_dict[skill] < 95:
                skill_dict[skill] = skill_dict[skill] + 5
                base_skill_points -= 5

        if base_skill_points > 0:
            the_lowest_point_value = min(list(skill_dict.values()))
            skill_with_the_lowest_point_value = [key for key in skill_dict if skill_dict[key] == the_lowest_point_value][0]
            skill_dict[skill_with_the_lowest_point_value] = skill_dict[skill_with_the_lowest_point_value] + base_skill_points

        return skill_dict



