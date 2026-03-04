import re

email = input("What is your email? ").strip()

if re.seach(".*@.*", email):
    print("Valid")
else:
    print("Invalid")