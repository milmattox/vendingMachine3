#Vending Machine by Michelle Mattox June 27, 2022
import tkinter as tk
import random
#set up window
window = tk.Tk()
window.title("Vending Machine")
window.geometry("600x600")

itemName = ['smarties','snickers','cheetos','cookies','musketeers','jujifruit','goobers','malt balls','circus peanuts', 'necco wafers']
itemPrice = [1.00, 1.50, 1.25, 1.50, 1.50,1.25,1.00,1.10,1.00,1.00]
itemQuantity = [0,0,0,0,0,0,0,0,0,0]
itemQuantityLabel = [0,0,0,0,0,0,0,0,0,0]
itemPriceLabel = [0,0,0,0,0,0,0,0,0,0]
itemButton = [0,0,0,0,0,0,0,0,0,0]
orderedItems = []
orderedItemsCount = 0
denominations = ["$100:", "$50:","$20:","$10:", "$5:", "$1:", "Half-dollars:", "Quarters:", "Dimes:", "Nickles:", "Pennies:"]
denominationsLabel=[0,0,0,0,0,0,0,0,0,0,0]
denominationsQuantityLabel=[0,0,0,0,0,0,0,0,0,0,0]
money = 0

def calculateChange():
  global money
  hundreds = int(money // 100)
  money = money - hundreds*100
  denominationsQuantityLabel[0].config(text = hundreds)
  fifties = int(money // 50)
  money = money - fifties*50
  denominationsQuantityLabel[1].config(text = fifties)
  twenties = int(money //20)
  money = money - twenties*20
  denominationsQuantityLabel[2].config(text = twenties)
  tens = int(money //10)
  money = money - tens*10
  denominationsQuantityLabel[3].config(text = tens)
  fives = int(money // 5)
  money = money - fives*5
  denominationsQuantityLabel[4].config(text = fives)
  ones = int(money//1)
  money = money - ones
  denominationsQuantityLabel[5].config(text = ones)
  halves = int(money//.50)
  money = money - halves*.50
  denominationsQuantityLabel[6].config(text = halves)
  quarters = int(money//.25)
  denominationsQuantityLabel[7].config(text = quarters)
  money = money - quarters*.25
  dimes = int(money//.10)
  denominationsQuantityLabel[8].config(text = dimes)
  money = money - dimes*.10
  nickles = int(money//.05)
  denominationsQuantityLabel[9].config(text = nickles)
  money = money - nickles*.05
  pennies = round(money*100)
  denominationsQuantityLabel[10].config(text = pennies)

def setQuantities():  #set the starting inventory
    for i in range(len(itemName)):
        itemQuantity[i] =random.randint(1,10)
        
def myOrder(itemnum): #place an order
  global money
  if money > 0:
    if money >= itemPrice[itemnum]:
      if itemQuantity[itemnum] > 0:
        itemQuantity[itemnum]-=1
        money = money - itemPrice[itemnum]
        myMoneyLabel.config(text="Money Left: ${:,.2f}".format(money))
      else:
       itemOutLabel.config(text = "This item out: "+ itemName[itemnum])
    else:
      itemOutLabel.config(text = "You don't have enough for a " + itemName[itemnum])
  else: 
        itemOutLabel.config(text = "Enter some cash!")
  itemQuantityLabel[itemnum].config(text=itemQuantity[itemnum])
    
def myMoney(): #enter money
  global money
  try:
    money = float(e.get())+ money
    myMoneyLabel.config(text="Money Left:  ${:,.2f}".format(money))
    if money > 0:
      itemOutLabel.config(text = "Thank you! What would you like?")
  except:
    itemOutLabel.config(text = "Enter some cash!")
  
ack1 = tk.Label(text="Make Your Selection!")

e = tk.Entry(borderwidth=2, width=15) #enter money
#e.insert(0,"Enter amount")
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
#Denominations Labels
for i in range(len(denominations)):
  denominationsLabel[i] = tk.Label(text = denominations[i])
  denominationsLabel[i].grid(row=i+11,column=1,sticky="E")
  denominationsQuantityLabel[i] = tk.Label(text = "")
  denominationsQuantityLabel[i].grid(row=i+11, column=2, sticky="E")
  
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

tk.mainloop()
