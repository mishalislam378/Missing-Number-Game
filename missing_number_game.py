import random
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_99_random_numbers():
    """
    Generate 99 random numbers from 1 to 100.
    One number is randomly missing.
    The computer has NO IDEA which number is missing.
    """
    all_numbers = list(range(1, 101))
    random.shuffle(all_numbers)
    return all_numbers[:99]

def ask_play_again():
    """Ask user what to do after game ends"""
    print("\n" + "-"*40)
    print("What would you like to do?")
    print("1. Play Again (same mode)")
    print("2. Back to Main Menu")
    print("3. Exit Game")
    print("-"*40)
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        return "play_again"
    elif choice == '2':
        return "main_menu"
    elif choice == '3':
        return "exit"
    else:
        return "main_menu"

# ========== TRANSFORM & CONQUER ALGORITHM ==========

def find_missing_transform_conquer(number_list):
    """
    Transform & Conquer algorithm from Assignment #3
    Uses last two digits method (mod 100) as given in the book
    
    This is the ONLY way the computer knows the missing number.
    No cheating. 
    """
    j_last_two = 0
    
    # Sum all numbers and keep only last two digits
    for num in number_list:
        j_last_two = (j_last_two + num) % 100
    
    # Apply formula from the book
    if j_last_two == 50:
        return 100
    elif j_last_two <= 49:
        return 50 - j_last_two
    else:
        return 150 - j_last_two

# ========== EASY MODE ==========

def easy_mode():
    global total_score, rounds_count
    
    while True:
        print("\n" + "="*50)
        print("EASY MODE - Numbers appear one by one")
        print("="*50)
        print("Computer uses Transform & Conquer algorithm")
        print("+10 points for correct answer")
        print("="*50)
        input("Press Enter when ready...")
        
        # Generate 99 random numbers 
        number_list = generate_99_random_numbers()
        
        # Computer finds missing number using Transform & Conquer ONLY
        missing_number = find_missing_transform_conquer(number_list)
        
        clear_screen()
        print("\n--- Numbers will appear one by one ---\n")
        
        for position in range(99):
            clear_screen()
            print(f"Number {position+1}: {number_list[position]}")
            time.sleep(0.9)
        
        user_guess = input("\nWhat number is missing? ")
        
        try:
            user_guess = int(user_guess)
            if user_guess == missing_number:
                print(f"\n✅ CORRECT! The missing number was {missing_number}")
                total_score += 10
                print(f"+10 points! Total score: {total_score}")
            else:
                print(f"\n❌ WRONG! The missing number was {missing_number}")
        except:
            print(f"\n❌ Invalid input! The missing number was {missing_number}")
        
        rounds_count += 1
        
        action = ask_play_again()
        if action == "play_again":
            continue
        elif action == "main_menu":
            break
        elif action == "exit":
            print(f"\nFinal Score: {total_score}")
            print("Thanks for playing!")
            exit()

# ========== CHALLENGE MODE ==========

def challenge_mode():
    global total_score, rounds_count
    
    while True:
        print("\n" + "="*50)
        print("CHALLENGE MODE - BEAT THE CLOCK!")
        print("="*50)
        print("Round 1: 20 seconds")
        print("Round 2: 15 seconds")
        print("Round 3: 10 seconds")
        print("Complete all 3 rounds to WIN!")
        print("="*50)
        input("Press Enter to start...")
        
        time_limits = [20, 15, 10]
        round_won = 0
        game_over = False
        
        for current_round in range(3):
            if game_over:
                break
                
            time_limit = time_limits[current_round]
            
            number_list = generate_99_random_numbers()
            missing_number = find_missing_transform_conquer(number_list)
            
            clear_screen()
            print("\n" + "="*40)
            print(f"ROUND {current_round + 1} - {time_limit} seconds")
            print("="*40)
            
            # Display grid (5 rows x 20 columns = 100 cells, last is ??)
            index = 0
            for row in range(5):
                line = ""
                for col in range(20):
                    if index < 99:
                        line += f"{number_list[index]:3d} "
                        index += 1
                    else:
                        line += " ?? "
                print(line)
            
            print("\n" + "-"*40)
            print(f"You have {time_limit} seconds. GO!")
            
            start_time = time.time()
            user_guess = input("\nMissing number is: ")
            end_time = time.time()
            time_taken = end_time - start_time
            
            if time_taken > time_limit:
                print(f"\n⏰ TIME'S UP! You took {time_taken:.1f} seconds")
                print(f"The missing number was {missing_number}")
                print(f"\nGAME OVER! You completed {round_won} out of 3 rounds")
                game_over = True
                break
            else:
                try:
                    user_guess = int(user_guess)
                    if user_guess == missing_number:
                        print(f"\n✅ CORRECT! {time_taken:.1f} seconds")
                        round_won += 1
                        if current_round == 2:
                            print("\n" + "="*40)
                            print("🏆 YOU ARE THE WINNER! 🏆")
                            print("="*40)
                            print(f"Completed all 3 rounds!")
                            total_score += 50
                            print(f"+50 BONUS POINTS! Total: {total_score}")
                        else:
                            print(f"\n+10 points for passing round {current_round + 1}")
                            total_score += 10
                            input("\nPress Enter for next round...")
                    else:
                        print(f"\n❌ WRONG! The missing number was {missing_number}")
                        print(f"\nGAME OVER! You completed {round_won} out of 3 rounds")
                        game_over = True
                        break
                except:
                    print(f"\n❌ Invalid input! The missing number was {missing_number}")
                    print(f"\nGAME OVER! You completed {round_won} out of 3 rounds")
                    game_over = True
                    break
        
        rounds_count += 1
        print(f"\nTotal score: {total_score}")
        
        action = ask_play_again()
        if action == "play_again":
            continue
        elif action == "main_menu":
            break
        elif action == "exit":
            print(f"\nFinal Score: {total_score}")
            print("Thanks for playing!")
            exit()

# ========== TWO PLAYER MODE ==========

def two_player_mode():
    global total_score, rounds_count
    
    while True:
        print("\n" + "="*50)
        print("TWO PLAYER MODE - WITH 30 SECOND TIMER!")
        print("="*50)
        print("Computer picks missing number using Transform & Conquer")
        print("Both players guess who can find it first!")
        print("="*50)
        input("Press Enter to start...")
        
        # Generate 99 random numbers (computer picks, both players don't know)
        number_list = generate_99_random_numbers()
        
        # Computer finds missing number using Transform & Conquer ONLY
        missing_number = find_missing_transform_conquer(number_list)
        
        clear_screen()
        
        print("\n[BOTH PLAYERS]")
        print("Here are 99 numbers. One number is missing.")
        print("Both players guess within 30 seconds!\n")
        
        # Display numbers in grid
        for i in range(99):
            print(f"{number_list[i]:4d}", end=" ")
            if (i + 1) % 15 == 0:
                print()
        
        print("\n" + "-"*40)
        print("⏱️ TIMER STARTED! 30 seconds to guess ⏱️")
        
        start_time = time.time()
        
        p1_guess = input("\n[PLAYER 1] What number is missing? ")
        p2_guess = input("[PLAYER 2] What number is missing? ")
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        print("\n" + "="*50)
        print(f"The missing number was: {missing_number}")
        print("="*50)
        
        if time_taken > 30:
            print("⏰ TIME'S UP! Both players took too long!")
        else:
            try:
                p1_guess = int(p1_guess)
                p2_guess = int(p2_guess)
                
                p1_correct = (p1_guess == missing_number)
                p2_correct = (p2_guess == missing_number)
                
                if p1_correct and p2_correct:
                    print("🏆 TIE! Both players guessed correctly!")
                    total_score += 10
                    print("+10 points to total score!")
                elif p1_correct:
                    print("🎉 PLAYER 1 WINS! Correct guess!")
                    total_score += 10
                    print("+10 points to total score!")
                elif p2_correct:
                    print("🎉 PLAYER 2 WINS! Correct guess!")
                    total_score += 10
                    print("+10 points to total score!")
                else:
                    print("❌ BOTH WRONG! No one wins this round!")
                    print(f"Player 1 guessed: {p1_guess}")
                    print(f"Player 2 guessed: {p2_guess}")
            except:
                print("❌ Invalid input! Round cancelled!")
        
        rounds_count += 1
        print(f"\nTotal Score: {total_score}")
        
        action = ask_play_again()
        if action == "play_again":
            continue
        elif action == "main_menu":
            break
        elif action == "exit":
            print(f"\nFinal Score: {total_score}")
            print("Thanks for playing!")
            exit()

# ========== SCORE AND HELP ==========

def show_scores():
    print("\n" + "="*50)
    print("SCOREBOARD")
    print("="*50)
    print(f"Total Score: {total_score}")
    print(f"Rounds Played: {rounds_count}")
    if rounds_count > 0:
        print(f"Average Score: {total_score/rounds_count:.1f}")
    input("\nPress Enter to continue...")

def show_help():
    print("\n" + "="*50)
    print("INSTRUCTIONS - Transform & Conquer Algorithm")
    print("="*50)
    print("""
    MISSING NUMBER GAME - Based on Puzzle #51
    
    ALGORITHM FROM THE BOOK (Levitin & Levitin, 2011):
    
    TRANSFORM & CONQUER METHOD:
    1. Sum all 99 numbers but keep ONLY the last two digits
       (Use modulo 100 after each addition)
    
    2. Let j = last two digits of total sum
    
    3. Apply formula:
       - If j == 50  → missing number = 100
       - If j <= 49  → missing number = 50 - j
       - If j >= 50  → missing number = 150 - j
    
    EXAMPLE:
    If sum of numbers ends with 48, then j = 48
    Since 48 <= 49, missing = 50 - 48 = 2
    
    GAME MODES:
    
    1. EASY MODE - Numbers appear one by one
       +10 points for correct answer
    
    2. CHALLENGE MODE - Beat the progressive timer!
       Round 1: 20 seconds → +10 points
       Round 2: 15 seconds → +10 points
       Round 3: 10 seconds → +10 points + 50 BONUS
    
    3. TWO PLAYER MODE - Player 1 picks, Player 2 guesses
       Player 2 has 30 seconds to guess!
       +10 points if Player 2 is correct
    
    The computer uses Transform & Conquer internally to find
    the missing number. NO CHEATING - algorithm only!
    """)
    input("\nPress Enter to continue...")

# ========== MAIN GAME LOOP ==========

total_score = 0
rounds_count = 0

while True:
    clear_screen()
    print("\n" + "="*50)
    print("MISSING NUMBER GAME")
    print("Using Transform & Conquer Algorithm (Assignment #3)")
    print("="*50)
    print(f"Score: {total_score}    Rounds: {rounds_count}")
    print("="*50)
    print("\n1. Easy Mode (No timer)")
    print("2. Challenge Mode (20s → 15s → 10s)")
    print("3. Two Player Mode (30s timer)")
    print("4. View Scores")
    print("5. Instructions")
    print("6. Exit")
    print("\n" + "="*50)
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        easy_mode()
    elif choice == '2':
        challenge_mode()
    elif choice == '3':
        two_player_mode()
    elif choice == '4':
        show_scores()
    elif choice == '5':
        show_help()
    elif choice == '6':
        print("\n" + "="*50)
        print(f"Final Score: {total_score}")
        print("Thanks for playing!")
        print("="*50)
        break
    else:
        print("\nInvalid choice! Enter 1-6 only.")
        time.sleep(1.5)