def ft_count_harvest_iterative():
    i = 1
    harvest = int(input("Days until harvest: "))
    for i in range(1, harvest + 1):
        print(f"Day {i}")
    print("Harvest time !")
