
# Python List Comprehensions
# AI Engineer Learning Journey

# 1. Create a list of squares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]

print("Original numbers:", numbers)
print("Squares:", squares)

# 2. Filter even numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

# 3. Filter odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
print("Odd numbers:", odd_numbers)

# 4. Process AI model accuracy scores
accuracies = [65, 78, 92, 88, 95, 54, 97]
high_accuracy = [score for score in accuracies if score >= 90]

print("All model accuracies:", accuracies)
print("High accuracy scores:", high_accuracy)

# 5. Convert scores into percentages
scores = [0.75, 0.82, 0.91, 0.96]
percentages = [round(score * 100, 2) for score in scores]

print("Accuracy percentages:", percentages)

# 6. Label models based on accuracy
model_status = [
    "Excellent" if score >= 90 else "Needs improvement"
    for score in accuracies
]

print("Model status:", model_status)

# 7. Extract names with uppercase conversion
model_names = ["linear regression", "decision tree", "neural network"]
uppercase_names = [name.upper() for name in model_names]

print("Model names:", uppercase_names)
