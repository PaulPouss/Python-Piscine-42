from typing import TextIO


def secure_archive(file_name: str, operation: int,
                   new_content: str = "") -> tuple[bool, str]:
    if not file_name:
        return (False, "Please write a file name")
    if operation == 0:
        try:
            file_obj: TextIO = open(file_name, "r")
        except FileNotFoundError:
            return (False,
                    f"[Errno 2] No such file or directory: '{file_name}'")
        except PermissionError:
            return (False,
                    f"Errno 13] Permission denied: '{file_name}'")
        content: str = file_obj.read()
        file_obj.close()
        return (True, content)
    elif operation == 1:
        try:
            file_obj = open("file_name", "w")
        except FileNotFoundError:
            return (False,
                    f"[Errno 2] No such file or directory: '{file_name}'")
        except PermissionError:
            return (False, f"Errno 13] Permission denied: '{file_name}'")
        file_obj.write(new_content)
        file_obj.close()
        return (True, "Content successfully written to file")
    else:
        return (False, "please enter a command")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 0))
    print("")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 0))
    print("")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("text.txt", 0))
    print("")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test.txt", 1,
                         "Not all of those ho wanders are lost"))


if __name__ == "__main__":
    main()
