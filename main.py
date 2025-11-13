# main.py
# -------------------------------------------
# Run this file to test your player function
# against all provided bots.
# -------------------------------------------

from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

if __name__ == "__main__":
    print("Testing your player strategy...\n")

    print("Quincy:", play(player, quincy, 1000))
    print("Mrugesh:", play(player, mrugesh, 1000))
    print("Kris:", play(player, kris, 1000))
    print("Abbey:", play(player, abbey, 1000))
