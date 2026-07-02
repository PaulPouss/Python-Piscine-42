def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        result = int(temp_str)
        return result
    except ValueError:
        print("Value error")
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
