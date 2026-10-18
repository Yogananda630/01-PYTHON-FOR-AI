
# Python Tuples - AI Engineer Journey

# 1. Create a tuple
ai_skills = ("Python", "NumPy", "Pandas", "Machine Learning")
print("AI Skills:", ai_skills)

# 2. Access tuple elements
print("First skill:", ai_skills[0])
print("Last skill:", ai_skills[-1])

# 3. Tuple length
print("Total skills:", len(ai_skills))

# 4. Loop through a tuple
print("\nMy AI learning roadmap:")
for skill in ai_skills:
    print("-", skill)

# 5. Tuple containing dataset values
model_scores = (85, 90, 78, 95, 88)
print("\nModel scores:", model_scores)
print("Highest score:", max(model_scores))
print("Lowest score:", min(model_scores))
print("Average score:", sum(model_scores) / len(model_scores))

# 6. Tuple unpacking
name, accuracy, status = ("AI Model", 92.5, "Passed")
print("\nModel name:", name)
print("Accuracy:", accuracy, "%")
print("Status:", status)

# 7. Count and index
numbers = (10, 20, 10, 30, 10)
print("\nCount of 10:", numbers.count(10))
print("Index of 20:", numbers.index(20))
