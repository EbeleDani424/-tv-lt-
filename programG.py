# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

# creates a Tk() object
root = Tk()

# sets the geometry of main 
# root window
root.geometry("200x200")


# function to open a new window 
# on a button click
def hWin():
	
	# Toplevel object which will 
	# be treated as a new window
	newWindow = Toplevel(root)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow, 
		text ="This is a new window").pack()

def tWin():
	
	# Toplevel object which will 
	# be treated as a new window
	newWindow = Toplevel(root)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow, 
		text ="This is a new window").pack()

def sWin():
	
	
		
		
	 

	# Nyit egy új ablakot
	sebWindow = Toplevel(root)

	# Az ablak "címe"
	sebWindow.title("Sebesség Átváltó")

	# beállítja az ablak méretét
	sebWindow.geometry("300x300")

	seblab = Label(sebWindow, text="Sebesség átváltás")
	seblab.grid (row = 0, column=1)
	sebent = tk.Entry(sebWindow, bd = 5)
	sebent.grid(row = 1, column=0)
	sebv = Button(sebWindow, 
	 		text ="Átvált", 
	 		command = sWin)
	Sclicked1 = StringVar() 
	beDrop = OptionMenu( sebWindow , Sclicked1 ,"","km/h", "mph", "m/s")
	beDrop.grid(row=1,column=1)
	Sclicked2 = StringVar()
	kiDrop = OptionMenu( sebWindow , Sclicked2 ,"","km/h", "mph", "m/s")
	kiDrop.grid(row=1,column=2)
	
	sebv.grid(row=2,column=0)
	sebvaltott = Label(sebWindow,text="")
	sebvaltott.grid (row = 3, column=0)
	


label = Label(root, 
			text ="Átváltó")

label.pack(pady = 10)

# a button widget which will open a 
# new window on button click
btn = Button(root, 
			text ="Hossz", 
			command = hWin)
btn.pack(pady = 10)
btn = Button(root, 
			text ="Tömeg", 
			command = tWin)
btn.pack(pady = 10)
btn = Button(root, 
			text ="Sebesség", 
			command = sWin)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()
