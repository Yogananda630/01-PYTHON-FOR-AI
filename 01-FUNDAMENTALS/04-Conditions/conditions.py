"""
Python Conditions
-----------------
Learn decision-making with if, elif, and else.
"""

# 1. Simple if statement
age = 21

if age >= 18:
    print("You are an adult.")


# 2. if-else statement
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 3. if-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs improvement"

print("Grade:", grade)


# 4. Multiple conditions
has_dataset = True
has_model = True

if has_dataset and has_model:
    print("Ready to evaluate the model.")
else:
    print("Prepare the dataset and model first.")


# 5. Nested conditions
accuracy = 92.0
minimum_accuracy = 90.0

if accuracy >= minimum_accuracy:
    if accuracy >= 95.0:
        print("Excellent model accuracy.")
    else:
        print("Model meets the minimum accuracy target.")
else:
    print("Model needs improvement.")


# 6. Membership condition
language = "Python"
supported_languages = ["Python", "R", "Java"]

if language in supported_languages:
    print(language, "is supported.")
else:
    print(language, "is not supported.")


# 7. AI Engineering example
correct_predictions = 920
total_predictions = 1000

if total_predictions > 0:
    accuracy = correct_predictions / total_predictions * 100

    if accuracy >= 90:
        print("Model status: Meets the accuracy target")
    else:
        print("Model status: Below the accuracy target")

    print("Accuracy:", accuracy, "%")
else:
    print("Cannot calculate accuracy: no predictions available.")
