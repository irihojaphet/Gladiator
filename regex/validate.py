email = input("What is your emai? ").strip()

if "@" and "." in email:
    print("Valid")
else:
    print("Invald")