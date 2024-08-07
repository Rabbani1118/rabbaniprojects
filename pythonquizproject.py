import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.quiz_data = [  
           {
            "question":"Who developed Python Programming Language?",
            "options":["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
            "correct_answer": 2
           },
           {
            "question":"Which year was Python created?",
            "options":["1989", "1991", "2000", "2010"],
            "correct_answer": 1
           },
           {
            "question":"Which type of Programming does Python support?",
            "options":["object-oriented programming", "structured programming","functional programming","all of the mentioned"],
            "correct_answer": 0
           },
           {
            "question":"Which of the following is a Python framework?",
            "options":["Django", "React", "Vue", "Angular"],
            "correct_answer": 0
           },
           {
            "question":"Which of the following is the correct extension of the Python file??",
            "options":[".python",".pl", ".py", ".p"],
            "correct_answer": 2
           }
        ]
        self.current_question_index = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.question_frame = tk.Frame(self.window)
        self.question_frame.pack()

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=30, command=self.next_question)
        self.next_question_button.pack(pady=10)

    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer = question_data["correct_answer"]
        correct_option = question_data["options"][correct_answer]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Your answer is wrong. The correct answer is: {correct_option}")

    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Over", f"Your score is {self.score}/{len(self.quiz_data)}")
            self.window.quit()
        else:
            self.load_question()

    def start_quiz(self):
        self.load_question()
        self.window.mainloop()

quiz_app = QuizApp()
quiz_app.start_quiz()
