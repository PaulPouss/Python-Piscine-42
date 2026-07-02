class Plant:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._height: float = 0
        self._old: int = 0

    def set_height(self, height_temp: float) -> None:
        if (height_temp < 0):
            print(f"Invalid operation attempted: {height_temp}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("")
            return
        else:
            self._height = height_temp
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age_temp: int) -> None:
        if (age_temp < self._old):
            print(f"Invalid operation attempted: {age_temp} days [REJECTED]")
            print("Security: Can not rejuvenate")
        else:
            self._old = age_temp
            print(f"Age updated: {self._old} days [OK]")
            print("")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._old += 1

    def get_height(self) -> None:
        print(f"Current height of {self.name}: {self._height}cm")

    def get_age(self) -> None:
        print(f"Current age of {self.name}: {self._old} days")

    def get_status(self) -> None:
        print(f"Current plant:{self.name} ({self._height}cm, {self._old}days)")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.get_status()


if __name__ == "__main__":
    main()
