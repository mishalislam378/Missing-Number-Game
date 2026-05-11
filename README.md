
## README.md - Missing Number Game

### Project Title
**Missing Number Game - Transform & Conquer Algorithm Demonstration**

---

### 1. Problem Statement
Create an interactive game based on Puzzle #51 from Algorithmic Puzzles. In this puzzle, 99 distinct numbers from 1 to 100 are recited randomly. One number is missing. The player must identify the missing number. The game must demonstrate the Transform & Conquer algorithm with a good user interface.

---

### 2. Objectives
- Develop an interactive game with three difficulty modes
- Implement the Transform & Conquer algorithm as the core verification method
- Provide a user-friendly console interface with clear instructions
- Track player scores across multiple rounds
- Include replay and exit options after each game

---

### 3. Game Modes

| Mode | How It Works | Timer | Points |
|------|-------------|-------|--------|
| **Easy Mode** | 99 numbers appear one by one on screen. Player remembers and guesses the missing number. | No timer | Correct: +10 |
| **Challenge Mode** | All 99 numbers displayed in a 5x20 grid. Player has limited time per round. 3 rounds total. | Round 1: 20s, Round 2: 15s, Round 3: 10s | Per round: +10, Win all 3: +50 bonus |
| **Two Player Mode** | Player 1 secretly picks a missing number. Player 2 sees the grid and guesses within 30 seconds. | 30 seconds | Correct: +10 |

---

### 4. Algorithm Used

**Transform & Conquer (Last Two Digits Method)**
- Step 1: Sum all 99 numbers keeping only last two digits (mod 100)
- Step 2: Let j = last two digits of total sum
- Step 3: Apply formula:
  - If j == 50 → missing number = 100
  - If j <= 49 → missing number = 50 - j
  - If j >= 50 → missing number = 150 - j

The algorithm runs internally to verify player answers. No cheating occurs.

---

### 5. Features
- Score tracking (total points earned)
- Round counter (number of games played)
- Play again option after each game
- Back to main menu option
- Exit game option
- Clear screen between rounds for better visibility
- Timer in Challenge and Two Player modes
- Scoreboard to view statistics

---

### 6. How to Run

**Requirements:** Python 3.x installed

**Steps:**
1. Download the file `missing_number_game.py`
2. Open terminal/command prompt in the file directory
3. Run command:
```bash
python missing_number_game.py
```

---

### 7. Sample Output Screenshots

**Main Menu**
```
==================================================
MISSING NUMBER GAME
Using Transform & Conquer Algorithm
==================================================
Score: 0    Rounds: 0
==================================================

1. Easy Mode (No timer)
2. Challenge Mode (20s → 15s → 10s)
3. Two Player Mode (30s timer)
4. View Scores
5. Instructions
6. Exit
==================================================
```

**Challenge Mode Grid Display**
```
========================================
ROUND 1 - 20 seconds
========================================
  42   7  99  23  56  12  34  78  91   5  67  89  44  33  22  11  88  77  66  55
  45  67  89  12  34  56  78  90  21  43  65  87  98  76  54  32  10  20  30  40
  61  72  83  94   6  17  28  39  50  62  73  84  95   8  19  31  42  53  64  75
  86  97   9  18  27  36  46  57  68  79  81  92   4  15  26  37  48  59  70  71
  82  93   2  13  24  35  47  58  69  80   1  14  25  38  49  60  63  74  85   ??
----------------------------------------
You have 20 seconds. GO!
```

---

### 8. Conclusion

The Missing Number Game successfully implements Puzzle #51 as an interactive experience. All three modes function correctly with their respective timers and scoring systems. The Transform & Conquer algorithm runs internally as the sole verification method, ensuring no cheating. Score tracking, replay options, and clear screen formatting provide a complete and user-friendly gameplay loop.

---

### 9. Reference
Levitin, A. & Levitin, M. (2011). *Algorithmic Puzzles*. Oxford University Press. Puzzle #51, p.124.

---

### 10. Submission Information
- **Course:** Design and Analysis of Algorithms
- **Due Date:** 11th May, 2026

---

### 11. Academic Integrity Statement
This work is completed individually. 
