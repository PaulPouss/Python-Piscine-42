import sys
inventory: dict = dict()


class DoubleError(Exception):
    def __init__(self, message: str =
                 "Already existing piece of inventory") -> None:
        self.message = message

    def put_error(self):
        print(self.message)


def verif_repetition() -> None:
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        try:
            cle, valeur = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")

        try:
            if cle in inventory:
                raise DoubleError(f"Redundant item '{cle}' - discarding")
            inventory[cle] = int(valeur)
        except ValueError:
            print(f"Quantity error for '{cle}'", end="")
            print(f": invalid literal for int() with base 10: '{valeur}'")
        except DoubleError as error:
            error.put_error()


def get_inventory_keys() -> None:
    if len(sys.argv) < 2:
        print("No inventory provided !")
    else:
        verif_repetition()
    print(f"Got inventory: {inventory}")
    print("Item list: ", list(inventory.keys()))


def get_statistics() -> None:
    total: int = 0
    total_key: int = 0
    for key in inventory:
        total = total + inventory[key]
        total_key += 1
    print(f"Total quantity of the {total_key} items: {total}")
    for key in inventory:
        temp_num: float = round(inventory[key] / total * 100, 1)
        print(f"Item {key} represents: {temp_num}%")
    cle_max = max(inventory, key=lambda k: inventory.get(k, 0))
    cle_min = min(inventory, key=lambda k: inventory.get(k, 0))
    print(f"Item most abundant: {cle_max} ", end="")
    print(f"with quantity {inventory[cle_max]}")
    print(f"Item least abundant: {cle_min} ", end="")
    print(f"with quantity {inventory[cle_min]}")


def update_inventory() -> None:
    inventory.update({"magic item": 1})
    print(f"Inventory updated: {inventory}")


def main() -> None:
    get_inventory_keys()
    get_statistics()
    update_inventory()


if __name__ == "__main__":
    main()
