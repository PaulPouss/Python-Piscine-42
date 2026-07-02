from ex0.create_creatures import CreatureFactory, FlameFactory, AquaFactory


def create_base_and_evolved(factory: CreatureFactory) -> None:
    try:
        base_creature = factory.create_base()
        base_creature.describe()
        base_creature.attack()
    except AttributeError:
        print("Impossible to create base creature")
    try:
        evolved_creature = factory.create_evolved()
        evolved_creature.describe()
        evolved_creature.attack()
    except AttributeError:
        print("Impossible to create evolved creature")


def make_them_fight(factory_1: CreatureFactory,
                    factory_2: CreatureFactory) -> None:
    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()
    creature_1.describe()
    print("vs.")
    creature_2.describe()
    print("fight !")
    creature_1.attack()
    creature_2.attack()


if __name__ == "__main__":
    flameling = FlameFactory()
    aquabub = AquaFactory()
    print("testing factory")
    create_base_and_evolved(flameling)
    print("")
    print("testing factory")
    create_base_and_evolved(aquabub)
    print("")
    print("testing battle")
    make_them_fight(flameling, aquabub)
