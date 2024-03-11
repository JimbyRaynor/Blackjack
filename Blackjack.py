# blackjack with 3 computer players, ONE deck :) Count cards ;)

import random

Acefound = False

def value(cardstring):
    global Acefound
    if cardstring[0] in ['2','3','4','5','6','7','8','9','10']:
        return int(cardstring[0])
    elif cardstring[0] == "A":
        Acefound = True  # an Ace can be 1 or 11
        return 1  # Ace=1, at most one of the Aces can be 11, so add 10 in total() if <= 21
    else:
        return 10  # face card

def total(cardlist):
    global Acefound
    Acefound = False
    subtotal = 0
    for i in cardlist:
        subtotal = subtotal + value(i)
    if Acefound == True:
       if subtotal+10 <= 21:
           subtotal = subtotal + 10  # one Ace can be 11, so add 10
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

dealer = [Cards.pop()] # dealer only gets extra cards after
                       # all other players "stand" or "go bust"
player = [Cards.pop()]
computer1 = [Cards.pop()]
computer2 = [Cards.pop()]
computer3 = [Cards.pop()]

def showcards():
  print("Dealer: ", dealer)
  print("total = ", total(dealer))
  print("You: ", player)
  print("total = ", total(player))
  print("Computer 1:", computer1)
  print("total = ", total(computer1))
  print("Computer 2:", computer2)
  print("total = ", total(computer2))
  print("Computer 3:", computer3)
  print("total = ", total(computer3))

dealcard = 'y';
computer1out = False;
computer2out = False;
computer3out = False;


def computerchoice():
   global computer1out, computer2out, computer3out 
   if total(computer1) <= 14:
      computer1.append(Cards.pop())
      if total(computer1) > 21:
          print("Computer 1 busted")
          computer1out = True
   else:
      print("Computer1 stands")
      computer1out = True;
   if total(computer2) <= 14:
      computer2.append(Cards.pop())
      if total(computer2) > 21:
          print("Computer 2 busted")
          computer2out = True
   else:
      print("Computer2 stands")
      computer2out = True;
   if total(computer3) <= 14:
      computer3.append(Cards.pop())
      if total(computer3) > 21:
          print("Computer 3 busted")
          computer3out = True
   else:
      print("Computer3 stands")
      computer3out = True;
      


while (dealcard == 'y') or \
      ( (not computer1out) or (not computer2out) or (not computer2out) ):
   computerchoice()
   player.append(Cards.pop())
   showcards()
   dealcard  = input("Deal another card (y/n)?")


print("Remaining cards in deck: ", len(Cards))

print("Goodbye. Have a nice day :)")
