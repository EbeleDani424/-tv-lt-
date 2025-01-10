# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

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
	hosszWin = Toplevel(root)

	# sets the title of the
	# Toplevel widget
	hosszWin.title("New Window")

	# sets the geometry of toplevel
	hosszWin.geometry("200x200")

    Entry(root,textvariable = name_var, font=('calibre',10,'normal'))



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
