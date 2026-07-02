from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def describe(self):
        print(f"{self.name} is a {self.type} type creature")

    @abstractmethod
    def attack(self):
        pass


class Flameling(Creature):
    def __init__(self, name: str = "Flameling", type: str = "fire"):
        super().__init__(name, type)

    def attack(self):
        print(f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon", type: str = "fire/flying"):
        super().__init__(name, type)

    def attack(self):
        print(f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub", type: str = "water"):
        super().__init__(name, type)

    def attack(self):
        print(f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self, name: str = "Torragon", type: str = "water"):
        super().__init__(name, type)

    def attack(self):
        print(f"{self.name} uses Hydro Pump!")


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
