from tkinter import *
import datetime
import Letter_Aya_envelop
import Letter_Aya_sent

def Letter():
	def imports2():
		master2.destroy()
		Letter_Aya_envelop.envelop()

	def sends():
		master2.destroy()
		Letter_Aya_sent.sent()

	BackColor="#5d6d7e"
	TextboxColor="#85929e"
	ButtonColor="#ec7063"
	TextColor="#e8daef"


	master2 = Tk()
	now = datetime.datetime.now()
	master2.geometry('1366x800')
	master2.configure(background=BackColor)
	master2.title("Letter Aya")
	Label(master2, text="", bg=BackColor).grid(row=0)
	Label(master2, text="To:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=1)
	Label(master2, text="", bg=BackColor).grid(row=2)
	Label(master2, text="Date:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=3)
	Label(master2, text="", bg=BackColor).grid(row=4)
	Label(master2, text="From:", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=5)
	Label(master2, text="", bg=BackColor).grid(row=6)
	Label(master2, text="Letter", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=7,column=1)
	Label(master2, text="", bg=BackColor).grid(row=8)
	Label(master2, text=" ", bg=BackColor).grid(row=7,column=3)

	e1 = Text(master2, height=1, width=15)
	e1.configure(background=TextboxColor)
	e2 = Text(master2, height=1, width=15)
	e2.configure(background=TextboxColor)
	e3 = Text(master2, height=1, width=15)
	e3.configure(background=TextboxColor)
	e4 = Text(master2, height=20, width=100)
	e4.configure(background=TextboxColor)

	e1.grid(row=1, column=1)
	e2.grid(row=3, column=1)
	e2.insert(END,now.strftime("%Y-%m-%d"))
	e3.grid(row=5, column=1)
	e4.grid(row=7, column=2)


	Button(master2, text='back', command=imports2,bg=ButtonColor,relief=FLAT).grid(row=7, column=4, sticky=W, pady=1)
	Button(master2, text='Send', command=sends,relief=RAISED,bg=ButtonColor).grid(row=10, column=2, sticky=W, pady=1)

	mainloop()
