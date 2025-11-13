# RPS_game.py
# -------------------------------------------
# This file provides the play() function that simulates a match
# between two player functions.
# -------------------------------------------

import random

def play(player1, player2, num_games, verbose=False):
    """
    Simulate Rock, Paper, Scissors games between two player functions.
    """
    moves = ["R", "P", "S"]
    p1_prev = ""
    p2_prev = ""

    p1_score = 0
    p2_score = 0

    for _ in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if p1_move not in moves:
            p1_move = random.choice(moves)
        if p2_move not in moves:
            p2_move = random.choice(moves)

        if verbose:
            print(f"Player1: {p1_move}  |  Player2: {p2_move}")

        if p1_move == p2_move:
            pass  # Tie
        elif (
            (p1_move == "R" and p2_move == "S")
            or (p1_move == "S" and p2_move == "P")
            or (p1_move == "P" and p2_move == "R")
        ):
            p1_score += 1
        else:
            p2_score += 1

        p1_prev, p2_prev = p1_move, p2_move

    win_rate = p1_score / num_games
    if verbose:
        print(f"Player1 win rate: {win_rate:.2%}")

    return win_rate

# --- Opponent bots ---

def quincy(prev_play, opponent_history=[]):
    choices = ["R", "P", "S", "P", "S"]
    if prev_play:
        opponent_history.append(prev_play)
    return choices[len(opponent_history) % len(choices)]

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    if len(opponent_history) < 5:
        return "R"
    most_common = max(set(opponent_history[-5:]), key=opponent_history[-5:].count)
    return ideal_response[most_common]

def kris(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    if not prev_play:
        return "R"
    return ideal_response[prev_play]

def abbey(prev_play, opponent_history=[], play_order={}):
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        last_two = "".join(opponent_history[-2:])
        play_order[last_two] = play_order.get(last_two, 0) + 1
        potential_plays = [
            opponent_history[-1] + "R",
            opponent_history[-1] + "P",
            opponent_history[-1] + "S",
        ]
        possible = {k: play_order.get(k, 0) for k in potential_plays}
        predicted_move = max(possible, key=possible.get)[-1]
        ideal_response = {"P": "S", "R": "P", "S": "R"}
        guess = ideal_response[predicted_move]

    return guess
