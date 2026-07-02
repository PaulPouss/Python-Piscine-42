def ft_plant_age():
    plant_age = 0
    plant_age = int(input("Enter plant age in days: "))
    if (plant_age > 60):
        print("Plant is ready to harvest !")
    else:
        print("Plant needs more time to grow.")
