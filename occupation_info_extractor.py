import re
from typing import List

import skills_info
import translator
from Enums import language
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

    or_skill_list = []
    if skills_list != []:
        for skills in skills_list:
            for skill in skills:
                if skill.upper() in enum_list:
                    or_skill_list.append(specialization[skill.replace(" ", "_").upper()])
                else:
                    or_skill_list.append(Skill[skill.replace(" ", "_").upper()])
                    skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\) or \w+)", skills_string)[0], "")

    occupation_info.skills.append(or_skill_list)
    return skills_string, occupation_info

def add_custum_skills_with_or(skills_string, occupation_info):
    regex_find = re.findall("(\w+) \(([^)]+)\) or (\w+) \(([^)]+)\)", skills_string)
    regex_find = [[regex_find for regex_find in tuples if regex_find != ""] for tuples in regex_find]

    or_skill_list = []
    if len(regex_find) > 0:
        skills_list = regex_find[0]

        enum_1 = skills_info.SkillsInfo.enums_dict[skills_list[0]]
        member_1 = skills_list[1].upper()
        skill_1 = enum_1[member_1]
        or_skill_list.append(skill_1)

        enum_2 = skills_info.SkillsInfo.enums_dict[skills_list[2]]
        member_2 = skills_list[3].upper()
        skill_2 = enum_2[member_2]
        or_skill_list.append(skill_2)

        string_to_remove = re.findall("((\w+) \(([^)]+)\) or (\w+) \(([^)]+)\))", skills_string)[0]
        string_to_remove = str([i for i in string_to_remove][0])
        skills_string = skills_string.replace(string_to_remove, "")
        occupation_info.skills.append(or_skill_list)

    return skills_string, occupation_info

def add_custom_skills(skills_string, occupation_info, regexr_skill, skill_class_type, specialization):
    custom_skill_name_list = re.findall(f"{regexr_skill}\(([^)]+)\)", skills_string)

    if len(custom_skill_name_list) > 0:
        for custom_skill_name in custom_skill_name_list:

            if "Botany" not in custom_skill_name and "any" in custom_skill_name or "Any" in custom_skill_name or "e.g." in custom_skill_name or "etc." in custom_skill_name:

                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")
                occupation_info.skills.append([skill_class_type])

                if "two" in custom_skill_name:
                    occupation_info.skills.append([skill_class_type])
                elif "three" in custom_skill_name:
                    occupation_info.skills.append([skill_class_type])
                    occupation_info.skills.append([skill_class_type])
                elif "four" in custom_skill_name:
                    occupation_info.skills.append([skill_class_type])
                    occupation_info.skills.append([skill_class_type])
                    occupation_info.skills.append([skill_class_type])

            elif " or " in custom_skill_name:
                custom_skill_name_list = custom_skill_name.split(' or ')

                list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in custom_skill_name_list]

                occupation_info.skills.append(list_of_enums)
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

            elif len(custom_skill_name.split(',')) >= 2:
                custom_skill_name_list = custom_skill_name.split(',')

                for word in custom_skill_name_list:
                    word_position = custom_skill_name_list.index(word)
                    custom_skill_name_list.remove(word)
                    custom_skill_name_list.insert(word_position, word.strip())
                list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in custom_skill_name_list]

                occupation_info.skills.append(list_of_enums)
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

            elif "/" in custom_skill_name:
                custom_skill_name = custom_skill_name.replace("/", "_")
                occupation_info.skills.append([specialization[custom_skill_name.replace(" ", "_").upper()]])
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

            else:
                occupation_info.skills.append([specialization[custom_skill_name.replace(" ", "_").upper()]])
                skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

    return skills_string, occupation_info


def add_skill_or_custom_skill_or(skills_string, occupation_info):
    skills_list = re.findall("(\w+ \w+|\w+) or (\w+) \(([^)]+)\)", skills_string)
    if len(skills_list)>0:
        skills_list = list(skills_list[0])
        enums_list = []
        normal_skill = skills_list[0].replace(" ", "_").upper()
        enum_normal_skill = Skill[normal_skill]
        enums_list.append(enum_normal_skill)

        custom_skill = skills_list[2].split(" or ")
        custom_skill = [skill.replace(" ", "_").upper() for skill in custom_skill]
        enum = skills_info.SkillsInfo.enums_dict[skills_list[1]]
        enum_custom_skill = [enum[skill] for skill in custom_skill]
        enums_list.append(enum_custom_skill[0])
        enums_list.append(enum_custom_skill[1])

        occupation_info.skills.append(enums_list)
        skills_string = skills_string.replace((re.findall("((\w+ \w+|\w+) or (\w+) \(([^)]+)\))", skills_string))[0][0], "")

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
            enums_list = [member[1] for member in language.Language.__members__.items()]
            enums_list.append(Skill.FIRST_AID)
            enums_list.append(Skill.MECHANICAL_REPAIR)
            occupation_info.skills.append(enums_list)
            occupation_info.skills.append(enums_list)
        if ", any( Diving, Drive Automobile, Pilot , Ride)" in skills_string:
            skills_string = skills_string.replace(", any( Diving, Drive Automobile, Pilot , Ride)", "")
            occupation_info.skills.append([Skill.DIVING, Skill.DRIVE_AUTO, Skill.PILOT, Skill.RIDE])

        skills_string, occupation_info = add_skill_or_custom_skill_or(skills_string, occupation_info)

        skills_string, occupation_info = add_custum_skills_with_or(skills_string, occupation_info)

        skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Art\/Craft ", ArtCraft)
        # skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Fighting ", Fighting)
        # skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Science ", Science)
        skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Other Language ", Language)
        # skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Pilot ", Pilot)
        # skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Firearms ", Firearm)
        # skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Survival ", Survival)
        # skills_string, occupation_info = custom_skill_with_or(skills_string, occupation_info, "Uncommon Skill ", UncommonSkill)

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
                or_list_skill_string = skill.split(" or ")
                or_list_skill = []

                for i in or_list_skill_string:
                    if i == "" or i == " ":
                        break
                    elif i == " Electrical":
                        or_list_skill.append(Skill.ELECTRICAL_REPAIR)
                    else:
                        or_list_skill.append(Skill[i.strip().replace(" ", "_").upper()])

                occupation_info.skills.append(or_list_skill)
            else:
                skill.strip()
                if skill.strip().replace(" ", "_").upper() == "PERSONAL_SKILL":
                    enum_list = [member[1] for member in Skill.__members__.items()]
                    occupation_info.skills.append(enum_list)
                else:
                    occupation_info.skills.append([Skill[skill.strip().replace(" ", "_").replace(".", "").upper()]])

        occupation_infos.append(occupation_info)
    return occupation_infos