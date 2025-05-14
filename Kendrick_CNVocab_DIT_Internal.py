"""This is a Chinese Vocab Test program."""
from tkinter import *
from tkinter import messagebox
import random

class Character:
    """This is a helper class for storing the infomation of Chinese characters"""
    def __init__(self, character, pinyin, meaning):
        self.character = character
        self.pinyin = pinyin
        self.meaning = meaning
        
class Program:
    """Creat a class for this program."""

    def __init__(self, root):
        """Initialize the program."""
        self.chinese_words = [
            # Beginner Vocab
            Character("人", "rén", "person"),
            Character("口", "kǒu", "mouth"),
            Character("日", "rì", "sun, day"),
            Character("月", "yuè", "moon"),
            Character("山", "shān", "mountain"),
            Character("水", "shuǐ", "water"),
            Character("火", "huǒ", "fire"),
            Character("木", "mù", "wood"),
            Character("大", "dà", "big"),
            Character("小", "xiǎo", "small"),

            # Elementary Vocab
            Character("中", "zhōng", "middle"),
            Character("国", "guó", "country"),
            Character("上", "shàng", "up"),
            Character("下", "xià", "down"),
            Character("好", "hǎo", "good"),
            Character("学", "xué", "study"),
            Character("生", "shēng", "life"),
            Character("我", "wǒ", "me"),
            Character("你", "nǐ", "you"),
            Character("他", "tā", "he"),

            # Intermediate Vocab
            Character("爱", "ài", "love"),
            Character("想", "xiǎng", "think"),
            Character("做", "zuò", "do, make"),
            Character("说", "shuō", "speak"),
            Character("看", "kàn", "look"),
            Character("听", "tīng", "listen"),
            Character("走", "zǒu", "walk"),
            Character("来", "lái", "come"),
            Character("去", "qù", "go"),
            Character("有", "yǒu", "have"),

            # Upper Intermediate Vocab
            Character("理", "lǐ", "reason"),
            Character("情", "qíng", "emotion"),
            Character("意", "yì", "meaning"),
            Character("知", "zhī", "know"),
            Character("道", "dào", "way"),
            Character("得", "dé", "obtain"),
            Character("法", "fǎ", "law"),
            Character("信", "xìn", "believe"),
            Character("明", "míng", "bright"),
            Character("实", "shí", "real, solid"),

            # Advanced Vocab
            Character("哲", "zhé", "philosophy"),
            Character("辩", "biàn", "debate"),
            Character("逻", "luó", "logic"),
            Character("矛", "máo", "spear"),
            Character("盾", "dùn", "shield"),
            Character("抽", "chōu", "extract"),
            Character("象", "xiàng", "elephant"),
            Character("证", "zhèng", "proof"),
            Character("论", "lùn", "discuss"),
            Character("绝", "jué", "absolute"),

            # Expert (Rare/Complex) Vocab
            Character("玄", "xuán", "mysterious, profound"),
            Character("禅", "chán", "Zen (Buddhism)"),
            Character("韵", "yùn", "rhyme, charm"),
            Character("熵", "shāng", "entropy"),
            Character("爻", "yáo", "divination lines"),
            Character("龖", "dá", "appearance of a dragon"),
            Character("靐", "bìng", "thunder"),
            Character("齉", "nàng", "stuffy nose"),
            Character("龘", "dá", "flying dragon"),
            Character("䨻", "bèng", "thunderclap")
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
        """Change the first page to the second page by griding."""
        if not self.customized_lives():
            return
        # Check if the user put a valid number in the blank
        self.f1.grid_forget()
        self.f2.grid()  # Change the display from first page tp the second page
        self.generate_question()
        self.update_question()

    def generate_question(self):
        """Generate the question type and option based on random choose of Boolean"""
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
        self.display_header.config(text=f"{selected.character}")  # display the characters
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
            if que_type == 1:
                b.config(text=self.option_list[idx].pinyin) 
            else:
                b.config(text=self.option_list[idx].meaning)

    def check_score(self):
        """Check the score of users and give them results. It will calculate the users' Chinese level based on the correct answers and go back to the begining page."""
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
                title = "U do not speak Chinese"
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
        """This function will check if the answer is right and use the if statement to send message to users in order to tell them if they are correct."""
        selected_answer = button["text"]
        if self.display_que["text"] == "Which one is the right pinyin?":
            correct_ans = self.current_ans[0].pinyin  # Check answer for pinyin
        else:
            correct_ans = self.current_ans[0].meaning  # Check answer for meaning

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
        """For user to choose how many mistakes are allowed. This loop will keep running until the users enter a valid integer."""
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
