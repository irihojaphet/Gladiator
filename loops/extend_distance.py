distances = {
    "voyager 1": 163,
    "voyager 2": 136,
    "pioneer 10": 80,
    "New Horizons": 58,
    "pioneer 11": 44
}

def main():
    for distance in distances.values():
        print(f"{distance} is {converter(distance)} in miters.")


def converter(au):
    return au * 149597870700




main()