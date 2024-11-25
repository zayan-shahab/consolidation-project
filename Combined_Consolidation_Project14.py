import random

def roll_dice():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  dice3 = random.randint(1, 6)
  print(f"Dice rolled: {dice1}, {dice2}, {dice3}")
  return dice1, dice2, dice3

def is_tuple_out(dice):
  return dice[0] == dice[1] == dice[2]

def is_fixed(dice):
  return len(set(dice)) < 3

def calculate_score(dice):
  if is_tuple_out(dice):
    return 0
  else:
    return sum(dice)

def player_turn():
  dice = roll_dice()
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
    choice = input().lower()

    if choice == 'n':
      score += calculate_score(dice)
      break

    re_roll_dice = []
    for i in range(3):
      if input(f"Re-roll dice {i+1}? (y/n)").lower() == 'y':
        re_roll_dice.append(i)

    for i in re_roll_dice:
      dice[i] = random.randint(1, 6)
    print(f"Dice after re-roll: {dice}")

  return score

def main():
  num_players = int(input("Enter the number of players: "))
  scores = [0] * num_players
  current_player = 0

  while True:
    print(f"Player {current_player + 1}'s turn:")
    score = player_turn()
    scores[current_player] += score
    print(f"Player {current_player + 1}'s score: {scores[current_player]}")

    current_player = (current_player + 1) % num_players

    # Check for game end condition (e.g., reaching a target score)
    if any(score >= 50 for score in scores):
      break

  winner = scores.index(max(scores))
  print(f"Player {winner + 1} wins!")

if __name__ == "__main__":
  main()