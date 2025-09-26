import os
import random

def winner(player):
    print(f"vyhral hrac {player}")
    
    wins[player - 1] += 1

def tie():
    print("remiza")

values = ["kamen", "papier", "noznice"]
wins = [0, 0]

games = int(input("zadajte pocet hier: "))

while games > 0:
    os.system("cls")

    result_1 = random.choice(values)
    result_2 = random.choice(values)

    print(f"hrac 1: {result_1}")
    print(f"hrac 2: {result_2}")

    match result_1:
        case "kamen":
            match result_2:
                case "kamen":
                    tie()
                case "papier":
                    winner(2)
                case "noznice":
                    winner(1)
        case "papier":
            match result_2:
                case "kamen":
                    winner(2)
                case "papier":
                    tie()
                case "noznice":
                    winner(2)
        case "noznice":
            match result_2:
                case "kamen":
                    winner(1)
                case "papier":
                    winner(2)
                case "noznice":
                    tie()

    input("stlacte akykolvek klaves pre pokracovanie")
    games -= 1

print(f"hrac 1: {wins[0]} vyhier")
print(f"hrac 2: {wins[1]} vyhier")