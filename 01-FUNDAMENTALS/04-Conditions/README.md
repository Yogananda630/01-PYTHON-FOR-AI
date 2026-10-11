# 🐍 Python Conditions

Conditions allow a Python program to make decisions based on whether expressions are `True` or `False`.

## Learning Objectives

- Understand `if`, `elif`, and `else`.
- Write conditions using comparison operators.
- Combine conditions with `and`, `or`, and `not`.
- Use nested conditions.
- Apply decision-making to AI model evaluation.

## 1. The `if` Statement

Executes a block when a condition is true.

```python
age = 21

if age >= 18:
    print("You are an adult.")
```

## 2. The `if-else` Statement

Chooses between two alternatives.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 3. The `if-elif-else` Statement

Checks multiple conditions in order.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs improvement"

print(grade)
```

## 4. Combining Conditions

Use `and`, `or`, and `not` to combine or reverse logical conditions.

```python
has_dataset = True
has_model = True

if has_dataset and has_model:
    print("Ready to evaluate the model.")
```

## 5. Nested Conditions

A condition can contain another condition. Use nesting only when it makes the logic clearer.

## AI Engineering Example

```python
correct_predictions = 920
total_predictions = 1000

if total_predictions > 0:
    accuracy = correct_predictions / total_predictions * 100

    if accuracy >= 90:
        print("Model meets the accuracy target.")
    else:
        print("Model needs improvement.")

    print("Accuracy:", accuracy, "%")
else:
    print("No predictions available.")
```

Output:

```text
Model meets the accuracy target.
Accuracy: 92.0 %
```

## Practice Tasks

1. Check whether a number is positive, negative, or zero.
2. Check whether a number is even or odd.
3. Assign grades based on marks.
4. Check whether a user meets two eligibility conditions.
5. Decide whether a model meets a chosen accuracy threshold.

## Practice Code

See [`conditions.py`](./conditions.py).

---

**Previous:** [Operators](../03-Operators/)

**Next:** [Loops](../05-Loops/)
