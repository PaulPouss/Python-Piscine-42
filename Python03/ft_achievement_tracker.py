import random


achievements = [
    "First Steps",
    "First Blood",
    "Explorer",
    "Treasure Hunter",
    "Level Up",
    "Master Warrior",
    "Unstoppable",
    "Speed Runner",
    "Sharpshooter",
    "Untouchable",
    "Survivor",
    "Collector",
    "Secret Finder",
    "Lucky One",
    "Perfectionist",
    "Fearless",
    "Dungeon Master",
    "Boss Slayer",
    "Legendary Hero",
    "Ultimate Champion"
]


def get_player_achievments() -> None:
    Player1 = set(random.sample(
        achievements, random.randint(1, len(achievements))))
    print(f"Player Alice: {Player1}")
    print("")
    Player2 = set(random.sample(
        achievements, random.randint(1, len(achievements))))
    print(f"Player Bob: {Player2}")
    Player3 = set(random.sample(
        achievements, random.randint(1, len(achievements))))
    print("")
    print(f"Player Charlie: {Player3}")
    print("")
    Player4 = set(random.sample(
        achievements, random.randint(1, len(achievements))))
    print(f"Player Dylan: {Player4}")
    print("")
    all_achievements = Player1.union(Player2, Player3, Player4)
    print(f"All distincts achievements: {all_achievements}")
    print("")
    commun_achievements = Player1.intersection(Player2, Player3, Player4)
    if commun_achievements:
        print(f"Common achievements: {commun_achievements}")
    else:
        print("No common achievements")
        print("")
    Player1_dif = Player1.difference(Player2, Player3, Player4)
    print(f"Only Alice has: {Player1_dif}")
    Player2_dif = Player2.difference(Player1, Player3, Player4)
    print(f"Only Bob has: {Player2_dif}")
    Player3_dif = Player3.difference(Player2, Player1, Player4)
    print(f"Only Charlie has: {Player3_dif}")
    Player4_dif = Player4.difference(Player2, Player3, Player1)
    print(f"Only Dylan has: {Player4_dif}")
    print("")
    global_achievements = set(achievements)
    Player1_missing = global_achievements.difference(Player1)
    print(f"Alice is missing: {Player1_missing}")
    Player2_missing = global_achievements.difference(Player2)
    print(f"Bob is missing: {Player2_missing}")
    Player3_missing = global_achievements.difference(Player3)
    print(f"Charlie is missing: {Player3_missing}")
    Player4_missing = global_achievements.difference(Player4)
    print(f"Dylan is missing: {Player4_missing}")


def main() -> None:
    get_player_achievments()


if __name__ == "__main__":
    main()
