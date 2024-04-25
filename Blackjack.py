# blackjack with 3 computer players, ONE deck :) Count cards ;)

from tkinter import *

import random
import time

mainwin = Tk()
mainwin.geometry("800x600")

font1 = ("Arial",12)
canvasText = Canvas(mainwin, width = 200, height = 600)
canvasText.place(x=0,y=0)
def printscr(mytext,x,y):
    canvasText.create_text(x,y,text=mytext, fill="blue",font=font1, anchor="sw") 

printscr("Human Player:",10,40)
printscr("Computer 1:",10,40+80)
printscr("Computer 2:",10,40+80*2)
printscr("Computer 3:",10,40+80*3)
printscr("Dealer:",10,50+80*4)

def hit():
    global playerturn, playerout
    if playerout == False:
       player.append(Cards.pop())
       if total(player) > 21:
          print("Player busted")
          playerout = True
    playerturn = False
    
    
btnHit = Button(mainwin, text="Hit", command=hit)
btnHit.place(x=170, y = 500)


xgap = 60



# CANNOT easily use PhotoImage inside a function
# NEED to store returned pointers as GLOBAL variables
# objects work well in this case, since they are pointers

class playerclass:
    def __init__(self,myfilename="",xloc=0,yloc=0):
        self.xloc = xloc
        self.yloc = yloc
        self.canvas = Canvas(mainwin, width=64, height = 64)
        self.image = PhotoImage(file=myfilename)
        self.sprite = self.canvas.create_image(0,0,anchor=NW,image=self.image)
        self.canvas.place(x=xloc,y=yloc)
    def changecard(self,card):
        self.image = PhotoImage(file=cardfilename(card))
        self.canvas.itemconfigure(self.sprite, image=self.image)
    
        
playerobjlist = []
for i in range(8):
  playerobjlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=0))

computer1objlist = []
for i in range(8):
  computer1objlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=80))

computer2objlist = []
for i in range(8):
  computer2objlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=160))

computer3objlist = []
for i in range(8):
  computer3objlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=240))  

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





Acefound = False

Money = 100
Bet = 10



def value(cardstring):
    global Acefound
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
        


def computerchoice():
   global computer1out, computer2out, computer3out 
   if total(computer1) <= 16:
      computer1.append(Cards.pop())
      if total(computer1) > 21:
          print("Computer 1 busted")
          computer1out = True
   else:
      computer1out = True;
   if total(computer2) <= 17:
      computer2.append(Cards.pop())
      if total(computer2) > 21:
          print("Computer 2 busted")
          computer2out = True
   else:
      computer2out = True;
   if total(computer3) <= 15:
      computer3.append(Cards.pop())
      if total(computer3) > 21:
          print("Computer 3 busted")
          computer3out = True
   else:
      computer3out = True;


def showcards():
  print("dealing ...")
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

playerturn = True;

def updatecards(cardlist, cardobjlist): # draw cards on screen
    i = 0
    for card in cardlist:
        cardobjlist[i].changecard(card)
        i = i + 1
    

# cannot use PhotoImage inside a function since the returned pointer is local, and trashed
# So use global variables or objects :) to store the returned pointer
def timerupdate():  # global player1aobj is not required since we
                    # are not changing the pointer player1aobj
    global playerturn
    updatecards(player, playerobjlist)
    if not playerturn:
       computerchoice()
       playerturn = True
    updatecards(computer1, computer1objlist)
    updatecards(computer2, computer2objlist)
    updatecards(computer3, computer3objlist)
    mainwin.after(1000,timerupdate)




mainwin.after(1000,timerupdate)
mainwin.mainloop()
      


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
