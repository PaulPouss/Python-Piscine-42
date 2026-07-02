class TemperatureError(Exception):
    def __init__(self, temp: int, message: str =
                 "Temperature is not suitable for plants") -> None:
        self.temp = temp
        self.message = message


# TE = TemperatureError(96)
# print(TE.temp)
# print(TE.message)
def input_temperature(user_input: str) -> int:
    print(f"Input data is {user_input} ")
    try:
        temp_input = int(user_input)
        if not (0 <= temp_input <= 40):
            raise TemperatureError(temp_input)
        return temp_input
    except ValueError:
        print("Value error")
        return False
    except TemperatureError as error_temp:
        print(error_temp.message)
        return False


def test_temperature() -> None:
    input_temperature("abc")
    input_temperature("25")
    input_temperature("50")
    input_temperature("100")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
