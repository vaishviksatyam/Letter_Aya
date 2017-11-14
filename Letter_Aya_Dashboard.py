from tkinter import *
import xlrd
import os
from geopy.geocoders import Nominatim
import Letter_Aya_envelop
def Dashboard():


    def imports():
        master.destroy()
        Letter_Aya_envelop.envelop()

    workbook = xlrd.open_workbook('Documentation.xls')
    worksheet = workbook.sheet_by_name('Sheet1')

    BackColor="#5d6d7e"
    TextboxColor="#85929e"
    ButtonColor="#ec7063"
    TextColor="#e8daef"

    master = Tk()
    master.geometry('1366x800')
    master.configure(background=BackColor)
    master.title("Letter Aya")
    Label(master, text="From,", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=0,column=0)
    Label(master, text="to", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=0,column=1)
    Label(master, text="Date", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=0,column=2)
    Label(master, text="Status", bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=0,column=3)

    for rownum in range(1,worksheet.nrows):
        From=str(worksheet.cell(rownum, 12))
        To=str(worksheet.cell(rownum, 10))
        Date=str(worksheet.cell(rownum, 11))
        Status=str(worksheet.cell(rownum, 1))
        From=From[6:-1]
        To=To[6:-1]
        Date=Date[6:-1]
        Status=Status[6:-1]
        Label(master, text=str(From), bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=rownum,column=0)
        Label(master, text=str(To), bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=rownum,column=1)
        Label(master, text=str(Date), bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=rownum,column=2)
        Label(master, text=str(Status), bg=BackColor,justify=LEFT, font=("Helvetica", 13),foreground=TextColor).grid(row=rownum,column=3)

        Button(master, text='Send a new Letter', command=imports,bg=ButtonColor,relief=FLAT).grid(row=7, column=4, sticky=W, pady=1)
    mainloop()
