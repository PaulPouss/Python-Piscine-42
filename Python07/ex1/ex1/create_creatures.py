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


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


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


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str = "Sproutling", type: str = "Grass"):
        super().__init__(name, type)

    def attack(self):
        print("Sproutling uses Vine Whip!")

    def heal(self):
        print("Sproutling heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str = "Bloumelle", type: str = "Grass/fairy"):
        super().__init__(name, type)

    def attack(self):
        print("Bloomelle uses Petal Dance!")

    def heal(self):
        print("Bloomelle heals itself and others for a large amount")


class HealingFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling", type: str = "Normal"):
        super().__init__(name, type)

    def attack(self):
        print("Shiftling attacks normally.")
