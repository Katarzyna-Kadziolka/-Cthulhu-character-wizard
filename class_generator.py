import re

from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.firearms import Firearm
from Enums.language import Language
from Enums.pilot import Pilot
from Enums.science import Science
from Enums.skill import Skill
from Enums.survival import Survival


def add_custom_skills(skills_string, info, regexr_skill, skill_class_type, specialization):
    skill_name = re.findall(f"{regexr_skill}\(([^)]+)\)", skills_string)

    if len(skill_name) > 0:
        if "any" in skill_name[0] or "Any" in skill_name[0] or "e.g." in skill_name[0] or "etc." in skill_name[0]:

            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")
            info["skills"].append([skill_class_type])

            if "two" in skill_name[0]:
                info["skills"].append([skill_class_type])
            elif "three" in skill_name[0]:
                info["skills"].append([skill_class_type])
                info["skills"].append([skill_class_type])
            elif "four" in skill_name[0]:
                info["skills"].append([skill_class_type])
                info["skills"].append([skill_class_type])
                info["skills"].append([skill_class_type])

        elif " or " in skill_name[0]:
            x = skill_name[0].split(' or ')

            list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in x]

            info["skills"].append(list_of_enums)
            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

        elif len(skill_name[0].split(',')) >= 2:
            x = skill_name[0].split(',')

            for word in x:
                word_position = x.index(word)
                x.remove(word)
                x.insert(word_position, word.strip())
            list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in x]

            info["skills"].append(list_of_enums)
            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

        elif "/" in skill_name[0]:
            skill_name[0] = skill_name[0].replace("/", "_")
            info["skills"].append([specialization[skill_name[0].replace(" ", "_").upper()]])
            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

        else:
            info["skills"].append([specialization[skill_name[0].replace(" ", "_").upper()]])
            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

    return skills_string, info



if __name__== '__main__':
    with open('Occupations.tsv', encoding="utf-8") as tsv_file:
        lines = tsv_file.readlines()
    occupation_infos=[]
    for line in lines:
        if line == lines[0]:
            continue
        info = {}
        info_list = line.split('\t')
        info["occupation_eng"] = info_list[1]
        info["occupation_pl"] = info_list[2]
        info["occupation_skills_points"] = info_list[3]
        info["min_credit_rating"] = info_list[4]
        info["max_credit_rating"] = info_list[5]

        skills_string = info_list[6]
        info["skills"] = []


        two_personal_skill = "two interpersonal skills (Charm, Fast Talk, Intimidate, or Persuade), "
        if two_personal_skill in skills_string:
            skills_string = skills_string.replace(two_personal_skill, "")
            info["skills"].append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
            info["skills"].append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if "one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade), " in skills_string:
            skills_string = skills_string.replace("one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade), ", "")
            info["skills"].append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if "one interpersonal skill (Charm, Fast Talk, Intimidate or Persuade), " in skills_string:
            skills_string = skills_string.replace("one interpersonal skill (Charm, Fast Talk, Intimidate or Persuade), ", "")
            info["skills"].append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if "one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade)" in skills_string:
            skills_string = skills_string.replace("one interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade)", "")
            info["skills"].append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])
        if ", two any (First Aid, Mechanical Repair, Other Language)" in skills_string:
            skills_string = skills_string.replace(", two any (First Aid, Mechanical Repair, Other Language)", "")
            info["skills"].append([Skill.FIRST_AID, Skill.MECHANICAL_REPAIR, Skill.OTHER_LANGUAGE])
        if ", any( Diving, Drive Automobile, Pilot , Ride)" in skills_string:
            skills_string = skills_string.replace(", any( Diving, Drive Automobile, Pilot , Ride)", "")
            info["skills"].append([Skill.DIVING, Skill.DRIVE_AUTO, Skill.PILOT, Skill.RIDE])

        skills_string, info = add_custom_skills(skills_string, info, "Art\/Craft ", Skill.ART_CRAFT, ArtCraft)
        skills_string, info = add_custom_skills(skills_string, info, "Fighting ", Skill.FIGHTING, Fighting)
        skills_string, info = add_custom_skills(skills_string, info, "Science ", Skill.SCIENCE, Science)
        skills_string, info = add_custom_skills(skills_string, info, "Other Language ", Skill.OTHER_LANGUAGE, Language)
        skills_string, info = add_custom_skills(skills_string, info, "Pilot ", Skill.PILOT, Pilot)
        skills_string, info = add_custom_skills(skills_string, info, "Firearms ", Skill.FIREARMS, Firearm)
        skills_string, info = add_custom_skills(skills_string, info, "Survival ", Skill.SURVIVAL, Survival)

        skills_list = skills_string.split(",")
        skills_list = [i for i in skills_list if i != "" and i != " "]
        for skill in skills_list:
            if " or " in skill:
                or_list_skill = skill.split(" or ")
                for i in or_list_skill:
                    if i == " Electrical":
                        info["skills"].append([Skill.ELECTRICAL_REPAIR])
                    else:
                        info["skills"].append([Skill[i.strip().replace(" ", "_").upper()]])
            else:
                skill.strip()
                if skill.strip().replace(" ", "_").upper() == "PERSONAL_SKILL":
                    enum_list = [member[1] for member in Skill.__members__.items()]
                    info["skills"].append(enum_list)
                else:
                    info["skills"].append([Skill[skill.strip().replace(" ", "_").upper()]])



        print (info["skills"])
