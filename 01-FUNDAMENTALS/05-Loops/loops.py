
# Python Loops - AI Engineer Journey

# 1. For loop
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# 2. While loop
print("\nWhile loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 3. Loop through a list
print("\nAI Skills:")
skills = ["Python", "Machine Learning", "Deep Learning", "Generative AI"]

for skill in skills:
    print(skill)

# 4. Break statement
print("\nBreak example:")
for number in range(1, 10):
    if number == 5:
        break
    print(number)

# 5. Continue statement
print("\nContinue example:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
