
# Python Dictionaries - AI Engineer Journey

# 1. Create a dictionary
student = {
    "name": "Yogananda",
    "goal": "AI Engineer",
    "language": "Python"
}
print("Student details:", student)

# 2. Access values
print("Name:", student["name"])
print("Career goal:", student["goal"])

# 3. Add and update values
student["github"] = "Yogananda630"
student["language"] = "Python for AI"
print("Updated details:", student)

# 4. Loop through key-value pairs
print("\nStudent profile:")
for key, value in student.items():
    print(f"{key}: {value}")

# 5. AI model information
model = {
    "model_name": "Image Classifier",
    "accuracy": 92.5,
    "status": "Passed",
    "version": 1
}

print("\nModel:", model["model_name"])
print("Accuracy:", model["accuracy"], "%")

# 6. Update model status
model["version"] = 2
model["status"] = "Updated"
print("Updated model:", model)

# 7. Safely access a missing key
print("Training time:", model.get("training_time", "Not available"))

# 8. Get all keys and values
print("Model fields:", list(model.keys()))
print("Model values:", list(model.values()))
