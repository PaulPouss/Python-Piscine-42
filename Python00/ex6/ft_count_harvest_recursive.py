def ft_count_harvest_recursive(i: int = 1, harvest: int =
                               int(input("Days until harvest: "))):
    if (i == harvest):
        print(f"Day {i}")
        print("Harvest time!")
    else:
        print(f"Day {i}")
        i += 1
        ft_count_harvest_recursive(i, harvest)
