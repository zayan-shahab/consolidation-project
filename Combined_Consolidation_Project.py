import random

def roll_dice():
    """
    Rolls three dice and returns them as a tuple
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    print(f"Dice rolled: {dice1}, {dice2}, {dice3}")
    return dice1, dice2, dice3

def is_tuple_out(dice):
    """
    Checks if all dice have the same value, indicating a "tuple out"
    """
    return dice[0] == dice[1] == dice[2]

def is_fixed(dice):
    """
    Checks if at least two dice have the same value, indicating "fixed" dice.
    """
    return len(set(dice)) < 3

def calculate_score(dice):
    """
    Calculates the score based on the dice values.
    If all dice have the same value, the score is 0.
    Otherwise, the score is the sum of the dice.
    """
    if is_tuple_out(dice):
        return 0
    return sum(dice)

def get_yes_no(prompt):
     """
    Prompts the user for a yes or no response and validates the input.
    """
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response
        print("Please enter 'y' or 'n'.")

def player_turn():
    """
    Manages a single player's turn in the dice game.

    The player rolls three dice and decides whether to re-roll any dice
    or keep their current roll. The turn ends when the player chooses not
    to re-roll or certain conditions (like "TUPLE OUT") are met.
    """
    dice = roll_dice()
    dice = list(dice)  
    score = 0

    while True:
        if is_tuple_out(dice):
            print("TUPLE OUT! You score 0 points.")
            break

        if is_fixed(dice):
            print("Fixed dice. Cannot re-roll.")
            score += calculate_score(dice)
            break

        print("Do you want to re-roll any dice? (y/n)")
        if get_yes_no("") == 'n':
            score += calculate_score(dice)
            break

        re_roll_dice = []
        for i in range(3):
            print(f"Dice {i+1}: {dice[i]}")
            if get_yes_no(f"Re-roll dice {i+1}? (y/n) ") == 'y':
                re_roll_dice.append(i)

        for i in re_roll_dice:
            if 0 <= i < len(dice):
                dice[i] = random.randint(1, 6)
        print(f"Dice after re-roll: {dice}")

    return score

def main():
    """
    Manages the overall flow of the dice game.

    Prompts the user to enter the number of players, manages player turns,
    and determines the winner when a player reaches the target score.

    The game ends when a player reaches or exceeds the target score.
    """
    TARGET_SCORE = 50
    num_players = int(input("Enter the number of players: "))
    scores = [0] * num_players
    current_player = 0

    while True:
        print(f"Player {current_player + 1}'s turn:")
        score = player_turn()
        scores[current_player] += score
        print(f"Player {current_player + 1}'s score: {scores[current_player]}")

        if any(score >= TARGET_SCORE for score in scores):
            break

        current_player = (current_player + 1) % num_players

    winner = scores.index(max(scores))
    print(f"Player {winner + 1} wins!")

if __name__ == "__main__":
    main()
