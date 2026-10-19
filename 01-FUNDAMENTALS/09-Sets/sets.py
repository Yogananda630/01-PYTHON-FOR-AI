
# Python Sets - AI Engineer Journey

# 1. Create a set
ai_skills = {"Python", "NumPy", "Pandas", "Python"}
print("AI Skills:", ai_skills)

# 2. Remove duplicates from a dataset
data = [10, 20, 10, 30, 20, 40, 50, 30]
unique_data = set(data)
print("Original data:", data)
print("Unique data:", unique_data)

# 3. Add and remove elements
ai_skills.add("Machine Learning")
print("After adding:", ai_skills)

ai_skills.discard("NumPy")
print("After removing NumPy:", ai_skills)

# 4. Set operations
python_students = {"Ravi", "Kiran", "Yogananda"}
ai_students = {"Kiran", "Yogananda", "Arjun"}

print("All students:", python_students | ai_students)
print("Students in both groups:", python_students & ai_students)
print("Only Python students:", python_students - ai_students)
print("Students in either group, but not both:",
      python_students ^ ai_students)

# 5. Check membership
print("Is Python available?", "Python" in ai_skills)

# 6. Count unique values
print("Number of unique values:", len(unique_data))
