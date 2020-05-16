from itertools import groupby

import occupation_info_extractor
import translator
from Enums.skill import Skill
from data import Data


class SkillFormater():

    def __init__(self):
        self.translator = translator.Translator()
        infos = occupation_info_extractor.get_infos()
        self.info = [i for i in infos if i.occupation_enum == Data.data["occupation"]][0]

    def get_occupation_skills(self):
        enum_skills_list = self.info.skills
        skills_list = []
        for lists in enum_skills_list:
            if len(lists) == 1:
                for i in lists:
                    skills_list.append(self.translator.get_translation_for_skill(i))
            elif len(lists) == len(Skill.__members__.items()):
                skills_list.append("Dowolna umiejętność")
            elif len(Skill.__members__.items()) > len(lists) > 1:
                skill_string = ""
                for i in lists[:-1]:
                    skill_string += self.translator.get_translation_for_skill(i)
                    skill_string += " lub "
                skill_string += self.translator.get_translation_for_skill(lists[-1])
                skills_list.append(skill_string)

        return skills_list


    def format_skills_list(self, skills_list):
        skill_string = ""
        grouping_skills_list = [list(j) for i, j in groupby(skills_list)]
        for i in grouping_skills_list:
            if len(i) == 1:
                skill_string += i[0] + "\n"
            else:
                num = str(len(i))
                skill_string += f"{num}x {i[0]}\n"

        return skill_string