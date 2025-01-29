import random
import time

# Welcome Message
print("Welcome to the Math Quiz Game!")
print("Test your math skills with random arithmetic questions.")

# Function to generate a random math question
def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)

    # Ensure division results in an integer answer
    if operation == '/':
        num1 = num1 * num2

    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)

    return question, correct_answer

# Main game loop
score = 0
rounds = 5

print(f"You will get {rounds} questions. Try your best!")

for i in range(1, rounds + 1):
    print(f"\nQuestion {i}:")
    question, correct_answer = generate_question()

    print(question)
    
    # Get the user's answer
    try:
        user_answer = float(input("Your answer: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Check if the answer is correct
    if abs(user_answer - correct_answer) < 0.001:
        print("Correct!")
        score += 1
    else:
        print(f"Oops! The correct answer was {correct_answer:.2f}")

    time.sleep(1)

# Display final results
print("\nGame Over!")
print(f"Your final score is: {score}/{rounds}")

if score == rounds:
    print("Amazing! You're a math genius!")
elif score >= rounds / 2:
    print("Good job! Keep practicing.")
else:
    print("Don't worry, you'll do better next time!")
