# ⚙️ Python Operators

Operators are symbols and keywords used to perform calculations, compare values, make logical decisions, and manipulate data in Python.

## 🎯 Learning Objectives

- Understand the main categories of Python operators.
- Perform arithmetic calculations.
- Compare values and evaluate conditions.
- Use logical operators to combine conditions.
- Understand membership, identity, and bitwise operators.
- Apply operators to AI engineering examples.

## 1. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 3 = 13` |
| `-` | Subtraction | `10 - 3 = 7` |
| `*` | Multiplication | `10 * 3 = 30` |
| `/` | Division | `10 / 3` |
| `//` | Floor division | `10 // 3 = 3` |
| `%` | Modulus (remainder) | `10 % 3 = 1` |
| `**` | Exponentiation | `10 ** 3 = 1000` |

## 2. Comparison Operators

Comparison operators compare two values and return a Boolean result: `True` or `False`.

- `==` — equal to
- `!=` — not equal to
- `>` — greater than
- `<` — less than
- `>=` — greater than or equal to
- `<=` — less than or equal to

## 3. Assignment Operators

Assignment operators assign or update variable values.

```python
score = 10
score += 5

print(score)  # 15
```

Other examples include `-=`, `*=`, `/=`, and `//=`.

## 4. Logical Operators

Logical operators combine or reverse Boolean conditions.

- `and` — True when both conditions are True.
- `or` — True when at least one condition is True.
- `not` — reverses a Boolean condition.

These operators help build conditions in data processing and machine learning workflows.

## 5. Membership Operators

Membership operators check whether a value exists in a collection.

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)       # True
print("JavaScript" not in languages)  # True
```

## 6. Identity Operators

Identity operators check whether two references point to the same object.

- `is` — refers to the same object.
- `is not` — refers to different objects.

**Important:** `==` checks value equality, while `is` checks object identity.

## 7. Bitwise Operators

Bitwise operators work on the binary representation of integers.

| Operator | Meaning |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left shift |
| `>>` | Right shift |

Example:

```python
x = 5
y = 3

print(x & y)  # 1
print(x | y)  # 7
print(x ^ y)  # 6
```

## 🤖 AI Engineering Example

Model accuracy can be calculated using arithmetic operators:

```python
correct_predictions = 920
total_predictions = 1000

accuracy = correct_predictions / total_predictions * 100

print(accuracy)  # 92.0
```

Accuracy is 92% because 920 out of 1,000 predictions were correct. In real projects, choose evaluation metrics based on the problem and dataset.

## 🧪 Practice Tasks

1. Calculate the average of three numbers.
2. Check whether a number is even using `%`.
3. Compare two model accuracy values.
4. Use `and` to check whether two conditions are True.
5. Check whether `"Python"` exists in a list of programming languages.
6. Calculate the accuracy percentage for a different set of predictions.

## 📁 Practice Code

See [`operators.py`](./operators.py).

---

**Previous Topic:** [Data Types](../02-Data-Types/)

**Next Topic:** [Conditions](../04-Conditions/)
