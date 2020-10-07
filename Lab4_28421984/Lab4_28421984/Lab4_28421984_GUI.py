from Lab4_28421984 import *
from tkinter import *

#functions
def Reset():
	global app
	app.destroy()
	main = Frame(root)
	main.grid(row = 3, column = 1)

	enter = Button(main, text = "Enter", command = Enter)
	enter.grid(row = 3, column = 1)

def Enter():
	global loc
	global point
	global numR
	global app
	global main

	app = Frame(root)
	app.grid(row = 3, column = 1)
	main.destroy()
	reset = Button(app, text = "Reset", command = Reset)
	reset.grid(row = 3, column = 1)

	m = MapQuest('AWeLhVHRZwow7As8WpQ48fuCT9IDwJOk')
	yourResults = m.pointOfInterest(loc.get(), point.get(), int(numR.get()))
	Label(app, text = "Results: ").grid(row = 4, column = 1, sticky = W)
	n = 4
	for i in yourResults:
		label = Label(app, text = i)
		label.grid(row = n, column = 1)
		n = n + 1

#title
root = Tk()
root.title('Points of Interest')
root.geometry('600x600')

main = Frame(root)
main.grid(row = 3, column = 1)
app = Frame(root)
app.grid(row = 3, column = 1)

#entries
Label(root, text = "Location").grid(row = 0, column = 0, sticky = W)
loc = Entry(root)
loc.grid(row = 0, column = 1)

Label(root, text = "Keyword").grid(row = 1, column = 0, sticky = W)
point = Entry(root)
point.grid(row = 1, column = 1)

Label(root, text = "Number of Results").grid(row = 2, column = 0, sticky = W)
numR = StringVar(root)
numR.set("5") # default value
numS = OptionMenu(root, numR, "5", "10", "15")
numS.grid(row = 2, column = 1)

#button
enter = Button(main, text = "Enter", command = Enter)
enter.grid(row = 3, column = 1)

root.mainloop()