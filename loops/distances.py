distances = {
    "voyager 1": 163,
    "voyager 2": 136,
    "pioneer 10": 80,
    "New Horizons": 58,
    "pioneer 11": 44
}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth.")


main()