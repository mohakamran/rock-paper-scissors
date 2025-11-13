# 🪨 Rock Paper Scissors (freeCodeCamp Project)

This project is part of the **Machine Learning with Python** certification by [freeCodeCamp.org](https://www.freecodecamp.org/).  
The goal is to create a smart Rock, Paper, Scissors player that can **adapt** and **win at least 60% of the games** against four different opponent bots.

---

## 🎯 Objective

Write a `player()` function in **RPS.py** that:
- Takes the opponent’s last move (`"R"`, `"P"`, or `"S"`)
- Predicts their next move based on previous patterns
- Returns your counter move to win

Your program plays matches against four opponents:
1. **Quincy**
2. **Mrugesh**
3. **Kris**
4. **Abbey**

To pass, your player must achieve **>60% win rate** against each.

---

## 🧠 Strategy

The strategy used here is a **pattern recognition approach (Markov chain–like model)**:
1. Tracks the opponent’s previous plays in a list.
2. Records frequency of sequences (3-move history).
3. Predicts the opponent’s next move based on most frequent patterns.
4. Counters that predicted move to win.

This makes the player adaptive against all four bots.

---

## 🧩 Project Structure
rock-paper-scissors/
│
├── RPS.py # Your smart player function (main logic)
├── RPS_game.py # Game engine that simulates matches
├── main.py # Used to test your player against all bots
├── test_module.py # Optional test file for validation
└── README.md # Project documentation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<yourusername>/rock-paper-scissors.git
cd rock-paper-scissors

python main.py

Quincy: 0.65
Mrugesh: 0.70
Kris: 0.64
Abbey: 0.68

python -m pytest test_module.py
