import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        inp = input("enter coordonates as floats in format 'x y z': ").split()
        if len(inp) != 3:
            print("please unter exactly 3 values")
            continue
        try:
            x, y, z = map(float, inp)
            return (x, y, z)
        except ValueError:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===")
    tpl1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {tpl1}")
    print(f"It uncludes: X={tpl1[0]}, Y={tpl1[1]}, Z={tpl1[2]}")
    dist_tpl1: float = round(
        math.sqrt(tpl1[0] ** 2 + tpl1[1] ** 2 + tpl1[2] ** 2), 4)
    print(f"distance to center : {dist_tpl1}")
    print("")
    tpl2: tuple[float, float, float] = get_player_pos()
    print(f"Got a second tuple: {tpl2}")
    print(f"It uncludes: X={tpl2[0]}, Y={tpl2[1]}, Z={tpl2[2]}")
    dist_tpl2_tpl1: float = round(math.sqrt((tpl2[0] - tpl1[0]) ** 2 +
                                            (tpl2[1] - tpl1[1]) ** 2 +
                                            (tpl2[2] - tpl1[2]) ** 2), 4)
    print(f"distance between the 2 sets of coordinates : {dist_tpl2_tpl1}")


if __name__ == "__main__":
    main()
