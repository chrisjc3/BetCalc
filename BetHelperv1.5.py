
import tkinter as tk
from tkinter import BOTH, END, LEFT, RIGHT, NORMAL, DISABLED, W, E, N, S
from tkinter.simpledialog import askstring, askinteger
from tkinter.messagebox import showerror
import re

def getConversion(bank, unit):
    ans = round((bank*.01)*unit,2)
    lsum1.insert(END, str(unit) + "u" + " == $ " + str(ans))

def runReduce():
    match = re.match(r'.+\$\s(.+)', lsum1.get("1.0",END))
    bank = float(v1.get())
    amt = round(float(bank) - float(match.group(1)),2)
    v1.set(amt)
    runGetRates()

def runGetRates():
    try:
        bank = float(v1.get())
        unit = float(v2.get())
        lsum1.config(state=NORMAL)
        lsum1.delete(1.0, END)
    except:
        lsum1.insert(END, "Put in real numbers")
    getConversion(bank, unit)
    lsum1.config(state=DISABLED)

def getProb(val):
    try:
        digits = float(val)
        if odds_switch.get() == "plus":
            ans = 100/(digits+100)
        if odds_switch.get() == "minus":
            ans = (-1*-digits)/((-1*-digits)+100)
        ans = round(ans*100,2)
        lsum2.insert(END, "Implied Probabity: " + str(ans))
    except:
        lsum2.insert(END, "Enter actual Odds please.")
        
def runGetProb():
    try:
        val = str(odds.get())
        lsum2.config(state=NORMAL)
        lsum2.delete(1.0, END)
        getProb(val)
    except:
        lsum2.insert(END, "Enter actual Odds please.")
    lsum2.config(state=DISABLED)

master = tk.Tk()
master.title("BetUnitCalc")
##master.geometry("430x200")

v1 = tk.StringVar(master)
v1.set("0") 

v2 = tk.StringVar(master)
v2.set("0")

odds = tk.StringVar(master)
odds.set("0")

label1 = tk.Label(master, text="Bankroll")
e = tk.Entry(master, textvariable=v1)

label2 = tk.Label(master, text="Units to burn")
w = tk.Entry(master, textvariable=v2)

lsum1 = tk.Text(master, height=1, width=25, bg='lightgrey', relief='flat')
lsum1.insert(END, "Waiting....")
lsum1.config(width=25,state=DISABLED) # forbid text edition

b = tk.Button(master, text="Convert", command=runGetRates)
c = tk.Button(master, text="Placed", command=runReduce)

label3 = tk.Label(master, text="Odds(+/-)")
j = tk.Entry(master, textvariable=odds)
lsum2 = tk.Text(master, height=1, width=25, bg='lightgrey', relief='flat')
lsum2.insert(END, "Waiting....")
lsum2.config(width=25,state=DISABLED) # forbid text edition
d = tk.Button(master, text="Probability", command=runGetProb)

odds_switch = tk.StringVar(value="plus")
plus_button = tk.Radiobutton(master, text="+", variable=odds_switch,
                            indicatoron=False, value="plus", width=8)
minus_button = tk.Radiobutton(master, text="-", variable=odds_switch,
                            indicatoron=False, value="minus", width=8)

label1.grid(row=0, column=0, sticky=N+W,padx=5)
e.grid(row=1, column=0, sticky=W,padx=5)
label2.grid(row=0, column=0, sticky=N+E,padx=5)
w.grid(row=1, column=0, sticky=E,padx=5)
lsum1.grid(row=2, column=0, sticky=W+E+N+S,padx=5)
b.grid(row=3, column=0, sticky=W+E+N+S,padx=5)
c.grid(row=4, column=0, sticky=W+E+N+S,padx=5)

label3.grid(row=0, column=2,columnspan=2,sticky=W+E+N+S)
plus_button.grid(row=1, column=2,sticky=W+E+N+S)
minus_button.grid(row=1, column=3,sticky=W+E+N+S)

j.grid(row=2, column=2,columnspan=2,sticky=W+E+N+S)
lsum2.grid(row=3, column=2, columnspan=2,sticky=W+E+N+S)
d.grid(row=4, column=2, columnspan=2,sticky=W+E+N+S)


tk.mainloop()

