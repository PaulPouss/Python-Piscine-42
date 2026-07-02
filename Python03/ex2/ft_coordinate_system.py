

def get_player_pos() -> tuple[int, int, int]:
    x = None
    y = None
    z = None
    
    return (x, y, z)


def main() -> None:
    tpl: tuple[int, int, int] = get_player_pos()
    print(f"{tpl}")


if __name__ == "__main__":
    main()
