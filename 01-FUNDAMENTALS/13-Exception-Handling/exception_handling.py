
# Python Exception Handling - AI Engineer Journey

# 1. Handle division by zero
print("1. Division Example")

try:
    number = 10
    divisor = 0
    result = number / divisor
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# 2. Handle invalid input conversion
print("\n2. Value Conversion Example")

user_input = "hello"

try:
    number = int(user_input)
    print("Number:", number)
except ValueError:
    print("Error: Input must contain a valid integer.")


# 3. Handle multiple exceptions
print("\n3. Multiple Exceptions")

try:
    numbers = [10, 20, 30]
    index = 5
    print(numbers[index] / 0)
except IndexError:
    print("Error: List index is out of range.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# 4. Use else and finally
print("\n4. Else and Finally")

try:
    result = 100 / 5
except ZeroDivisionError:
    print("Division failed.")
else:
    print("Division successful:", result)
finally:
    print("Division operation completed.")


# 5. Validate AI model accuracy
print("\n5. AI Model Evaluation")

def evaluate_model(accuracy):
    try:
        accuracy = float(accuracy)

        if not 0 <= accuracy <= 100:
            raise ValueError("Accuracy must be between 0 and 100.")

        if accuracy >= 90:
            return "Excellent model"
        elif accuracy >= 70:
            return "Acceptable model"
        else:
            return "Model needs improvement"

    except (ValueError, TypeError) as error:
        return f"Invalid accuracy: {error}"

print(evaluate_model(92.5))
print(evaluate_model(65))
print(evaluate_model("invalid"))
print(evaluate_model(150))

print("\nProgram completed safely.")
