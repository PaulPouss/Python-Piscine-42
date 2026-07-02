import sys
from typing import TextIO


def put_content(content: str) -> None:
    print("---")
    print("")
    print(content)
    print("")
    print("---")


def check_file() -> bool:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return False
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file_obj: TextIO = open(sys.argv[1], "r")
    except FileNotFoundError:
        print(f"Error opening file '{sys.argv[1]}': ", end="")
        print(f"[Errno 2] No such file or directory: '{sys.argv[1]}'")
        return False
    except PermissionError:
        print(f"Error opening file '{sys.argv[1]}': ", end="")
        print(f"[Errno 13] Permission denied: '{sys.argv[1]}'")
        return False
    content: str = file_obj.read()
    file_obj.close()
    put_content(content)
    return True


def main() -> None:
    if not check_file():
        return


if __name__ == "__main__":
    main()
