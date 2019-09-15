
import tkinter as tk
from tkinter import BOTH, END, LEFT, RIGHT, NORMAL, DISABLED, W, E, N, S
import re

def call_minustoggle(event):
    odds_switch.set("minus")
    odds.set("")
    j.focus_set()
    
def call_plustoggle(event):
    odds_switch.set("plus")
    odds.set("")
    j.focus_set()
    
def call_enterproc(event):
    try:
        runGetProb()
    except: pass

def call_bankrollent(event):
    v1.set("")
    e.focus_set()

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
    
def confidentUnit(event):
    bank = float(v1.get())
    umin = float(1)
    umax = float(100)
    conf = float(cscale.get())
    umin = round((bank*.01)*umin,2)
    umax = round((bank*.01)*umax,2)
    ans = round(((conf - 0) * (umax - umin) / (100 - 0) + umin),2)
    v2.set(str(ans))

def runReduce():
    minus = float(v2.get())
    bank = float(v1.get())
    amt = round(float(bank) - minus,2)
    v1.set(amt)
    cscale.set("-1")
    v2.set("0")


master = tk.Tk()
master.title("BetUnitCalc")

v1 = tk.StringVar(master)
v1.set("0") 

v2 = tk.StringVar(master)
v2.set("0")

odds = tk.StringVar(master)
odds.set("0")

cscale = tk.Scale(orient='horizontal', from_=-1, to=100, command=confidentUnit)
clabel = tk.Label(master, text="Confidence")

label1 = tk.Label(master, text="Session Amt:")
e = tk.Entry(master, textvariable=v1)
label2 = tk.Label(master, text="Minus:")
w = tk.Entry(master, textvariable=v2)

c = tk.Button(master, text="Placed", command=runReduce)

label3 = tk.Label(master, text="Odds(+/-):")
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
label2.grid(row=0, column=1, sticky=N+W,padx=5)
w.grid(row=1, column=1, sticky=W,padx=5)

clabel.grid(row=2, column=0, sticky=W+E+N+S, padx=5,columnspan=2) 
cscale.grid(row=3, column=0, sticky=W+E+N+S, padx=5,columnspan=2) 
c.grid(row=4, column=0, sticky=W+E+N+S,padx=5,columnspan=2)

label3.grid(row=0, column=2,columnspan=2,sticky=W+E+N+S)
plus_button.grid(row=1, column=2,sticky=W+E+N+S)
minus_button.grid(row=1, column=3,sticky=W+E+N+S)

j.grid(row=2, column=2,columnspan=2,sticky=W+E+N+S)
lsum2.grid(row=3, column=2, columnspan=2,sticky=W+E+N+S)
d.grid(row=4, column=2, columnspan=2,sticky=W+E+N+S)

master.bind("-", call_minustoggle)
master.bind("+", call_plustoggle)
master.bind("<Return>", call_enterproc)
master.bind("<space>", call_bankrollent)

tk.mainloop()

