'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from random import randint
done = False
class shopping:
    def __init__(self):
        self.items = []
    def addcart(self,item):
        self.items.append(item)
    def removefromcart(self,itemindex):
        self.items.pop(itemindex)
    def pricecart(self):
        price = 0
        for x in self.items:
            price = price + x.price
        return price
    def listcart(self):
        cid = 0
        print("cart items:")
        for x in self.items:
            print(x.name,x.price,cid)
            cid = cid + 1
        print ("")
class Item:
        def __init__(self,price,name):
            self.name = name
            self.price = price
store=[]
itemNames = ["Phone","keyborad","Ram","Headphone"]
def makestore(amt):
        storeitems = 0
        while storeitems <= amt:
            nItem = Item(randint(1,50),itemNames[randint(0,len(itemNames)-1)])
            store.append(nItem)
            storeitems = storeitems + 1
def CreateStore(storefile):
        try:
            fx = open(storefile,"r")
            str1 = ""
            str1 = fx.read()
        except IOError:
            print("No Existing store generating items")
            makestore(4)
def liststore():
        iid = 0
        for x in store:
            print(iid,x.price,x.name)
            iid = iid + 1
def removeItem(cart):
    input1 = int(input("Type of cart object ID to remove"))
    cart.removefromcart(input1)
def printdetail():
    print("Type C to view tocart items")
    print("Type R to remove tocart item")
    print("Type an item number to buy it")
    print("Type P to get the total cart price")
    print("Type X to exit the programe.")
def handleinput(n,cart):
    char_inputs = ["C","R","P","X"]
    if (n == "C"):
        cart.listcart()
    if (n == "R"):
        removeItem(cart)
    if(n == "P"):
        print("The items in your cart currently cost")
        print(cart.pricecart())
    if(n == "X"):
        global done
        done = True
    if(n not in char_inputs):
        try:
            cart.addcart(store[int(n)])
        except:
            pirnt("you have enter an illegal character!")
cart1 = shopping()
CreateStore("cart1.cartfile")
while (done == False):
    liststore()
    printdetail()
    n = input("choose an item to buy(type the id)")
    handleinput(n,cart1)