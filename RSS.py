# RPS.py
# -------------------------------------------
# This file defines the player function for the Rock, Paper, Scissors game.
# Your goal: create a smart player that wins at least 60% of the time
# against all four bots provided by freeCodeCamp.
# -------------------------------------------

def player(prev_play, opponent_history=[], play_order={}):
    """
    Rock Paper Scissors player function.
    Arguments:
      prev_play (str): Opponent's last move ("R", "P", or "S")
      opponent_history (list): Keeps track of opponent's previous moves
      play_order (dict): Tracks patterns of opponent plays

    Returns:
      str: The next move ("R", "P", or "S")
    """

    # Record opponent's last move
    if prev_play:
        opponent_history.append(prev_play)

    # Default move
    guess = "R"

    # Start predicting after a few rounds
    if len(opponent_history) > 3:
        # Get last 3 moves to find pattern
        last_three = "".join(opponent_history[-3:])
        play_order[last_three] = play_order.get(last_three, 0) + 1

        # Create possible sequences assuming next move could be R, P, or S
        potential_plays = [
            "".join(opponent_history[-2:]) + "R",
            "".join(opponent_history[-2:]) + "P",
            "".join(opponent_history[-2:]) + "S",
        ]

        # Count occurrences of these sequences
        possible = {k: play_order.get(k, 0) for k in potential_plays}

        # Predict opponent’s next move (most frequent following pattern)
        predicted_move = max(possible, key=possible.get)[-1]

        # Counter predicted move
        ideal_response = {"R": "P", "P": "S", "S": "R"}
        guess = ideal_response[predicted_move]

    return guess
