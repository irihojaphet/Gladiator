try:
    x = int(input("What' x? "))

    
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")   