def main():
    vowels = ["a","i","u","o","e","A","I","U","O","E"]
    original = input("Input: ")

    for o in original:
        if o not in vowels:
            print(o, end="")


main()


