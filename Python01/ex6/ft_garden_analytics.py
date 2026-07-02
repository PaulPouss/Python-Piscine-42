class Plant:
    def __init__(self, name: str):
        self.name = name
        self._height: float = 0
        self._old = 0
        self.statistics = Plant.stats()

    class stats():
        def __init__(self):
            self.grew = 0
            self.aged = 0
            self.showed = 0

        def increase_grow(self):
            self.grew += 1

        def increase_age(self):
            self.aged += 1

        def increase_show(self):
            self.showed += 1

        def show_stats(self):
            print(f"Stats: {self.grew} grow, {self.aged} age", end="")
            print(f", {self.showed} show")

    @classmethod
    def create_anonymous(cls):
        return (Plant("anonymous"))

    def set_height(self, height_temp: float):
        if (height_temp < 0):
            print(f"Invalid operation attempted: {height_temp}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("")
            return
        else:
            self._height = round(height_temp)

    def set_age(self, age_temp: int):
        if (age_temp < self._old):
            print(f"Invalid operation attempted: {age_temp} days [REJECTED]")
            print("Security: Can not rejuvenate")
        else:
            self._old = age_temp

    def grow(self, value: float):
        self._height = self._height + value
        self.statistics.increase_grow()

    def age(self, value: int):
        self._old += value
        self.statistics.increase_age()

    def get_height(self):
        print(f"Current height of {self.name}: {self._height}cm")

    def show(self):
        print(f"Current age of {self.name}: {self._old} days")

    def get_status(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
        self.statistics.increase_show()

    @staticmethod
    def check_year_old(age: int):
        print(f"Is {age} days more than a year ? -> ", end="")
        if (age < 365):
            print("False")
        else:
            print("True")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.color = color
        self.blooming = False

    def bloom(self):
        if not self.blooming:
            self.blooming = True

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print("Rose is blooming beautifully!")
        self.statistics.increase_show()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 seeds: int):
        super().__init__(name, height, age, color)
        self.seeds_held = seeds

    def bloom_seed(self):
        self.bloom()
        self.seeds_held += 42

    def show_seed(self):
        self.show()
        print(f"Seeds: {self.seeds_held}")


class tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.diameter = trunk_diameter
        self.shade_done = 0

    def show_shade(self):
        print(f"{self.shade_done} shade")

    def cast_shadow(self):
        print(f"Tree {self.name} produces a shade of", end="")
        print(f"{self._height}cm long and {self.diameter}cm wide.")
        self.shade_done += 1

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Trunk diameter: {self.diameter}")
        self.statistics.increase_show()


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year_old(30)
    Plant.check_year_old(400)
    print("")
    rose = Flower("Rose", 15, 10, "red")
    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    rose.statistics.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(8)
    rose.show()
    print("[statistics for Rose]")
    rose.statistics.show_stats()
    print("")
    print("=== Tree")
    oak = tree("Oak", 200, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    oak.statistics.show_stats()
    oak.show_shade()
    print("[asking the oak to produce shade]")
    oak.cast_shadow()
    print("[statistics for Oak]")
    oak.statistics.show_stats()
    oak.show_shade()
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", 0)
    sunflower.show_seed()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom_seed()
    sunflower.show_seed()
    print("[statistics for Sunflower]")
    sunflower.statistics.show_stats()
    print("")
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.get_status()
    print("[statistics for Unknown plant]")
    anonymous.statistics.show_stats()


if __name__ == "__main__":
    main()
