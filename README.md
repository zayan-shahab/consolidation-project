# Dice Game

A simple dice game for one or multiple players. The game involves rolling dice, making strategic decisions on re-rolls, and competing to achieve the highest score.

## Features
- Supports multiple players.
- Automatic dice rolling and scoring.
- Special conditions:
  - **TUPLE OUT**: If all three dice show the same value, the player scores 0 for the turn.
  - **Fixed Dice**: If at least two dice have the same value, the player cannot re-roll.
- Players can strategically choose which dice to re-roll.
- Configurable target score for winning.

---

## How to Play

1. **Setup**: Enter the number of players when prompted.
2. **Player Turn**:
   - Roll three dice automatically.
   - Decide whether to re-roll any of the dice or keep the current roll.
   - Repeat until:
     - The player decides not to re-roll.
     - A "TUPLE OUT" or "Fixed Dice" condition occurs.
   - The turn ends, and the score is added to the player's total.
3. **Winning**: The first player to reach or exceed the target score wins.

---

## Rules
1. **TUPLE OUT**: 
   - If all dice have the same value, the player's score for that turn is **0**.
2. **Fixed Dice**:
   - If at least two dice have the same value, the dice are "fixed," and the player cannot re-roll.
3. **Scoring**:
   - If neither condition occurs, the player's score is the sum of the dice values.

---
## How to Run

1. Clone the repository or download the game script.
2. Run the script using Python:
   ```bash
   python dice_game.py
