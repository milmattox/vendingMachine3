#Vending Machine by Michelle Mattox June 27, 2022
import tkinter as tk
from tkinter import *
import random
#set up window
window = tk.Tk()
window.title("Vending Machine")
window.geometry("600x600")

itemName = ['smarties','snickers','cheetos','cookies','musketeers','jujifruit','goobers','malt balls','circus peanuts', 'necco wafers'] #available items
itemPrice = [1.00, 1.50, 1.25, 1.50, 1.50,1.25,1.00,1.10,1.00,1.00]#item prices
itemQuantity = [0,0,0,0,0,0,0,0,0,0] #holds quantity of each item
itemQuantityLabel = [0,0,0,0,0,0,0,0,0,0]#label for quantity
itemPriceLabel = [0,0,0,0,0,0,0,0,0,0] #price for each item
itemButton = [0,0,0,0,0,0,0,0,0,0]#item button
orderedItemsCount = [0,0,0,0,0,0,0,0,0,0]#number of items in an order
denominations = ["$100:", "$50:","$20:","$10:", "$5:", "$1:", "Half-dollars:", "Quarters:", "Dimes:", "Nickles:", "Pennies:"]#denominations of money
denominationsLabel=[0,0,0,0,0,0,0,0,0,0,0]#denominations label
denominationsQuantityLabel=[0,0,0,0,0,0,0,0,0,0,0]# label to show the amount of change
money = 0  #the amount of money that the user entered
completeOrder = False #Boolean to keep track of when order is complete

def calculateChange():
  global money, completeOrder
  hundreds = int(money // 100)#count of $100's
  money = round(money - hundreds*100, 2)
  denominationsQuantityLabel[0].config(text = hundreds)
  fifties = int(money // 50)#count of $50's
  money = round(money - fifties*50,2)
  denominationsQuantityLabel[1].config(text = fifties)
  twenties = int(money //20)#count of $20's
  money = round(money - twenties*20,2)
  denominationsQuantityLabel[2].config(text = twenties)
  tens = int(money //10)#count of $10'
  money = round(money - tens*10,2)
  denominationsQuantityLabel[3].config(text = tens)
  fives = int(money // 5)#count of $5's
  money = round(money - fives*5,2)
  denominationsQuantityLabel[4].config(text = fives)
  ones = int(money//1)#count of $1's
  money = money - ones
  denominationsQuantityLabel[5].config(text = ones)
  money = round(money * 100)
  halves = int(money//50)#count of half dollars
  money = money - halves*50
  denominationsQuantityLabel[6].config(text = halves)
  quarters = int(money//25)#count of quarters
  denominationsQuantityLabel[7].config(text = quarters)
  money = money - quarters*25
  dimes = int(money//10)#count of dimes
  denominationsQuantityLabel[8].config(text = dimes)
  money = money - dimes*10
  nickles = int(money//5)#count of nickles
  denominationsQuantityLabel[9].config(text = nickles)
  money = money - nickles*5
  pennies = round(money)#count of pennies
  
  denominationsQuantityLabel[10].config(text = pennies)
  completeOrder = True
  money = 0
  
def setQuantities():  #set the starting inventory
    for i in range(len(itemName)):
        itemQuantity[i] =random.randint(1,10)

def restockItems():  #set the starting inventory
    for i in range(len(itemName)):
        itemQuantity[i] =itemQuantity[i] + random.randint(1,10)
    for i in range(len(itemQuantityLabel)):
      itemQuantityLabel[i].config(text = itemQuantity[i])

def makelist():
  listbox.delete(0,listbox.size())
  for i in range(10):
    if orderedItemsCount[i] > 0:
      item = itemName[i] + " " + str(orderedItemsCount[i])
      listbox.insert(i,item)

def myOrder(itemnum): #place an order
  global money
  if money > 0:
    if money >= itemPrice[itemnum]:
      if itemQuantity[itemnum] > 0:
        itemQuantity[itemnum]-=1
        money = money - itemPrice[itemnum]
        orderedItemsCount[itemnum]=orderedItemsCount[itemnum] + 1
        myMoneyLabel.config(text="Money Left: ${:,.2f}".format(money))
        makelist()
      else:
       itemOutLabel.config(text = "This item out: "+ itemName[itemnum])
    else:
      itemOutLabel.config(text = "You don't have enough for a " + itemName[itemnum])
  else: 
        itemOutLabel.config(text = "Enter some cash!")
  itemQuantityLabel[itemnum].config(text=itemQuantity[itemnum])

def clearEverything():
  global completeOrder
  listbox.delete(0,listbox.size())
  for i in range(11):
    denominationsQuantityLabel[i].config(text = "")
  for i in range(10):
      orderedItemsCount[i] = 0
  completeOrder = False
  
def myMoney(): #enter money
  global money, completeOrder
  if completeOrder == True:
    clearEverything()
  try:
    money = float(e.get())+ money
    myMoneyLabel.config(text="Money Left:  ${:,.2f}".format(money))
    if money > 0:
      itemOutLabel.config(text = "Thank you! What would you like?")
  except:
    itemOutLabel.config(text = "Enter some cash!")
  e.delete(0,15)
ack1 = tk.Label(text="Make Your Selection!")

e = tk.Entry(borderwidth=2, width=15) #enter money

cashButton = tk.Button(text="Enter Cash", command=myMoney, bg="lightgreen")
itemOutLabel = tk.Label(text = "", fg="red")
myMoneyLabel = tk.Label(text = "Money Left: ${:,.2f}".format(money))
myMoneyLabel.grid(row=1,column=3, columnspan=2)
#place instructions on grid
ack1.grid(row=0,column=0, columnspan=6)

itemOutLabel.grid(row=9,column=0,columnspan=3)
#place entry box on grid
e.grid(row=1,column=1, columnspan=2)
cashButton.grid(row=1,column=0, columnspan=1)

#Complete order
completeOrderButton = tk.Button(text="Complete Order",command=calculateChange, bg="lightgreen")
completeOrderButton.grid(row = 10,column=0)
changeLabel = tk.Label(text="Your change:")
changeLabel.grid(row = 11, column = 0)

#Restock Button
restockButton = tk.Button(text="Restock", command=restockItems, bg="brown")
restockButton.grid(row = 21, column = 0)

#Denominations Labels
for i in range(len(denominations)):
  denominationsLabel[i] = tk.Label(text = denominations[i])
  denominationsLabel[i].grid(row=i+11,column=1,sticky="E")
  denominationsQuantityLabel[i] = tk.Label(text = "")
  denominationsQuantityLabel[i].grid(row=i+11, column=2, sticky="W")
  
#item Buttons
itemButton[0] = tk.Button(text=itemName[0], command=lambda:myOrder(0), bg="lightblue")
itemButton[1] = tk.Button(text=itemName[1], command=lambda:myOrder(1), bg="lightpink")
itemButton[2] = tk.Button(text=itemName[2], command=lambda:myOrder(2), bg="lightyellow")
itemButton[3] = tk.Button(text=itemName[3], command=lambda:myOrder(3), bg="orange")
itemButton[4] = tk.Button(text=itemName[4], command=lambda:myOrder(4), bg="#778844")
itemButton[5] = tk.Button(text=itemName[5], command=lambda:myOrder(5), bg="violet")
itemButton[6] = tk.Button(text=itemName[6], command=lambda:myOrder(6), bg="#66FF33")
itemButton[7] = tk.Button(text=itemName[7], command=lambda:myOrder(7), bg="#4477FF")
itemButton[8] = tk.Button(text=itemName[8], command=lambda:myOrder(8), bg="#7744FF")
itemButton[9] = tk.Button(text=itemName[9], command=lambda:myOrder(9), bg="#774477")
#place buttons
for i in range(5):
  itemButton[i].grid(row=2,column=i)
for i in range(5,10):
  itemButton[i].grid(row=5,column=i-5)
setQuantities()
#quantity labels
for i in range(len(itemQuantityLabel)):
  itemQuantityLabel[i] = tk.Label(text = itemQuantity[i])

#price labels
for i in range(len(itemPriceLabel)):
  itemPriceLabel[i] = tk.Label(text = "${:,.2f}".format(itemPrice[i]))

#place price labels
for i in range(5):
  itemPriceLabel[i].grid(row=3,column=i)
for i in range(5,10):
  itemPriceLabel[i].grid(row=6,column=i-5)
#place quantity labels
for i in range(5):
  itemQuantityLabel[i].grid(row=4,column=i)
for i in range(5,10):
  itemQuantityLabel[i].grid(row=7,column=i-5)
  
#create listbox
ack3 = tk.Label(text = "Ordered Items")
ack3.grid(row=10, column=3)
listbox = Listbox(window, height = 10, 
                  width = 15, 
                  bg = "lightgrey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "black")
listbox.grid(row=11, column=3, rowspan=15)

tk.mainloop()
