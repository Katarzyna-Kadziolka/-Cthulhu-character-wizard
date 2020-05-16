import re
from typing import List

import translator
from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.firearms import Firearm
from Enums.language import Language
from Enums.pilot import Pilot
from Enums.science import Science
from Enums.skill import Skill
from Enums.survival import Survival
from Enums.uncommon_skill import UncommonSkill
from occupation_info import OccupationInfo


def custom_skill_with_or(skills_string, occupation_info, regexr_skill, specialization):
    skills_list = re.findall(f"{regexr_skill}\(([^)]+)\) or (\w+)|{regexr_skill} or (\w+)+", skills_string)
    skills_list = [[skill_name for skill_name in tuples if skill_name != ""] for tuples in skills_list]

    enum_list = [member[0] for member in specialization.__members__.items()]

    if skills_list != []:
        for skills in skills_list:
            for skill in skills:
                if skill.upper() in enum_list:
                    occupation_info.skills.append([specialization[skill.replace(" ", "_").upper()]])
                else:
                    occupation_info.skills.append([Skill[skill.replace(" ", "_").upper()]])
                    skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\) or \w+)", skills_string)[0], "")

    return skills_string, occupation_info



def add_custom_skills(skills_string, occupation_info, regexr_skill, skill_class_type, specialization):
    custom_skill_name_list = re.findall(f"{regexr_skill}\(([^)]+)\)", skills_string)

    if len(custom_skill_name_list) > 0:
        for s in custom_skill_name_list:
            if "any" in s or "Any" in s or "e.g." in s or "etc." in s:

                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")
                occupation_info.skills.append([skill_class_type])

                if "two" in s:
                    occupation_info.skills.append([skill_class_type])
                elif "three" in s:
                    occupation_info.skills.append([skill_class_type])
                    occupation_info.skills.append([skill_class_type])
                elif "four" in s:
                    occupation_info.skills.append([skill_class_type])
                    occupation_info.skills.append([skill_class_type])
                    occupation_info.skills.append([skill_class_type])

            elif " or " in s:
                x = s.split(' or ')

                list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in x]

                occupation_info.skills.append(list_of_enums)
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

            elif len(s.split(',')) >= 2:
                x = s.split(',')

                for word in x:
                    word_position = x.index(word)
                    x.remove(word)
                    x.insert(word_position, word.strip())
                list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in x]

                occupation_info.skills.append(list_of_enums)
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

            elif "/" in s:
                s = s.replace("/", "_")
                occupation_info.skills.append([specialization[s.replace(" ", "_").upper()]])
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

            else:
                occupation_info.skills.append([specialization[s.replace(" ", "_").upper()]])
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

    return skills_string, occupation_info


def get_infos() -> List[OccupationInfo]:
    with open('Occupations.tsv', encoding="utf-8") as tsv_file:
        lines = tsv_file.readlines()
    occupation_infos = []
    for line in lines:
        if line == lines[0]:
            continue

        info_list = line.split('\t')

        occupation_info = OccupationInfo()
        occupation_info.occupation_enum = [key for key, value in translator.Translator.occupations.items() if value == info_list[2]][0]
        occupation_info.occupation_eng = info_list[1]
        occupation_info.occupation_pl = info_list[2]
        occupation_info.occupation_skills_points = info_list[3]
        occupation_info.min_credit_rating = info_list[4]
        occupation_info.max_credit_rating = info_list[5]

        skills_string = info_list[6]
        occupation_info.skills = []


        two_personal_skill = "two interpersonal skills (Charm, Fast Talk, Intimidate, or Persuade), "
        if two_personal_skill in skills_string:
            skills_string = skills_string.replace(two_personal_skill, "")
            occupation_info.skills.append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
            occupation_info.skills.append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if "one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade), " in skills_string:
            skills_string = skills_string.replace("one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade), ", "")
            occupation_info.skills.append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if "one interpersonal skill (Charm, Fast Talk, Intimidate or Persuade), " in skills_string:
            skills_string = skills_string.replace("one interpersonal skill (Charm, Fast Talk, Intimidate or Persuade), ", "")
            occupation_info.skills.append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if "one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade)" in skills_string:
            skills_string = skills_string.replace("one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade)", "")
            occupation_info.skills.append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if ", two any (First Aid, Mechanical Repair, Other Language)" in skills_string:
            skills_string = skills_string.replace(", two any (First Aid, Mechanical Repair, Other Language)", "")
            occupation_info.skills.append([Skill.FIRST_AID, Skill.MECHANICAL_REPAIR, Skill.OTHER_LANGUAGE])
        if ", any( Diving, Drive Automobile, Pilot , Ride)" in skills_string:
            skills_string = skills_string.replace(", any( Diving, Drive Automobile, Pilot , Ride)", "")
            occupation_info.skills.append([Skill.DIVING, Skill.DRIVE_AUTO, Skill.PILOT, Skill.RIDE])

        skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Art\/Craft ", ArtCraft)

        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Art\/Craft ", Skill.ART_CRAFT, ArtCraft)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Fighting ", Skill.FIGHTING, Fighting)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Science ", Skill.SCIENCE, Science)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Other Language ", Skill.OTHER_LANGUAGE, Language)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Pilot ", Skill.PILOT, Pilot)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Firearms ", Skill.FIREARMS, Firearm)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Survival ", Skill.SURVIVAL, Survival)
        skills_string, occupation_info = add_custom_skills(skills_string, occupation_info, "Uncommon Skill ", Skill.UNCOMMON_SKILL, UncommonSkill)

        skills_list = skills_string.split(",")
        skills_list = [i for i in skills_list if i != "" and i != " "]
        for skill in skills_list:
            if " or " in skill:
                or_list_skill = skill.split(" or ")

                for i in or_list_skill:
                    if i == "" or i == " ":
                        break
                    elif i == " Electrical":
                        occupation_info.skills.append([Skill.ELECTRICAL_REPAIR])
                    else:
                        occupation_info.skills.append([Skill[i.strip().replace(" ", "_").upper()]])
            else:
                skill.strip()
                if skill.strip().replace(" ", "_").upper() == "PERSONAL_SKILL":
                    enum_list = [member[1] for member in Skill.__members__.items()]
                    occupation_info.skills.append(enum_list)
                else:
                    occupation_info.skills.append([Skill[skill.strip().replace(" ", "_").replace(".", "").upper()]])

        occupation_infos.append(occupation_info)
    return occupation_infos