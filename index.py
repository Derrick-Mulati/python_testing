import random
import time
import tkinter as tk
from tkinter import messagebox

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Game")

        self.score = 0
        self.rounds = 5
        self.current_round = 0

        # Create UI components
        self.create_widgets()
        self.start_new_round()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Math Quiz Game", font=("Helvetica", 24, "bold"), pady=20)
        self.title_label.pack()

        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.question_label.pack(pady=10)

        # Answer Entry
        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 14), padx=10, pady=5)
        self.submit_button.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(self.root, text=f"Score: 0/{self.rounds}", font=("Helvetica", 14))
        self.score_label.pack(pady=5)

    def generate_question(self):
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

    def start_new_round(self):
        self.current_round += 1

        if self.current_round > self.rounds:
            self.end_game()
            return

        self.question, self.correct_answer = self.generate_question()
        self.question_label.config(text=f"Question {self.current_round}: {self.question}")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        try:
            user_answer = float(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            return

        # Check if the answer is correct
        if abs(user_answer - self.correct_answer) < 0.001:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done! That's the correct answer.")
        else:
            messagebox.showerror("Wrong Answer", f"Oops! The correct answer was {self.correct_answer:.2f}")

        self.update_score()
        self.start_new_round()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}/{self.rounds}")

    def end_game(self):
        messagebox.showinfo("Game Over", f"Your final score is: {self.score}/{self.rounds}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
