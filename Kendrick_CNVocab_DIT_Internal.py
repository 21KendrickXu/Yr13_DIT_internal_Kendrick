"""This is a Chinese Vocab Test program."""
from tkinter import *
from tkinter import messagebox
import random


class Program:
    """Creat a class for this program."""

    def __init__(self, root):
        """Initialize the program."""
        self.chinese_words = [
            # Beginner Vocab
            ["人", "rén", "person"],
            ["口", "kǒu", "mouth"],
            ["日", "rì", "sun, day"],
            ["月", "yuè", "moon"],
            ["山", "shān", "mountain"],
            ["水", "shuǐ", "water"],
            ["火", "huǒ", "fire"],
            ["木", "mù", "wood"],
            ["大", "dà", "big"],
            ["小", "xiǎo", "small"],

            # Elementary Vocab
            ["中", "zhōng", "middle"],
            ["国", "guó", "country"],
            ["上", "shàng", "up"],
            ["下", "xià", "down"],
            ["好", "hǎo", "good"],
            ["学", "xué", "study"],
            ["生", "shēng", "life"],
            ["我", "wǒ", "me"],
            ["你", "nǐ", "you"],
            ["他", "tā", "he"],

            # Intermediate Vocab
            ["爱", "ài", "love"],
            ["想", "xiǎng", "think"],
            ["做", "zuò", "do, make"],
            ["说", "shuō", "speak"],
            ["看", "kàn", "look"],
            ["听", "tīng", "listen"],
            ["走", "zǒu", "walk"],
            ["来", "lái", "come"],
            ["去", "qù", "go"],
            ["有", "yǒu", "have"],

            # Upper Intermediate Vocab
            ["理", "lǐ", "reason"],
            ["情", "qíng", "emotion"],
            ["意", "yì", "meaning"],
            ["知", "zhī", "know"],
            ["道", "dào", "way"],
            ["得", "dé", "obtain"],
            ["法", "fǎ", "law"],
            ["信", "xìn", "believe"],
            ["明", "míng", "bright"],
            ["实", "shí", "real, solid"],

            # Advanced Vocab
            ["哲", "zhé", "philosophy"],
            ["辩", "biàn", "debate"],
            ["逻", "luó", "logic"],
            ["矛", "máo", "spear"],
            ["盾", "dùn", "shield"],
            ["抽", "chōu", "extract"],
            ["象", "xiàng", "elephant"],
            ["证", "zhèng", "proof"],
            ["论", "lùn", "discuss"],
            ["绝", "jué", "absolute"],

            # Expert (Rare/Complex) Vocab
            ["玄", "xuán", "mysterious, profound"],
            ["禅", "chán", "Zen (Buddhism)"],
            ["韵", "yùn", "rhyme, charm"],
            ["熵", "shāng", "entropy"],
            ["爻", "yáo", "divination lines"],
            ["龖", "dá", "appearance of a dragon"],
            ["靐", "bìng", "thunder"],
            ["齉", "nàng", "stuffy nose"],
            ["龘", "dá", "flying dragon"],
            ["䨻", "bèng", "thunderclap"]
        ]  # Create a Chinese character list
        self.option_list = []  # A list for contaning options
        self.current_ans = []  # A list for storing current answer
        self.f1 = Frame(
            root,
            bg="pink",
            padx=150,
            pady=120
            )  # Initialize the first frame
        self.f2 = Frame(
            root,
            bg="red",
            padx=100,
            pady=100
            )  # Initialize the second frame
        self.f1.grid(row=0, column=0)  # Grid the first frame
        self.title_label = Label(
            self.f1,
            text="Chinese Vocab Test"
            )  # Title of the window
        self.title_label.grid(row=0, column=1, padx=10, pady=5, sticky="n")
        self.test_label = Label(
            self.f1,
            text="中文")  # Title on the first page
        self.test_label.grid(row=0, column=0, padx=10, pady=5, sticky="n")
        self.chinese_label = Label(
            self.f1,
            text="测试"
            )  # Title on the first page
        self.chinese_label.grid(row=0, column=2, padx=10, pady=5, sticky="n")
        self.start_button = Button(
            self.f1,
            text="Start",
            command=self.change_to_display
            )  # Start button

        self.customized_live_header = Label(
            self.f1,
            text="Number of lives (1-5)"
            )  # Label of lives
        self.customized_live_header.grid(row=2, column=0, padx=10, pady=5)
        self.customized_live_entry = Entry(
            self.f1
            )  # Entry of lives
        self.customized_live_entry.grid(row=2, column=1, padx=10, pady=5)
        self.start_button.grid(row=1, column=1, padx=10, pady=5)

        # Header for question and character
        self.display_header = Label(
            self.f2,
            text=""
            )
        self.display_header.grid(row=0, column=1, padx=10, pady=5)
        self.display_que = Label(
            self.f2,
            text=""
            )
        self.display_que.grid(row=1, column=1, padx=10, pady=5)

        # Button for options
        self.b1 = Button(
            self.f2,
            text="",
            command=lambda: self.check_answer(self.b1)
            )
        self.b2 = Button(
            self.f2,
            text="",
            command=lambda: self.check_answer(self.b2)
            )
        self.b3 = Button(
            self.f2,
            text="",
            command=lambda: self.check_answer(self.b3)
            )
        self.b4 = Button(
            self.f2,
            text="",
            command=lambda: self.check_answer(self.b4)
            )
        self.b1.grid(row=2, column=0, padx=10, pady=5)
        self.b2.grid(row=2, column=2, padx=10, pady=5)
        self.b3.grid(row=3, column=0, padx=10, pady=5)
        self.b4.grid(row=3, column=2, padx=10, pady=5)

        # Variables for counting the wrong and correct questions
        self.count = 0
        self.lives = 0

        # Label for scoreboard
        self.score_board = Label(
            self.f2,
            text=f"Score: {self.count} Lives: {self.lives}"
            )
        self.score_board.grid(row=4, column=1, padx=10, pady=5)

    def change_to_display(self):
        """Change the first page to the second page."""
        if not self.customized_lives():
            return
        self.f1.grid_forget()
        self.f2.grid()  # Change the display from first page tp the second page
        self.generate_question()
        self.update_question()

    def generate_question(self):
        """Generate the question type and option."""
        selected = random.choice([True, False])  # Questions type selecting
        if selected:
            self.display_que.config(text="Which one is the right pinyin?")
            self.generate_option()
            self.update_buttons(1, self.b1, self.b2, self.b3, self.b4)  # Questions for pinyin
        else:
            self.display_que.config(text="Which one is the right meaning?")
            self.generate_option()
            self.update_buttons(2, self.b1, self.b2, self.b3, self.b4)  # Questions for meaning

    def update_question(self):
        """Update the word from question the the header."""
        selected = random.choice(self.option_list)
        self.display_header.config(text=f"{selected[0]}")  # display the characters
        self.current_ans.append(selected)

    def generate_option(self):
        """Randomly choose 4 characters."""
        self.option_list.clear()
        selected = random.sample(self.chinese_words, 4)
        self.option_list.extend(selected)

    def update_buttons(self, que_type, *buttons):
        """Update the diplay pf the button."""
        self.num_btn = len(buttons)
        self.num_opt = len(self.option_list)
        self.select_indi = random.sample(range(self.num_opt), self.num_btn)  # Rearrange the options
        for b, idx in zip(buttons, self.select_indi):
            b.config(text=self.option_list[idx][que_type])  # Update the context on the button

    def check_score(self):
        """Check the score of users and give them results."""
        if self.count > 19 or self.lives == 0:
            degree = self.count + self.lives
            if degree >= 20:
                title = "Expert"
            elif degree < 20 and degree > 15:
                title = "Advanced"
            elif degree < 15 and degree > 10:
                title = "Intermediate"
            elif degree < 10 and degree > 5:
                title = "Beginner"
            elif degree < 5 and degree > 0:
                title = "You do not speak Chinese"
            else:
                title = "Martian"
            # Calculating users' Chinese level
            messagebox.showinfo(
                "You test finished!",
                f"Correct: {self.count} Level: {title}"
                )  # Give results
            self.count = 0
            self.f2.grid_forget()
            self.f1.grid() # Go back to the first page

    def check_answer(self, button):
        """Check if the answer is right."""
        selected_answer = button["text"]
        if self.display_que["text"] == "Which one is the right pinyin?":
            correct_ans = self.current_ans[0][1]  # Check answer for pinyin
        else:
            correct_ans = self.current_ans[0][2]  # Check answer for meaning

        if selected_answer == correct_ans:
            messagebox.showinfo("Correct!", "Well done!")   # Send correct message to users
            self.count += 1
            self.score_board.config(
                text=f"Score: {self.count} Lives: {self.lives}"
                )
        else:
            messagebox.showerror(
                "Wrong!",
                f"You are wrong!!! Correct Answer: {correct_ans}"
                )  # Send wrong message to users
            self.lives -= 1
            self.score_board.config(
                text=f"Score: {self.count} Lives: {self.lives}"
                )# Update the score board

        self.current_ans.clear()
        self.option_list.clear()
        # Clear the list
        self.check_score()
        self.generate_question()
        self.update_question()
        # Generate the next question

    def customized_lives(self):
        """For user to choose how many mistakes are allowed."""
        try:
            self.lives = int(self.customized_live_entry.get())
            if 0 < self.lives < 6:
                self.score_board.config(
                    text=f"Score: {self.count} Lives: {self.lives}"
                    )
                return True
            else:
                messagebox.showerror(
                    "Invalid",
                    "Please enter a number between 1 and 5"
                    )
                # Send error to users 
                return False
        except ValueError:
            messagebox.showerror(
                "Invalid",
                "Please enter a number between 1 and 5"
                )
                # Send error to users 
            return False


if __name__ == "__main__":
    """Run the program."""
    root = Tk()
    root.grid_rowconfigure(0, weight=1, minsize=50)
    root.grid_columnconfigure(0, weight=1, minsize=0)
    root.grid_columnconfigure(1, weight=1, minsize=0)
    character = Program(root)
    root.mainloop()
