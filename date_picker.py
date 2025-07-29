# import necessary libraries
from tkinter import Tk, Label, Button
from tkcalendar import Calendar

selected_date = None
# Define a function to pick a date using tkcalendar
def pick_date():
    def get_date():
        global selected_date
        selected_date = cal.get_date()
        top.destroy()

    top = Tk()
    top.title("Select Appointment Date")
    Label(top, text="Choose a date:").pack(pady=10)
    cal = Calendar(top, selectmode='day')
    cal.pack(pady=20)
    Button(top, text="Confirm", command=get_date).pack(pady=10)
    top.mainloop()
    return selected_date