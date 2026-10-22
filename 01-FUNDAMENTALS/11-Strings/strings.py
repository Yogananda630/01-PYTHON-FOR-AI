
# Python Strings - AI Engineer Journey

# 1. Create strings
message = "Welcome to Python for AI!"
print("Message:", message)

# 2. String length
print("Length:", len(message))

# 3. Change letter case
text = "artificial intelligence"
print("Uppercase:", text.upper())
print("Title Case:", text.title())
print("Lowercase:", text.lower())

# 4. Remove extra spaces
name = "   Yogananda630   "
print("Clean name:", name.strip())

# 5. Access characters
language = "Python"
print("First character:", language[0])
print("Last character:", language[-1])

# 6. String slicing
print("First three characters:", language[:3])
print("Last three characters:", language[-3:])

# 7. Search within text
sentence = "Python is useful for AI and Machine Learning"
print("Contains AI:", "AI" in sentence)
print("Position of AI:", sentence.find("AI"))

# 8. Replace text
updated = sentence.replace("Python", "Generative AI")
print("Updated sentence:", updated)

# 9. Split a sentence into words
words = sentence.split()
print("Words:", words)
print("Number of words:", len(words))

# 10. Join words
skills = ["Python", "Machine Learning", "Deep Learning"]
print("AI skills:", ", ".join(skills))

# 11. String formatting
student = "Yogananda"
accuracy = 92.5
print(f"{student}'s AI model accuracy is {accuracy}%.")

# 12. Basic text cleaning
user_input = "  PYTHON FOR AI  "
cleaned_text = user_input.strip().lower()
print("Cleaned text:", cleaned_text)
