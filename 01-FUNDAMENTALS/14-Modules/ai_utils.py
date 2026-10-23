
# Reusable AI utility functions

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def evaluate_accuracy(accuracy):
    if not 0 <= accuracy <= 100:
        return "Invalid accuracy"
    if accuracy >= 90:
        return "Excellent"
    elif accuracy >= 70:
        return "Good"
    return "Needs improvement"


def display_model_info(name, accuracy):
    print(f"Model: {name}")
    print(f"Accuracy: {accuracy}%")
    print(f"Status: {evaluate_accuracy(accuracy)}")
