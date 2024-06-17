from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date

root = Tk()
root.title("Age Calculator")
root.geometry("400x200")

def cal_date():
    selected_date = cal.get_date()
    year1 = selected_date.year
    current_date = date.today()
    year2 = current_date.year
    actual_year = year2 - year1

    text_label.config(text=f"You are {actual_year} years old :)")
  

icon = PhotoImage(file="C:/Users/hp/Desktop/More/PYTHON/PYTHON PROJECTS/Tkinter Projects/calendar.png")

text = Label(root,text="Age Calculator",font=("Comic Sans MS",28),padx=10,pady=15)
text.pack()

frame = Frame(root)
frame.pack()

img_label = Label(frame,image=icon,compound='right')
img_label.grid(row=0, column=1)
cal = DateEntry(frame, width= 20, background= "magenta3", foreground= "white",bd=5)
cal.grid(row=0, column=0)

text_label = Label(root,font=("Comic Sans MS",12))
text_label.pack()

button = Button(root,bg="green",fg="white",bd=4,text="Calculate",font=("Comic Sans MS",12),activebackground="green",activeforeground="white",command=cal_date)
button.pack(padx=10,pady=10)
root.mainloop()

