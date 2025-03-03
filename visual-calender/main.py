from tkinter import *
import calendar


def show_calender():
     gui = Tk()
     gui.config(background='grey')
     gui.title("Ultimate Calender for Year")
     gui.geometry("550x600")
     year = int(year_field.get())
     gui_content = calendar.calendar(year)
     calYear = Label(gui, text=gui_content)

     calYear.grid(row=5, column=1, padx=20)
     gui.mainloop()

    
if __name__ == "__main__":
    new = Tk()
    new.config(background='dark grey')
    new.title("Year Calender")
    new.geometry("250x140")
    cal = Label(new, text="Enter the year", bg='dark grey')

    year = Label(new, text="Show Calender", bg='dark grey')
    year_field = Entry(new)
    
    button = Button(new, text="Show Calender", fg="Black", bg="blue", command=show_calender)
    exit = Button(new, text="Exit", fg="Black", bg="blue", command=new.destroy)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    exit.grid(row=6, column=1)
    new.mainloop()
