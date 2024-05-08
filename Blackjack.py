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

printscr("You:",10,40)
printscr("Computer 1:",10,40+80)
printscr("Computer 2:",10,40+80*2)
printscr("Computer 3:",10,40+80*3)
printscr("Dealer:",10,50+80*4)

labelRemainingcards = canvasText.create_text(10,500,text="Remaining Cards: ", fill="blue",font=font1, anchor="sw") 




xgap = 60

computer1out = False;
computer2out = False;
computer3out = False;
playerout = False;
dealerout = False;
playerturn = True;



######################################################################
# Use objects to draw on screen 
# CANNOT easily use PhotoImage inside a function
# NEED to store returned pointers as GLOBAL variables
# objects work well in this case, since they are pointers
#####################################################################

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
    

#######################################################################
# Initialise variables
#######################################################################
        
playerobjlist = []
computer1objlist = []
computer2objlist = []
computer3objlist = []
dealerobjlist = []


def setblankcards():
    for i in range(8):
      playerobjlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=0))
      computer1objlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=80))
      computer2objlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=160))
      computer3objlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=240))
      dealerobjlist.append(playerclass("Cards\card_back.png",xloc=120+xgap*i,yloc=320))  

setblankcards()  

player = []
Cards = []

Nums = ["Ace"]

for i in range(2,11):
    Nums.append(str(i))
    
Nums= Nums+["Jack", "Queen", "King"]

Suits = ["Hearts", "Diamonds", "Spades", "Clubs"]


def createdeckofcards():
    global Cards
    Cards.clear()
    for s in Suits:
       for n in Nums:
         Cards.append(n+" "+s)
    random.shuffle(Cards)

createdeckofcards()
dealer = [] 
player = []
computer1 = []
computer2 = []
computer3 = []
Acefound = False

Money = 100
Bet = 10

def dealinitialcards():
    global dealer, player, computer1, computer2, computer3
    global computer1out, computer2out, computer3out
    global playerout, dealerout, playerturn
    dealer = [Cards.pop()] # dealer only gets extra cards after
                       # all other players "stand" or "go bust"
    player = [Cards.pop(),Cards.pop()]
    computer1 = [Cards.pop(),Cards.pop()] 
    computer2 = [Cards.pop(),Cards.pop()]
    computer3 = [Cards.pop(),Cards.pop()]
    computer1out = False;
    computer2out = False;
    computer3out = False;
    playerout = False;
    dealerout = False;
    playerturn = True;
    playerobjlist.clear()
    computer1objlist.clear()
    computer2objlist.clear()
    computer3objlist.clear()
    dealerobjlist.clear()
    setblankcards()



dealinitialcards()



######################################################################
#  define on screen buttons
######################################################################
def hit():
    global playerout
    if playerout == False:
       player.append(Cards.pop())
       if total(player) > 21:
          print("Player busted")
          playerout = True
    playerturn = False
    
btnHit = Button(mainwin, text="Hit", command=hit)
btnHit.place(x=670, y = 20)

def stand():
    global playerturn, playerout
    playerturn = False
    playerout = True
    
btnHit = Button(mainwin, text="Stand", command=stand)
btnHit.place(x=720, y = 20)

def exitgame():
    mainwin.destroy()

btnExit = Button(mainwin, text = "Exit Game", command=exitgame)
btnExit.place(x=720, y=460)


btnNewDeck = Button(mainwin, text = "New Deck", command=createdeckofcards)
btnNewDeck.place(x=500, y=460)

def playagain():
    dealinitialcards()

btnPlayAgain = Button(mainwin, text = "Play Again", command=playagain)
btnPlayAgain.place(x=620, y=460)



######################################################################
# Define card functions for playing blackjack
######################################################################

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

def showscore():
  if total(dealer) > 21:
    print("Dealer Busted!!")
  if (total(player) > 21):
    print("player lost")
  elif (total(player) > total(dealer)) or (total(dealer) > 21):
    print("player wins")
  elif (total(player) == total(dealer)):
    print("Push (money returned, no loss or gain)")
  else:
    print("Player lost")

        
# after all players have finished, it is the dealers turn
# must hit if total <= 16
# must stand if total >= 17
def dealerturn():
    global dealerout
    if not dealerout:
      if total(dealer) <= 16:
        dealer.append(Cards.pop())
      if total(dealer) >= 17:
        dealerout = True;
    else:
        print("Game Over")
        showscore()

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

######################################################################
# Update cards on screen, while playing
######################################################################


def updatecards(cardlist, cardobjlist): # draw cards on screen
    i = 0
    for card in cardlist:
        cardobjlist[i].changecard(card)
        i = i + 1
    canvasText.itemconfigure(labelRemainingcards,text="Remaining cards: "+ str(len(Cards)))                    
    

# cannot use PhotoImage inside a function since the returned pointer is local, and trashed
# So use global variables or objects :) to store the returned pointer
def timerupdate():  # global player1aobj is not required since we
                    # are not changing the pointer player1aobj
    global playerturn
    updatecards(player, playerobjlist)
    if playerout:
       computerchoice()
    updatecards(computer1, computer1objlist)
    updatecards(computer2, computer2objlist)
    updatecards(computer3, computer3objlist)
    updatecards(dealer, dealerobjlist)
    if playerout and computer1out and computer2out and computer3out:
        print("dealer playing")
        dealerturn()
    mainwin.after(50,timerupdate)


mainwin.after(50,timerupdate)
mainwin.mainloop()
      








print("Goodbye. Have a nice day :)")
