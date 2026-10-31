import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players = ['Alice', 'bob', 'Charlie',
               'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    new_list = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {new_list}")
    cap_only = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {cap_only}\n")
    score_dict = {name: random.randint(0, 1000) for name in new_list}
    print(f"Score dict: {score_dict}")
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")
    high_scores = {key: score_dict[key]
                   for key in score_dict if score_dict[key] > average}
    print(f"High scores: {high_scores}")
