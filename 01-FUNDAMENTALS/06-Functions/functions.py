
# Python Functions - AI Engineer Journey

# 1. Simple function
def greet():
    print("Welcome to Python for AI!")

greet()


# 2. Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Yogananda")


# 3. Function that returns a value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)


# 4. Default parameter
def introduce(name, goal="AI Engineer"):
    print(f"{name} wants to become an {goal}.")

introduce("Yogananda")


# 5. Function for AI model accuracy
def evaluate_model(accuracy):
    if accuracy >= 90:
        return "Excellent"
    elif accuracy >= 70:
        return "Good"
    else:
        return "Needs improvement"

print("Model evaluation:", evaluate_model(92))


# 6. Calculate average
def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

scores = [85, 90, 95]
print("Average score:", calculate_average(scores))
