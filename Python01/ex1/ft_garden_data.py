class Plants:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    rose = Plants("Rose", 25, 30)
    Sunflower = Plants("Sunflower", 80, 45)
    Cactus = Plants("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    Sunflower.show()
    Cactus.show()


if __name__ == "__main__":
    main()
