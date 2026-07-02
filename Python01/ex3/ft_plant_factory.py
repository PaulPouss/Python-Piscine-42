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


def main():
    rose = Plants("Rose", 25, 30)
    oak = Plants("Oak", 200, 365)
    cactus = Plants("Cactus", 5, 90)
    sunflower = Plants("Sunflower", 80, 45)
    fern = Plants("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    print("Created:", end="")
    rose.show()
    print("Created:", end="")
    oak.show()
    print("Created:", end="")
    cactus.show()
    print("Created:", end="")
    sunflower.show()
    print("Created:", end="")
    fern.show()
    print("Total plant created: 5")


if __name__ == "__main__":
    main()
