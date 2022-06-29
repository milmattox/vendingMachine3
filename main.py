#Vending Machine by Michelle Mattox June 27, 2022
import tkinter as tk
import random
#set up window
window = tk.Tk()
window.title("Vending Machine")
window.geometry("500x300")
#initialize global variables
smarties,cookies,snickers,cheetos,reeses =0,0,0,0,0

itemName = ['smarties','snickers','cheetos','cookies','musketeers']
itemPrice = [1.00, 1.50, 1.25, 1.50, 1.50]
itemQuantity = [0,0,0,0,0]
itemQuantityLabel = [0,0,0,0,0]
itemPriceLabel = [0,0,0,0,0]
itemButton =[0,0,0,0,0]
def setQuantities():  #set the starting inventory
    for i in range(len(itemName)):
        itemQuantity[i] =random.randint(1,10)
        
def myOrder(itemnum): #if they want a smarties
    itemQuantity[itemnum]-=1
    itemQuantityLabel[itemnum].config(text=itemQuantity[itemnum])
    
def myMoney(): #enter money
    myLabel3 = tk.Label(text=e.get())
    myLabel3.grid(row=1,column=2)

#place acks on window
ack1 = tk.Label(text="Make Your Selection!")
e = tk.Entry(borderwidth=2, width=15) #enter money
#e.insert(0,"Enter amount")
cashButton = tk.Button(text="Enter Cash", command=myMoney, bg="lightgreen")
#place instructions on grid
ack1.grid(row=0,column=0, columnspan=4)
#place entry box on grid
e.grid(row=1,column=2, columnspan=2)
cashButton.grid(row=1,column=0, columnspan=2)
#buttons
itemButton[0] = tk.Button(text=itemName[0], command=lambda:myOrder(0), bg="lightblue")
itemButton[1] = tk.Button(text=itemName[1], command=lambda:myOrder(1), bg="lightpink")
itemButton[2] = tk.Button(text=itemName[2], command=lambda:myOrder(2), bg="lightyellow")
itemButton[3] = tk.Button(text=itemName[3], command=lambda:myOrder(3), bg="orange")
itemButton[4] = tk.Button(text=itemName[4], command=lambda:myOrder(4), bg="violet")
#place buttons
itemButton[0].grid(row=2,column=0)
itemButton[1].grid(row=2,column=1)
itemButton[2].grid(row=2, column=2)
itemButton[3].grid(row=2, column=3)
itemButton[4].grid(row=2, column=4)
setQuantities()
#quantity labels
itemQuantityLabel[0] = tk.Label(text = itemQuantity[0])
itemQuantityLabel[1] = tk.Label(text = itemQuantity[1])
itemQuantityLabel[2] = tk.Label(text = itemQuantity[2])
itemQuantityLabel[3] = tk.Label(text = itemQuantity[3])
itemQuantityLabel[4] = tk.Label(text = itemQuantity[4])
#price labels
itemPriceLabel[0] = tk.Label(text = "${:,.2f}".format(itemPrice[0]))
itemPriceLabel[1] = tk.Label(text = "${:,.2f}".format(itemPrice[1]))
itemPriceLabel[2] = tk.Label(text = "${:,.2f}".format(itemPrice[2]))
itemPriceLabel[3] = tk.Label(text = "${:,.2f}".format(itemPrice[3]))
itemPriceLabel[4] = tk.Label(text = "${:,.2f}".format(itemPrice[4]))
#place price labels
itemPriceLabel[0].grid(row=3,column=0)
itemPriceLabel[1].grid(row=3,column=1)
itemPriceLabel[2].grid(row=3,column=2)
itemPriceLabel[3].grid(row=3,column=3)
itemPriceLabel[4].grid(row=3,column=4)
#place quantity labels
itemQuantityLabel[0].grid(row=4,column=0)
itemQuantityLabel[1].grid(row=4,column=1)
itemQuantityLabel[2].grid(row=4,column=2)
itemQuantityLabel[3].grid(row=4,column=3)
itemQuantityLabel[4].grid(row=4,column=4)

tk.mainloop()
