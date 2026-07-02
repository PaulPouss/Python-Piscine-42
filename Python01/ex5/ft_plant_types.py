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
            self._height = round(height_temp)

    def set_age(self, age_temp: int) -> None:
        if (age_temp < self._old):
            print(f"Invalid operation attempted: {age_temp} days [REJECTED]")
            print("Security: Can not rejuvenate")
        else:
            self._old = age_temp

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._old += 1

    def get_height(self) -> None:
        print(f"Current height of {self.name}: {self._height}cm")

    def get_age(self) -> None:
        print(f"Current age of {self.name}: {self._old} days")

    def get_status(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._old}days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.color: str = color
        self.blooming: bool = False

    def bloom(self) -> None:
        if not self.blooming:
            self.blooming = True

    def get_status(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print("Rose is blooming beautifully!")


class tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.diameter = trunk_diameter

    def cast_shadow(self) -> None:
        print(f"Tree {self.name} produces a shade of", end="")
        print(f"{self._height}cm long and {self.diameter}cm wide.")

    def get_status(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Trunk diameter: {self.diameter}")


class vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str) -> None:
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.harvest_season = harvest_season
        self.nutrinional_value = 0

    def grow(self) -> None:
        temp_height = self._height + 2.1
        self.set_height(temp_height)

    def age(self) -> None:
        temp_age = self._old + 1
        self.set_age(temp_age)
        self.nutrinional_value += 1

    def get_status(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutrinional_value}")


def main():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.get_status()
    rose.bloom()
    print("")
    print("=== Tree")
    oak = tree("Oak", 200, 365, 5)
    oak.get_status()
    print("[asking the oak to produce shade]")
    oak.cast_shadow()
    print("")
    print("=== Vegetable")
    tomato = vegetable("Tomato", 5, 10, "April")
    tomato.get_status()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        i += 1
        tomato.grow()
        tomato.age()
    tomato.get_status()


if __name__ == "__main__":
    main()
