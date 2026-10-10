
"""
Python Operators
----------------
Learn the operators used in Python and AI Engineering.
"""

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. Comparison Operators
print("\nComparison Operators")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# 3. Assignment Operators
score = 10
score += 5
print("\nAssignment Operators")
print("Updated score:", score)


# 4. Logical Operators
is_training = True
has_data = False

print("\nLogical Operators")
print("AND:", is_training and has_data)
print("OR:", is_training or has_data)
print("NOT:", not is_training)


# 5. Membership Operators
languages = ["Python", "Java", "C++"]

print("\nMembership Operators")
print("Python available:", "Python" in languages)
print("JavaScript available:", "JavaScript" not in languages)


# 6. Identity Operators
first_list = [1, 2, 3]
second_list = [1, 2, 3]
third_list = first_list

print("\nIdentity Operators")
print("first_list is second_list:", first_list is second_list)
print("first_list is third_list:", first_list is third_list)
print("first_list == second_list:", first_list == second_list)


# 7. Bitwise Operators
x = 5  # Binary: 0101
y = 3  # Binary: 0011

print("\nBitwise Operators")
print("AND:", x & y)
print("OR:", x | y)
print("XOR:", x ^ y)


# 8. AI Engineering Example
correct_predictions = 920
total_predictions = 1000

accuracy = correct_predictions / total_predictions * 100

print("\nAI Model Evaluation")
print("Correct predictions:", correct_predictions)
print("Total predictions:", total_predictions)
print("Model accuracy:", accuracy, "%")

