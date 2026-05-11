import tkinter as tk
from tkinter import messagebox
import random

def find_missing_transform_conquer(number_list):
    j_last_two = 0
    for num in number_list:
        j_last_two = (j_last_two + num) % 100
    if j_last_two == 50:
        return 100
    elif j_last_two <= 49:
        return 50 - j_last_two
    else:
        return 150 - j_last_two

def generate_99_random_numbers():
    all_numbers = list(range(1, 101))
    random.shuffle(all_numbers)
    return all_numbers[:99]

class MissingNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Missing Number Game")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')

        self.total_score = 0
        self.rounds_count = 0
        self.number_list = []
        self.missing_number = None
        self.current_round = 0
        self.round_won = 0
        self.time_limits = [20, 15, 10]
        self.timer_id = None
        self.guess_submitted = False
        self.score_label = None

        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.root, bg='#2c3e50')
        header_frame.pack(pady=30)

        title = tk.Label(header_frame, text="🔢 MISSING NUMBER GAME 🔢",
                         font=('Arial', 28, 'bold'), fg='#ecf0f1', bg='#2c3e50')
        title.pack()

        subtitle = tk.Label(header_frame, text="Using Transform & Conquer Algorithm",
                           font=('Arial', 12), fg='#bdc3c7', bg='#2c3e50')
        subtitle.pack()

        score_frame = tk.Frame(self.root, bg='#34495e', relief=tk.RAISED, bd=2)
        score_frame.pack(pady=20, padx=50, fill=tk.X)

        self.score_label = tk.Label(score_frame, text=f"SCORE: {self.total_score}    ROUNDS: {self.rounds_count}",
                                    font=('Arial', 16, 'bold'), fg='#f1c40f', bg='#34495e')
        self.score_label.pack(pady=10)

        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=30)

        buttons = [
            ("🎯 EASY MODE", "#27ae60", self.easy_mode),
            ("⚡ CHALLENGE MODE", "#e67e22", self.challenge_mode),
            ("👥 TWO PLAYER MODE", "#3498db", self.two_player_mode),
            ("📖 INSTRUCTIONS", "#95a5a6", self.show_instructions),
            ("🚪 EXIT", "#e74c3c", self.exit_game)
        ]

        for text, color, command in buttons:
            btn = tk.Button(button_frame, text=text, font=('Arial', 14, 'bold'),
                           bg=color, fg='white', padx=30, pady=10,
                           relief=tk.RAISED, bd=3, cursor='hand2',
                           command=command)
            btn.pack(pady=8, fill=tk.X, padx=50)

    def update_score_display(self):
        if self.score_label and self.score_label.winfo_exists():
            self.score_label.config(text=f"SCORE: {self.total_score}    ROUNDS: {self.rounds_count}")

    def cancel_timer(self):
        if hasattr(self, 'timer_id') and self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def easy_mode(self):
        self.number_list = generate_99_random_numbers()
        self.missing_number = find_missing_transform_conquer(self.number_list)

        for widget in self.root.winfo_children():
            widget.destroy()

        back_btn = tk.Button(self.root, text="← BACK TO MENU", font=('Arial', 10),
                            bg='#95a5a6', fg='white', command=self.create_main_menu,
                            relief=tk.FLAT, cursor='hand2')
        back_btn.pack(anchor='nw', padx=10, pady=5)

        title = tk.Label(self.root, text="EASY MODE", font=('Arial', 24, 'bold'),
                        fg='#ecf0f1', bg='#2c3e50')
        title.pack(pady=10)

        self.number_display = tk.Label(self.root, text="", font=('Courier', 48, 'bold'),
                                        fg='#f1c40f', bg='#2c3e50')
        self.number_display.pack(pady=50)

        self.progress_label = tk.Label(self.root, text="", font=('Arial', 12),
                                       fg='#bdc3c7', bg='#2c3e50')
        self.progress_label.pack()

        start_btn = tk.Button(self.root, text="START GAME", font=('Arial', 14, 'bold'),
                             bg='#27ae60', fg='white', padx=20, pady=8,
                             command=self.start_easy_mode, cursor='hand2')
        start_btn.pack(pady=20)

    def start_easy_mode(self):
        self.current_index = 0

        def show_next():
            if self.current_index < 99:
                self.number_display.config(text=str(self.number_list[self.current_index]))
                self.progress_label.config(text=f"Number {self.current_index + 1} of 99")
                self.current_index += 1
                self.root.after(700, show_next)
            else:
                self.ask_easy_guess()

        show_next()

    def ask_easy_guess(self):
        self.number_display.config(text="???")
        self.progress_label.config(text="All numbers recited! What is missing?")

        guess_frame = tk.Frame(self.root, bg='#2c3e50')
        guess_frame.pack(pady=30)

        tk.Label(guess_frame, text="Your guess:", font=('Arial', 14),
                fg='white', bg='#2c3e50').pack()

        self.guess_entry = tk.Entry(guess_frame, font=('Arial', 14), width=10, justify='center')
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind('<Return>', lambda e: self.check_easy_guess())

        submit_btn = tk.Button(guess_frame, text="SUBMIT GUESS", font=('Arial', 12, 'bold'),
                              bg='#3498db', fg='white', padx=20, pady=5,
                              command=self.check_easy_guess, cursor='hand2')
        submit_btn.pack()

    def check_easy_guess(self):
        guess_text = self.guess_entry.get().strip()

        if not guess_text:
            messagebox.showerror("ERROR", "Please enter a number")
            return

        try:
            guess = int(guess_text)
            if guess < 1 or guess > 100:
                messagebox.showerror("ERROR", "Please enter a number between 1 and 100")
                return

            if guess == self.missing_number:
                self.total_score += 10
                self.rounds_count += 1
                messagebox.showinfo("CORRECT!", f"✅ Great! The missing number was {self.missing_number}\n+10 points!\n\nScore: {self.total_score}")
                answer = messagebox.askyesno("PLAY AGAIN?", "Would you like to play another round?")
                if answer:
                    self.easy_mode()
                else:
                    self.create_main_menu()
            else:
                self.rounds_count += 1
                messagebox.showinfo("GAME OVER!", f"❌ Wrong! The missing number was {self.missing_number}\n\nYour score: {self.total_score}\nRounds played: {self.rounds_count}")
                answer = messagebox.askyesno("PLAY AGAIN?", "Would you like to try again?")
                if answer:
                    self.easy_mode()
                else:
                    self.create_main_menu()
        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid number (1-100)")

    def challenge_mode(self):
        self.round_won = 0
        self.current_round = 0
        self.start_challenge_round()

    def start_challenge_round(self):
        self.cancel_timer()
        self.guess_submitted = False

        for widget in self.root.winfo_children():
            widget.destroy()

        back_btn = tk.Button(self.root, text="← BACK TO MENU", font=('Arial', 10),
                            bg='#95a5a6', fg='white', command=self.create_main_menu,
                            relief=tk.FLAT, cursor='hand2')
        back_btn.pack(anchor='nw', padx=10, pady=5)

        time_limit = self.time_limits[self.current_round]

        self.number_list = generate_99_random_numbers()
        self.missing_number = find_missing_transform_conquer(self.number_list)

        title = tk.Label(self.root, text=f"CHALLENGE MODE - ROUND {self.current_round + 1}",
                        font=('Arial', 20, 'bold'), fg='#ecf0f1', bg='#2c3e50')
        title.pack(pady=10)

        self.timer_label = tk.Label(self.root, text=f"⏱️ {time_limit} SECONDS LEFT ⏱️",
                                    font=('Arial', 14, 'bold'), fg='#e67e22', bg='#2c3e50')
        self.timer_label.pack(pady=5)

        grid_frame = tk.Frame(self.root, bg='#34495e')
        grid_frame.pack(pady=20, padx=20)

        index = 0
        for row in range(5):
            row_frame = tk.Frame(grid_frame, bg='#34495e')
            row_frame.pack()
            for col in range(20):
                if index < 99:
                    cell = tk.Label(row_frame, text=str(self.number_list[index]),
                                   font=('Courier', 10), width=4, height=1,
                                   relief=tk.RIDGE, bg='#ecf0f1')
                    cell.pack(side=tk.LEFT, padx=1, pady=1)
                    index += 1
                else:
                    cell = tk.Label(row_frame, text="??",
                                   font=('Courier', 10, 'bold'), width=4, height=1,
                                   relief=tk.RIDGE, bg='#f1c40f', fg='black')
                    cell.pack(side=tk.LEFT, padx=1, pady=1)

        guess_frame = tk.Frame(self.root, bg='#2c3e50')
        guess_frame.pack(pady=20)

        tk.Label(guess_frame, text="Enter your guess:", font=('Arial', 12),
                fg='white', bg='#2c3e50').pack()

        self.guess_entry = tk.Entry(guess_frame, font=('Arial', 14), width=10, justify='center')
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind('<Return>', lambda e: self.check_challenge_guess())

        submit_btn = tk.Button(guess_frame, text="SUBMIT GUESS", font=('Arial', 12, 'bold'),
                              bg='#e67e22', fg='white', padx=20, pady=5,
                              command=self.check_challenge_guess, cursor='hand2')
        submit_btn.pack()

        remaining = time_limit

        def countdown():
            nonlocal remaining
            if self.guess_submitted:
                return
            if remaining <= 0:
                self.timer_label.config(text="⏰ TIME'S UP! ⏰", fg='red')
                self.guess_submitted = True
                messagebox.showinfo("TIME'S UP!", f"You ran out of time!\nThe missing number was {self.missing_number}")
                answer = messagebox.askyesno("PLAY AGAIN?", "Would you like to try again?")
                if answer:
                    self.challenge_mode()
                else:
                    self.create_main_menu()
                return
            self.timer_label.config(text=f"⏱️ {remaining} SECONDS LEFT ⏱️")
            remaining -= 1
            self.timer_id = self.root.after(1000, countdown)

        self.timer_id = self.root.after(1000, countdown)

    def check_challenge_guess(self):
        if self.guess_submitted:
            return

        guess_text = self.guess_entry.get().strip()

        if not guess_text:
            messagebox.showerror("ERROR", "Please enter a number")
            return

        try:
            guess = int(guess_text)
            if guess < 1 or guess > 100:
                messagebox.showerror("ERROR", "Please enter a number between 1 and 100")
                return

            self.guess_submitted = True
            self.cancel_timer()

            if guess == self.missing_number:
                self.round_won += 1
                if self.current_round == 2:
                    self.total_score += 50
                    self.rounds_count += 1
                    messagebox.showinfo("🏆 YOU WIN! 🏆", f"Completed all 3 rounds!\n+50 BONUS POINTS!\n\nTotal Score: {self.total_score}")
                    answer = messagebox.askyesno("PLAY AGAIN?", "Would you like to play another round?")
                    if answer:
                        self.challenge_mode()
                    else:
                        self.create_main_menu()
                else:
                    self.total_score += 10
                    messagebox.showinfo("ROUND PASSED!", f"✅ Correct!\n+10 points!\nMoving to next round...")
                    self.current_round += 1
                    self.start_challenge_round()
            else:
                self.rounds_count += 1
                messagebox.showinfo("GAME OVER!", f"❌ Wrong! The missing number was {self.missing_number}\nYou completed {self.round_won} out of 3 rounds\n\nScore: {self.total_score}")
                answer = messagebox.askyesno("PLAY AGAIN?", "Would you like to try again?")
                if answer:
                    self.challenge_mode()
                else:
                    self.create_main_menu()
        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid number (1-100)")

    # ========== TWO PLAYER MODE - USING ALGORITHM ==========
    # Both players guess the SAME puzzle generated by the algorithm

    def two_player_mode(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        back_btn = tk.Button(self.root, text="← BACK TO MENU", font=('Arial', 10),
                            bg='#95a5a6', fg='white', command=self.create_main_menu,
                            relief=tk.FLAT, cursor='hand2')
        back_btn.pack(anchor='nw', padx=10, pady=5)

        title = tk.Label(self.root, text="TWO PLAYER MODE", font=('Arial', 24, 'bold'),
                        fg='#ecf0f1', bg='#2c3e50')
        title.pack(pady=10)

        info = tk.Label(self.root, text="Computer picks missing number using Transform & Conquer\nBoth players guess who can find it first!",
                       font=('Arial', 12), fg='#f1c40f', bg='#2c3e50')
        info.pack(pady=10)

        # Generate puzzle using algorithm
        self.number_list = generate_99_random_numbers()
        self.missing_number = find_missing_transform_conquer(self.number_list)

        start_btn = tk.Button(self.root, text="START GAME", font=('Arial', 14, 'bold'),
                             bg='#27ae60', fg='white', padx=30, pady=10,
                             command=self.show_two_player_puzzle, cursor='hand2')
        start_btn.pack(pady=20)

    def show_two_player_puzzle(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        back_btn = tk.Button(self.root, text="← BACK TO MENU", font=('Arial', 10),
                            bg='#95a5a6', fg='white', command=self.create_main_menu,
                            relief=tk.FLAT, cursor='hand2')
        back_btn.pack(anchor='nw', padx=10, pady=5)

        title = tk.Label(self.root, text="TWO PLAYER MODE - BOTH PLAYERS GUESS",
                        font=('Arial', 20, 'bold'), fg='#ecf0f1', bg='#2c3e50')
        title.pack(pady=10)

        # Display grid
        grid_frame = tk.Frame(self.root, bg='#34495e')
        grid_frame.pack(pady=20)

        index = 0
        for row in range(7):
            row_frame = tk.Frame(grid_frame, bg='#34495e')
            row_frame.pack()
            for col in range(15):
                if index < 99:
                    cell = tk.Label(row_frame, text=str(self.number_list[index]),
                                   font=('Courier', 9), width=4, height=1,
                                   relief=tk.RIDGE, bg='#ecf0f1')
                    cell.pack(side=tk.LEFT, padx=1, pady=1)
                    index += 1

        guess_frame = tk.Frame(self.root, bg='#2c3e50')
        guess_frame.pack(pady=20)

        tk.Label(guess_frame, text="[PLAYER 1] Enter your guess:",
                font=('Arial', 12), fg='white', bg='#2c3e50').pack()

        self.p1_entry = tk.Entry(guess_frame, font=('Arial', 14), width=10, justify='center')
        self.p1_entry.pack(pady=5)

        tk.Label(guess_frame, text="[PLAYER 2] Enter your guess:",
                font=('Arial', 12), fg='white', bg='#2c3e50').pack(pady=(10,0))

        self.p2_entry = tk.Entry(guess_frame, font=('Arial', 14), width=10, justify='center')
        self.p2_entry.pack(pady=5)

        submit_btn = tk.Button(guess_frame, text="SUBMIT GUESSES", font=('Arial', 12, 'bold'),
                              bg='#27ae60', fg='white', padx=20, pady=5,
                              command=self.check_two_player_guesses, cursor='hand2')
        submit_btn.pack(pady=10)

        # Show algorithm result after they guess
        self.algo_label = tk.Label(self.root, 
                                   text=f"Transform & Conquer algorithm found: {self.missing_number}",
                                   font=('Arial', 10), fg='#f1c40f', bg='#2c3e50')
        self.algo_label.pack(pady=10)

    def check_two_player_guesses(self):
        p1_text = self.p1_entry.get().strip()
        p2_text = self.p2_entry.get().strip()

        if not p1_text or not p2_text:
            messagebox.showerror("ERROR", "Both players must enter a guess!")
            return

        try:
            p1_guess = int(p1_text)
            p2_guess = int(p2_text)

            if p1_guess < 1 or p1_guess > 100 or p2_guess < 1 or p2_guess > 100:
                messagebox.showerror("ERROR", "Guesses must be between 1-100")
                return

            p1_correct = (p1_guess == self.missing_number)
            p2_correct = (p2_guess == self.missing_number)

            result_msg = f"The missing number was: {self.missing_number}\n\n"
            result_msg += f"Player 1 guessed: {p1_guess} {'✅' if p1_correct else '❌'}\n"
            result_msg += f"Player 2 guessed: {p2_guess} {'✅' if p2_correct else '❌'}\n\n"

            if p1_correct and p2_correct:
                result_msg += "🏆 TIE! Both players guessed correctly! 🏆\n+5 points to each player!"
                self.total_score += 10
            elif p1_correct:
                result_msg += "🎉 PLAYER 1 WINS! 🎉\n+10 points to Player 1!"
                self.total_score += 10
            elif p2_correct:
                result_msg += "🎉 PLAYER 2 WINS! 🎉\n+10 points to Player 2!"
                self.total_score += 10
            else:
                result_msg += "❌ BOTH WRONG! No one wins this round! ❌"

            self.rounds_count += 1
            self.update_score_display()

            messagebox.showinfo("RESULTS", result_msg)

            answer = messagebox.askyesno("PLAY AGAIN?", "Would you like to play another round?")
            if answer:
                self.two_player_mode()
            else:
                self.create_main_menu()

        except ValueError:
            messagebox.showerror("ERROR", "Please enter valid numbers")

    def show_instructions(self):
        instructions = """🎮 MISSING NUMBER GAME 🎮

Based on Puzzle #51 from Algorithmic Puzzles
by Levitin & Levitin (2011)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRANSFORM & CONQUER ALGORITHM:
1. Sum all numbers keeping only last two digits
2. Let j = last two digits of total sum
3. Formula: 
   - If j == 50 → missing = 100
   - If j <= 49 → missing = 50 - j
   - If j >= 50 → missing = 150 - j

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MODES:

🎯 EASY MODE: Numbers appear one by one, no timer

⚡ CHALLENGE MODE: All numbers in grid with timer
   Round 1: 20 seconds | Round 2: 15 seconds | Round 3: 10 seconds

👥 TWO PLAYER MODE: Computer picks missing number using algorithm
   Both players guess! Whoever is correct wins.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The computer uses Transform & Conquer internally!
Good luck!"""
        messagebox.showinfo("INSTRUCTIONS", instructions)

    def exit_game(self):
        if messagebox.askyesno("Exit", f"Final Score: {self.total_score}\nThanks for playing!\n\nExit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = MissingNumberGame(root)
    root.mainloop()