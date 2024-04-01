# blackjack with 3 computer players, ONE deck :) Count cards ;)

from tkinter import *

import random
import time

mainwin = Tk()
mainwin.geometry("800x400")
button1 = Button(mainwin, text="Hello World")
button1.place(x=170, y = 100)


xgap = 153


# NEED to store returned pointers as GLOBAL variables
# CANNOT use PhotoImage inside a function, otherwise

player1a = Canvas(mainwin, width = 64, height = 64)
player1aimage = PhotoImage(file="Cards\card_back.png")
player1asprite = player1a.create_image(0,0,anchor=NW,image=player1aimage)
player1a.place(x=120,y=0)
player1b = Canvas(mainwin, width = 64, height = 64)
player1bimage = PhotoImage(file="Cards\card_back.png")
player1bsprite = player1b.create_image(0,0,anchor=NW,image=player1bimage)
player1b.place(x=120+xgap,y=0)
player1c = Canvas(mainwin, width = 64, height = 64)
player1cimage = PhotoImage(file="Cards\card_back.png")
player1csprite = player1c.create_image(0,0,anchor=NW,image=player1cimage)
player1c.place(x=120+xgap*2,y=0)
player1d = Canvas(mainwin, width = 64, height = 64)
player1dimage = PhotoImage(file="Cards\card_back.png")
player1dsprite = player1d.create_image(0,0,anchor=NW,image=player1dimage)
player1d.place(x=120+xgap*3,y=0)



player = []

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

def cardfilename(cardstring):
    suitstring = ""
    if "Hearts" in cardstring:
        suitstring = "hearts"
    if "Clubs" in cardstring:
        suitstring = "clubs"
    if "Diamonds" in cardstring:
        suitstring = "diamonds"
    if "Spades" in cardstring:
        suitstring = "spades"
    numberstring = ""
    if cardstring[0] in ['2','3','4','5','6','7','8','9']:
        numberstring = "0"+cardstring[0]
    elif cardstring[0] == '1':
        numberstring = '10'
    else: numberstring = cardstring[0] # must be A, J, Q, K
    return "Cards\\"+"card_"+suitstring+"_"+numberstring+".png"


# cannot use PhotoImage inside a function since the returned pointer is local, and trashed
# So use global variables to store the returned pointer
def timerupdate():
    global player1aimage, player1asprite, player1bimage, player1bsprite, player1cimage, player1csprite, player1dimage, player1dsprite   
    if len(player) > 0:
     i = 0
     for card in player:
        i = i + 1
        if i == 1:
          player1aimage = PhotoImage(file=cardfilename(card))
          player1a.itemconfigure(player1asprite, image=player1aimage)
        if i == 2:
          player1bimage = PhotoImage(file=cardfilename(card))
          player1b.itemconfigure(player1bsprite, image=player1bimage)
        if i == 3:
          player1cimage = PhotoImage(file=cardfilename(card))
          player1c.itemconfigure(player1csprite, image=player1cimage)
        if i == 4:
          player1dimage = PhotoImage(file=cardfilename(card))
          player1d.itemconfigure(player1dsprite, image=player1dimage)
     mainwin.after(2000,timerupdate)




mainwin.after(2000,timerupdate)
mainwin.mainloop()


Acefound = False

Money = 100
Bet = 10



def value(cardstring):
    global Acefound
    print(cardfilename(cardstring))
    if cardstring[0] in ['2','3','4','5','6','7','8','9']:
        return int(cardstring[0])
    elif cardstring[0] == "A":
        Acefound = True  # an Ace can be 1 or 11
        return 1  # Ace=1, at most one of the Aces can be 11, so add 10 in total() if <= 21
    else:
        return 10  # face card, includes case where cardstring[0]=1, missing 0, so a ten

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
        





def showcards():
  time.sleep(1)
  print("dealing ...")
  time.sleep(2)
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
  a = input("Press Enter to continue")

dealcard = 'y';
computer1out = False;
computer2out = False;
computer3out = False;
playerout = False;


def computerchoice():
   global computer1out, computer2out, computer3out 
   if total(computer1) <= 14:
      computer1.append(Cards.pop())
      if total(computer1) > 21:
          print("Computer 1 busted")
          computer1out = True
   else:
      computer1out = True;
   if total(computer2) <= 14:
      computer2.append(Cards.pop())
      if total(computer2) > 21:
          print("Computer 2 busted")
          computer2out = True
   else:
      computer2out = True;
   if total(computer3) <= 14:
      computer3.append(Cards.pop())
      if total(computer3) > 21:
          print("Computer 3 busted")
          computer3out = True
   else:
      computer3out = True;
      


while  (not playerout) or \
       (not computer1out) or (not computer2out) or (not computer3out) :
   computerchoice()
   if playerout == False:
       player.append(Cards.pop())
   showcards()
   if total(player) > 21:
          print("Player busted")
          playerout = True
   if playerout == False:
      dealcard  = input("Deal another card (y/n)?")
   if dealcard != 'y':
       playerout = True

# after all players have finished, it is the dealers turn
# must hit if total <= 16
# must stand if total >= 17


print("")
print("Dealers turn")
print("")
time.sleep(3)

dealerout = False;
dealer.append(Cards.pop())
while (not dealerout):
    if total(dealer) <= 16:
        dealer.append(Cards.pop())
    if total(dealer) >= 17:
        dealerout = True;
    showcards()

if total(dealer) > 21:
    print("Dealer Busted!!")
showcards()
    

if (total(player) > 21):
    print("player lost")
elif (total(player) > total(dealer)) or (total(dealer) > 21):
    print("player wins")
elif (total(player) == total(dealer)):
    print("Push (money returned, no loss or gain)")
else:
    print("Player lost")


print("Remaining cards in deck: ", len(Cards))



print("Goodbye. Have a nice day :)")
