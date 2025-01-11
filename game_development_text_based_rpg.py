# -*- coding: utf-8 -*-
"""Game Development: Text-Based RPG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HnCKjDmbtkOcnZsEvjSzCFOno5LuUSwM

Game Development: Text-Based RPG
"""

import random

def text_rpg():
    player_hp = 100
    monsters = {"Goblin": 20, "Orc": 40, "Dragon": 80}

    print("Welcome to the RPG game!")
    while player_hp > 0:
        encounter = random.choice(list(monsters.keys()))
        monster_hp = monsters[encounter]
        print(f"A wild {encounter} appears with {monster_hp} HP!")

        while monster_hp > 0 and player_hp > 0:
            action = input("Attack (a) or Run (r): ").strip().lower()
            if action == "a":
                damage = random.randint(5, 20)
                monster_hp -= damage
                print(f"You dealt {damage} damage. Monster HP: {max(0, monster_hp)}")

                if monster_hp > 0:
                    monster_damage = random.randint(10, 30)
                    player_hp -= monster_damage
                    print(f"The {encounter} hit you for {monster_damage}. Your HP: {max(0, player_hp)}")
            elif action == "r":
                print("You ran away!")
                break

        if player_hp <= 0:
            print("You died! Game Over.")
        elif monster_hp <= 0:
            print(f"You defeated the {encounter}!")
        else:
            print("You survived this encounter!")

text_rpg()