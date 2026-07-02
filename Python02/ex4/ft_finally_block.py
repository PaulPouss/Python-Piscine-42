class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message

    def puterror(self) -> None:
        print(f"Caught GardenError: {self.message}")


class PlantError(GardenError):
    def __init__(self, err_plant: str = "Caught PlantError", message: str =
                 "the tomato plant is wilting!"):
        self.err_plant = err_plant
        self.message = message

    def puterror(self) -> None:
        print(f"{self.err_plant}: {self.message}")


class WaterError(GardenError):
    def __init__(self, err_water: str = "Caught WaterError", message: str =
                 "Not enough water in the tank !"):
        self.err_water = err_water
        self.message = message

    def puterror(self) -> None:
        print(f"{self.err_water}: {self.message}")


def test_water_errors() -> None:

    for water_tank in range(10):
        if (water_tank == 7):
            raise WaterError()


def test_plant_error() -> None:

    for Tomato in range(25):
        if (Tomato == 22):
            raise PlantError()


def test_garden_error(index: int) -> None:
    if (index == 0):
        try:
            test_plant_error()
        except PlantError:
            raise GardenError("The tomato plant is wilting !")
    else:
        try:
            test_water_errors()
        except WaterError:
            raise GardenError("Not enough water in the tank !")


def water_plant(plant_name: str) -> None:
    if str.capitalize(plant_name) == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError("Caught PlantError: ",
                         f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("Opening watering system")
    try:
        water_plant("Tomato")
    except PlantError as plant_error:
        plant_error.puterror()
        print(".. ending tests and returning to main")
        return
    try:
        water_plant("lettuce")
    except PlantError as plant_error:
        plant_error.puterror()
        print(".. ending tests and returning to main")
        return
    try:
        water_plant("Carrots")
    except PlantError as plant_error:
        plant_error.puterror()
        print(".. ending tests and returning to main")
        return


def main() -> None:
    print("=== Garden Watering System ===")
    print("")
    print("Testing invalid plants...")
    test_watering_system()
    print("closing watering system")


if __name__ == "__main__":
    main()
