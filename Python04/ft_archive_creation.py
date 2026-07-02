import sys
from typing import TextIO


def modificate_content(content: str) -> str:
    content = content.replace("\n", "#\n")
    return content


def create_new_file(new_content: str) -> None:
    new_file_name: str = input("Enter new file name (or empty):")
    if not new_file_name:
        new_file_name = sys.argv[1]
    new_file: TextIO = open(new_file_name, "w")
    print(f"Saving data  to '{new_file_name}'")
    new_file.write(new_content)
    print(f"Data saved in file '{new_file_name}'")
    put_content(new_content)


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
    new_content: str = modificate_content(content)
    create_new_file(new_content)
    return True


def main() -> None:
    if not check_file():
        return


if __name__ == "__main__":
    main()
