class Plants:
    def __init__(self, name: str, height: float, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.old} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.old += 1


def main() -> None:
    Rose = Plants("Rose", 25, 30)
    print("=== Day 1 ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.old} days old")
    i = 1
    for i in range(6):
        i += 1
        Rose.grow()
        Rose.age()
        print(f"=== Day {i} ===")
        Rose.show()
    print(f"Growth this week: +{i}cm")


if __name__ == "__main__":
    main()
