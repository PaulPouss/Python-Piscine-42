def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        raise (ValueError)
    elif (operation_number == 1):
        raise (ZeroDivisionError)
    elif (operation_number == 2):
        raise (FileNotFoundError)
    elif (operation_number == 3):
        raise (TypeError)
    return


def test_error_types() -> None:
    for value in range(5):
        print(f"Testing operation {value}...")
        try:
            garden_operations(value)
            print("Operation completed successfully")
        except ValueError:
            print("Caught ValueError: ", end="")
            print("invalid literal for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotfoundError: ", end="")
            print("[Errno 2] No such file or directory: 'non/existent/file'")
        except TypeError:
            print("Caught TypeError: ", end="")
            print("can only concatenate str (not ""int"") to str")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
