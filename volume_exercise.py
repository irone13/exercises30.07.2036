volume = int(input("Enter volume : "))

match volume:
    case 1:
        v = "Very quiet"
    case 2:
        v = "Quiet"
    case 3 | 4 :
        v = "Low"
    case 5:
        v = "Medium"
    case 6 :
        v = "Medium high"
    case 7:
        v = "Loud"
    case 8:
        v = "Very loud"
    case 9 | 10:
        v = "Max volume"
    case _:
        v = "Invalid volume ! "

print(f"Niveau {volume} : {v}")

