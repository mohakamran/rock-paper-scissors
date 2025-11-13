# test_module.py
# -------------------------------------------
# This file will be used by freeCodeCamp to verify your code.
# -------------------------------------------
from RPS import player
from RPS_game import play, quincy, mrugesh, kris, abbey

def test_player():
    assert play(player, quincy, 1000) > 0.60
    assert play(player, mrugesh, 1000) > 0.60
    assert play(player, kris, 1000) > 0.60
    assert play(player, abbey, 1000) > 0.60
