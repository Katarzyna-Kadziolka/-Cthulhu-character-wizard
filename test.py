from random_calculator import RandomCalculator
from ability import Ability

dict_of_ability = {
    Ability.STRENGTH: 20,
    Ability.SIZE: 10,
    Ability.DEXTERITY: 5,
    Ability.EDUCATION: 6
}
calculator = RandomCalculator()
x = calculator.get_all_random_abilities(70)
print (x)


