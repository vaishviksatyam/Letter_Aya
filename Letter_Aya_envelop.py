from tkinter import *
from geopy.geocoders import Nominatim
import Letter_Aya_Letter
import Letter_Aya_Dashboard
def envelop():

    BackColor="#5d6d7e"
    TextboxColor="#85929e"
    ButtonColor="#ec7063"
    TextColor="#e8daef"

    def imports1():
        master1.destroy()
        Letter_Aya_Letter.Letter()
        
    def backimports1():
        master1.destroy()
        Letter_Aya_Dashboard.Dashboard()

    master1 = Tk()
    master1.geometry('1366x800')
    master1.configure(background=BackColor)
    master1.title("Letter Aya")

    Label(master1, text="To,", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=1,column=0)
    Label(master1, text="City:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=2,column=1)
    Label(master1, text="state:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=3,column=1)
    Label(master1, text="Country:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=4,column=1)
    Label(master1, text="PinCode:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=5,column=1)

    Label(master1, text="From,", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=6,column=0)
    Label(master1, text="City:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=7,column=1)
    Label(master1, text="state:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=8,column=1)
    Label(master1, text="Country:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=9,column=1)
    Label(master1, text="PinCode:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=10,column=1)


    e1 = Text(master1, height=1, width=15) #city
    e1.configure(background=TextboxColor)

    e2 = Text(master1, height=1, width=15) #state
    e2.configure(background=TextboxColor)

    e3 = Text(master1, height=1, width=15) #country
    e3.configure(background=TextboxColor)

    e4 = Text(master1, height=1, width=15) #pincode
    e4.configure(background=TextboxColor)


    e5 = Text(master1, height=1, width=15) #city
    e5.configure(background=TextboxColor)

    e6 = Text(master1, height=1, width=15) #state
    e6.configure(background=TextboxColor)

    e7 = Text(master1, height=1, width=15) #country
    e7.configure(background=TextboxColor)

    e8 = Text(master1, height=1, width=15) #pincode
    e8.configure(background=TextboxColor)


    e1.grid(row=2, column=2)
    e2.grid(row=3, column=2)
    e3.grid(row=4, column=2)
    e4.grid(row=5, column=2)

    e5.grid(row=7, column=2)
    e6.grid(row=8, column=2)
    e7.grid(row=9, column=2)
    e8.grid(row=10, column=2)

    Button(master1, text='Create', command=imports1,bg=ButtonColor,relief=FLAT).grid(row=7, column=5, sticky=W, pady=1)
    Button(master1, text='Go Back', command=backimports1,bg=ButtonColor,relief=FLAT).grid(row=7, column=4, sticky=W, pady=1)

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
