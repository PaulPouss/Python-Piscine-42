import sys


def verif_arguments() -> bool:
    result: bool = True
    if len(sys.argv) < 2:
        result = False
        return result
    for i in range(1, len(sys.argv)):
        try:
            int(sys.argv[i])
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
            result = False
    return result


def analyse_stats() -> None:
    Score: list[int] = []
    i: int = 1
    while i < len(sys.argv):
        Score.append(int(sys.argv[i]))
        i += 1
    print(f"Scores processed: {Score}")
    print(f"Total score: {sum(Score)}")
    print(f"Average score: {sum(Score) / len(Score)}")
    print(f"High score: {max(Score)}")
    print(f"Low score: {min(Score)}")
    print(f"Score range: {max(Score) - min(Score)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    if not verif_arguments():
        print("No scores provided. Usage: python3", end="")
        print(" ft_score_analytics.py <score1> <score2> ...")
        return
    analyse_stats()


if __name__ == "__main__":
    main()
