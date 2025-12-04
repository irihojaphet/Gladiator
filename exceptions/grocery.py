def main():
    groceries = {}
    
    while True:
        try:
            item  = input().strip().upper()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except (KeyboardInterrupt,EOFError):
            print()
            break
    sorted_groceries = sorted(groceries)
    for item in sorted_groceries:
        print(f"{groceries[item]} {item}")



main()