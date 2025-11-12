name = input("Enter your name: ")

#remove whitespace and capitalize the first letter of each word

name = name.strip().title()

#split that name into two parts if there is a space

if ' ' in name:
    first_name, last_name = name.split(' ', 1)
    
    print(f'Hello, {first_name}')