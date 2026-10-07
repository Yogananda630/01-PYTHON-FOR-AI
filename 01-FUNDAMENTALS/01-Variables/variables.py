"""
Python Variables
----------------
Fundamental examples for AI Engineering.
"""

# 1. Basic variable assignment
name = "Yogananda"
age = 21
is_learning_ai = True

print("Name:", name)
print("Age:", age)
print("Learning AI:", is_learning_ai)


# 2. Different data types
course = "Python for AI"
hours_per_day = 3
progress = 75.5
completed = False

print("\nCourse:", course)
print("Hours:", hours_per_day)
print("Progress:", progress)
print("Completed:", completed)


# 3. Multiple assignment
x, y, z = 10, 20, 30

print("\nValues:", x, y, z)


# 4. Same value to multiple variables
a = b = c = 100

print("Same values:", a, b, c)


# 5. Checking variable types
print("\nTypes:")
print(type(name))
print(type(age))
print(type(progress))
print(type(is_learning_ai))


# 6. Updating a variable
score = 10
score = score + 5

print("\nUpdated score:", score)


# 7. Variables used in a simple AI-style calculation
features = 10
samples = 1000

total_values = features * samples

print("\nAI Dataset Information")
print("Features:", features)
print("Samples:", samples)
print("Total values:", total_values)
