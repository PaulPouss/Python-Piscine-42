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


def main() -> None:
    try:
        print("Testing Plant Errors...")
        test_plant_error()
    except PlantError as Plant_error:
        Plant_error.puterror()
    try:
        print("Testing Water Errors...")
        test_water_errors()
    except WaterError as Water_error:
        Water_error.puterror()
        print("Testing catching all garden errors...")
    for index in range(2):
        try:
            test_garden_error(index)
        except GardenError as global_error:
            global_error.puterror()


if __name__ == "__main__":
    main()
