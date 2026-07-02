import ex0
from ex0.create_creatures import Creature, CreatureFactory


def testing_fire_factory() -> None:
    creature_1: Creature = ex0.create_creatures.FlameFactory.create_base()
    creature_1.attack()


def main() -> None:
    testing_fire_factory()


if __name__ == "__main__":
    main()
