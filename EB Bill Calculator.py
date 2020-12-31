from tkinter import *

top = Tk()
top.title("EB Bill calculation")
top.geometry("500x500")

unit = StringVar()
amount = StringVar()

def calculate():
  units = int(unit.get())
  bill_amount = 0
  if units>= 1 and units<=50:
    bill_amount = units*1
  elif units>=51 and units<=100:
    bill_amount = units*2
  elif units>=101 and units<=150:
    bill_amount = units*3
  elif units>=151 and units<=250:
    bill_amount = units*4
  elif units>=251 and units<=400:
    bill_amount = units*5
  elif units>400:
    bill_amount = units*6
  amount.set('Rs : ' +str(bill_amount))

label1 = Label(top, text = "Enter the units :").place(x=20,y=30)
entry1 = Entry(top,textvariable = unit).place(x=130,y=30)
btn1 = Button(top,text = "Calculate",command = calculate).place(x=80,y=60)

lable2 = Label(top,text = "Bill amount : ").place(x =20,y=90)
entry2 = Entry(top,textvariable = amount).place(x=130,y=90)

top.mainloop()