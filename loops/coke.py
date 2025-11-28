'''
ibiceri 5 - 10 - 25

ayo ugomba kwishyura 50

mugihe umpaye 5 kandi usigaje kwishura aruta 5
muguhe umpaye 5 kandi ntayo waburaga kwishyura ndahita nkujyamo 5
'''
def main():
    amount_due = 50

    while True:
        coin = int(input("Insert coin:"))
        if coin == 5:
            if amount_due >= 5:
                amount_due = amount_due - 5
                print(f"Amount due: {amount_due}")
            elif amount_due == 0 :
                break
            else:
                amount_owed = amount_due + 5
                print(f"Change owed: {amount_owed}")

        elif coin == 10:
            if amount_due >= 10:
                amount_due = amount_due - 10
                print(f"Amount due: {amount_due}")
            elif amount_due == 0 :
                break
            else:
                amount_owed = amount_due + 10
                print(f"Change owed: {amount_owed}")
        elif coin == 25:
            if amount_due >= 25:
                amount_due = amount_due - 25
                print(f"Amount due: {amount_due}")
            elif amount_due == 0 :
                break
            else:
                amount_owed = amount_due + 25
                print(f"Change owed: {amount_owed}")
        else:
            print(f"Amount due: 50")




main()
