from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface(Tk):

    def __init__(self, quiz_brain: QuizBrain ):
        super().__init__()

        self.quize  = quiz_brain
        score = self.quize.score

        self.title('Quizzler')
        self.config(background = THEME_COLOR)


        self.score_label = Label(text = f"Score: {score}", bg = THEME_COLOR, fg = 'white')
        self.score_label.grid(row = 0, column = 1, pady = 20, padx = 20)

        self.canva = Canvas(width = 300, height = 250)
        # self.canva.create_rectangle(0, 0, 300, -250)
        self.question_text = self.canva.create_text(150,125,
                                                    text = f"Something Question",
                                                    fill = THEME_COLOR,
                                                    width = 280,
                                                    font = ('Aral', 20, 'italic'))
        self.canva.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = 20)
        self.next_question()

        false_img = PhotoImage(file = "images/false.png")
        true_img = PhotoImage(file = "images/true.png")

        self.false_button = Button(image = false_img, highlightthickness = 0, command = self.false_answer)
        self.false_button.grid(row = 2, column = 0, padx = 20, pady = 20)

        self.true_button = Button(image = true_img, highlightthickness = 0, command = self.true_answer)
        self.true_button.grid(row = 2, column = 1, padx = 20, pady = 20)

        self.mainloop()

    def next_question(self):
        self.canva.config(bg='white')
        if self.quize.still_has_questions():
            self.score_label.config(text=(f"Score: {self.quize.score}"))

            q_text = self.quize.next_question()
            self.canva.itemconfig(self.question_text, text = f"{q_text}")
        else:
            self.canva.itemconfig(self.question_text, text = "You've reach the end question.")
            self.false_button.config(state = 'disable')
            self.true_button.config(state = 'disable')


    def true_answer(self):
        is_right = self.quize.check_answer("True")
        self.give_feadback(is_right)


    def false_answer(self):
        is_right = self.quize.check_answer("False")
        self.give_feadback(is_right)

    def give_feadback(self, is_right):

        if is_right:
            self.canva.config(bg = 'green')
        else:
            self.canva.config(bg = 'red')

        # self.after_cancel(self.next_question)
        self.after(1000, self.next_question)
