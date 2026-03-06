import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.searcch(pattern, number)
    if match:
        code = match.group()[:match.group().find("-")]
        print(f"Valid. Location: {locations.get(code, 'Unknown')}")
    else:
        print("Invalid")

main()