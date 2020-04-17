import re

from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.skill import Skill

def add_custom_skills(skills_string, info, regexr_skill, skill_class_type, specialization):
    skill_name = re.findall(f"{regexr_skill}\(([^)]+)\)", skills_string)
#ZUO
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
            #x=["Acting ", "Art"]
            list_of_enums = [specialization[z.replace(" ", "_").upper()] for z in x]

            info["skills"].append(list_of_enums)
            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")

        else:
            info["skills"].append([specialization[skill_name[0].replace(" ", "_").upper()]])
            skills_string = skills_string.replace(re.findall(f"({regexr_skill}\([^)]+\))", skills_string)[0], "")
#to wybuchnie XD
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
        if "One interpersonal skill (Charm, Fast Talk, Intimidate or Persuade), " in skills_string:
            skills_string = skills_string.replace("One interpersonal skill (Charm, Fast Talk, Intimidate, or Persuade), ", "")
            info["skills"].append([Skill.CHARM, Skill.FAST_TALK, Skill.INTIMIDATE, Skill.PERSUADE])

        skills_string, info = add_custom_skills(skills_string, info, "Art\/Craft ", Skill.ART_CRAFT, ArtCraft)
        skills_string, info = add_custom_skills(skills_string, info, "Fighting ", Skill.FIGHTING, Fighting)
