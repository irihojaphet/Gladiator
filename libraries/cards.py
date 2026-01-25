import random
cards = ["jack", "queen", "king"]

def main():
   print(random.choices(cards,weights=[75, 20, 5], k=2)) # sampling with replacement
   print(random.sample(cards, k=2)) # sampling without replacement

main()