# -*- coding: utf-8 -*-
""". Probability: Monty Hall Simulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LFM2xmRi2xdtuSBoszl5cGvP8EJ8fIiW
"""

import random

def monty_hall_simulation(trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(trials):
        doors = [0, 0, 1]  # Two goats (0) and one car (1)
        random.shuffle(doors)

        player_choice = random.randint(0, 2)
        host_choice = next(i for i in range(3) if doors[i] == 0 and i != player_choice)

        # If the player switches
        switch_choice = next(i for i in range(3) if i != player_choice and i != host_choice)
        if doors[switch_choice] == 1:
            switch_wins += 1
        else:
            stay_wins += 1

    print(f"Switch Wins: {switch_wins}")
    print(f"Stay Wins: {stay_wins}")
    print(f"Switch Win Probability: {switch_wins / trials:.2f}")
    print(f"Stay Win Probability: {stay_wins / trials:.2f}")

# Example usage
trials = int(input("Enter the number of trials: "))
monty_hall_simulation(trials)