# blackjack with 3 computer players, ONE deck :) Count cards ;)

import random

def value(cardstring):
    if cardstring[0] in ['2','3','4','5','6','7','8','9','10']:
        return int(cardstring[0])
    elif cardstring[0] == "A":
        return 11
    else:
        return 10  # face card

def total(cardlist):
    subtotal = 0
    for i in cardlist:
        subtotal = subtotal + value(i)
    return subtotal
        
                         

Nums = ["Ace"]

for i in range(2,11):
    Nums.append(str(i))

Nums= Nums+["Jack", "Queen", "King"]

Suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

Cards = []

for s in Suits:
    for n in Nums:
        Cards.append(n+" "+s)

random.shuffle(Cards)

dealer = [Cards.pop(),Cards.pop()]
player = [Cards.pop(),Cards.pop()]
computer1 = [Cards.pop(),Cards.pop()]
computer2 = [Cards.pop(),Cards.pop()]
computer3 = [Cards.pop(),Cards.pop()]

print("Dealer: ", dealer)
print("total = ", total(dealer))
print("You: ",player)
print("total = ", total(player))
print("Computer 1:", computer1)
print("total = ", total(computer1))
print("Computer 2:", computer2)
print("total = ", total(computer2))
print("Computer 3:", computer3)
print("total = ", total(computer3))



print("Remaining cards = ", len(Cards))
