import sys


def verif_arg() -> None:
    if len(sys.argv) < 2:
        print("No arguments provided !")
    else:
        print(f" Arguments received: {len(sys.argv)}")


def put_arguments() -> None:
    for i in range(1, len(sys.argv)):
        print(f" Argument {i}: {sys.argv[i]}")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    verif_arg()
    put_arguments()
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
