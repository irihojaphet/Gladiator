import re

email = input("What is your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")