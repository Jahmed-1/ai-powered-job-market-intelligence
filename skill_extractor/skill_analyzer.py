from collections import Counter


def count_skills(skill_lists):
    all_skills = []

    for skills in skill_lists:
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    return skill_counts