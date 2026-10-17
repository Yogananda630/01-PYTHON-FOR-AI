
# Python Lists - AI Engineer Journey

# 1. Create a list
ai_skills = ["Python", "NumPy", "Pandas", "Machine Learning"]
print("AI Skills:", ai_skills)

# 2. Access list elements
print("First skill:", ai_skills[0])
print("Last skill:", ai_skills[-1])

# 3. Add an item
ai_skills.append("Deep Learning")
print("After adding:", ai_skills)

# 4. Remove an item
ai_skills.remove("NumPy")
print("After removing:", ai_skills)

# 5. Loop through a list
print("My AI learning topics:")
for skill in ai_skills:
    print("-", skill)

# 6. Calculate dataset statistics
scores = [85, 90, 78, 95, 88]
print("Number of scores:", len(scores))
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Average score:", sum(scores) / len(scores))

# 7. List slicing
print("First three scores:", scores[:3])
