def main():

    b = get_number()
    meow(b)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n

def meow(a):

    for i in range(a):
        print("meow")

main()