from tkinter import *
from geopy.geocoders import Nominatim
import Letter_Aya_Letter
import Letter_Aya_Dashboard
def sent():
	BackColor="#5d6d7e"
	TextboxColor="#85929e"
	ButtonColor="#ec7063"
	TextColor="#e8daef"
	def imports3():
	    master3.destroy()
	    Letter_Aya_Letter.Letter()

	def okays():
	    master3.destroy()
	    Letter_Aya_Dashboard.Dashboard()



	master3 = Tk()
	master3.geometry('1366x800')
	master3.configure(background=BackColor)
	master3.title("Letter Aya")
	Rec_Amount=0
	sent_Amount=0
	Label(master3, text="Letter Sent. "+ str(sent_Amount) + " points will automatically be reduced from account after the letter has been recieved by the reciever.", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=1,column=0)

	Button(master3, text='Okay', command=okays,bg=ButtonColor,relief=RAISED).grid(row=2, column=1, sticky=W, pady=4)
	Button(master3, text='Dont Send', command=imports3,bg=ButtonColor,relief=RAISED).grid(row=2, column=2, sticky=W, pady=4)

	mainloop()


	"""
	geolocator = Nominatim()
	location = geolocator.geocode("175 5th Avenue NYC")
	print(location.address)
	print((location.latitude, location.longitude))
	print(location.raw)

	measuring Distance

	>>> from geopy.distance import great_circle
	>>> newport_ri = (41.49008, -71.312796)
	>>> cleveland_oh = (41.499498, -81.695391)
	>>> print(great_circle(newport_ri, cleveland_oh).miles)
	537.1485284062816


	# vincinity distance
	>>> from geopy.distance import vincenty
	>>> newport_ri = (41.49008, -71.312796)
	>>> cleveland_oh = (41.499498, -81.695391)
	>>> print(vincenty(newport_ri, cleveland_oh).miles)
	538.3904451566326
	"""
