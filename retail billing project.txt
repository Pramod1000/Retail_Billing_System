from tkinter import*
import random
import time

root = Tk()
root.geometry("890x580+0+0")
root.title("BILLING SYSTEM")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)


#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="BILLING SYSTEM",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)



def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    cosand= float(Sandwich.get())
    cob= float(Burger.get())
    copi= float(Pizza.get())
    cohot= float(hotdog.get())
    codr= float(Drinks.get())

    costoffries = cof*5
    costofsandwich = cosand*4
    costofburger = cob*8
    costofPizza = copi*15
    costofhotdog = cohot*6
    costofdrinks = codr*2

    costofmeal = "$",str('%.2f'% (costoffries +  costofsandwich + costofburger + costofPizza + costofhotdog + costofdrinks))
    PayTax=((costoffries +  costofsandwich + costofburger + costofPizza +  costofhotdog + costofdrinks)*0.33)
    Totalcost=(costoffries +  costofsandwich + costofburger + costofPizza  + costofhotdog + costofdrinks)
    Ser_Charge=((costoffries +  costofsandwich + costofburger + costofPizza + costofhotdog + costofdrinks)/99)
    Service="$",str('%.2f'% Ser_Charge)
    OverAllCost="$",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="$",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Sandwich.set("")
    Burger.set("")
    Pizza.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    hotdog.set("")


#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Sandwich = StringVar()
Burger = StringVar()
Pizza = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
hotdog = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="brown",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="yellow" ,justify='right', state="readonly")
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="French Fries",fg="blue",bd=10,anchor='w')
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="lightblue" ,justify='right')
txtfries.grid(row=2,column=1)

lblSandwich = Label(f1, font=( 'aria' ,16, 'bold' ),text="Sandwich",fg="blue",bd=10,anchor='w')
lblSandwich.grid(row=3,column=0)
txtSandwich = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Sandwich , bd=6,insertwidth=4,bg="lightblue" ,justify='right')
txtSandwich.grid(row=3,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger",fg="blue",bd=10,anchor='w')
lblburger.grid(row=4,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="lightblue" ,justify='right')
txtburger.grid(row=4,column=1)

lblPizza = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza",fg="blue",bd=10,anchor='w')
lblPizza.grid(row=5,column=0)
txtPizza = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Pizza , bd=6,insertwidth=4,bg="lightblue" ,justify='right')
txtPizza.grid(row=5,column=1)

lblhotdog = Label(f1, font=( 'aria' ,16, 'bold' ),text="Hotdog",fg="blue",bd=10,anchor='w')
lblhotdog.grid(row=6,column=0)
txthotdog = Entry(f1,font=('ariel' ,16,'bold'), textvariable=hotdog , bd=6,insertwidth=4,bg="lightblue" ,justify='right')
txthotdog.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
lblDrinks.grid(row=1,column=0)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="lightblue" ,justify='right')
txtDrinks.grid(row=1,column=1)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=4,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right', state="readonly")
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="green",command=Ref)
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="green",command=qexit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sandwich ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="4", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="8", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hotdog", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="6", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()
