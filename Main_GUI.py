# import necessary libraries user-defined modules and third-party modules
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from helper import validate_date, save_order
# Define Customer, services and Oedr classes, 
# especially for GUI, app classes is needed to create a GUI application.
class Customer:
    def __init__(self, name, car_model):
        self.name = name
        self.car_model = car_model

    def get_info(self):
        return f"Customer Name: {self.name}, Car Model: {self.car_model}"

class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order(Service):
    def __init__(self, name, price, appointment, customer):
        super().__init__(name, price)
        self.appointment = appointment
        self.customer = customer

    def summary(self):
        return (
            f"{self.customer.get_info()}\n"
            f"Service: {self.name}\n"
            f"Price: ${self.price}\n"
            f"Appointment: {self.appointment}"
        )

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile Car Wash Booking")

        # Variables
        self.name_var = tk.StringVar()
        self.car_model_var = tk.StringVar()
        self.service_var = tk.StringVar()
        self.service_var.set("Basic Wash")
        self.date_var = tk.StringVar()

        # Widgets
        tk.Label(root, text="Your Name:").grid(row=0, column=0, sticky='e')
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(root, text="Car Model:").grid(row=1, column=0, sticky='e')
        tk.Entry(root, textvariable=self.car_model_var).grid(row=1, column=1)
        # using dictionary data type to display Services for selection
        tk.Label(root, text="Choose Service:").grid(row=2, column=0, sticky='ne')
        for i, (service, price) in enumerate({
            "Basic Wash": 25, "Deluxe Wash": 40, "Premium Detail": 60
        }.items()):
            tk.Radiobutton(root, text=f"{service} - ${price}",
                           variable=self.service_var, value=service).grid(row=2+i, column=1, sticky='w')

        tk.Label(root, text="Appointment Date:").grid(row=5, column=0, sticky='e')
        self.calendar = Calendar(root, selectmode='day')
        self.calendar.grid(row=5, column=1)

        tk.Button(root, text="Submit Order", command=self.submit_order).grid(row=6, column=0, columnspan=2, pady=10)
    # define a method to submit the order
    def submit_order(self):
        name = self.name_var.get()
        car_model = self.car_model_var.get()
        service = self.service_var.get()
        date = self.calendar.get_date()
        # Validate input fields
        if not name or not car_model:
            messagebox.showerror("Error", "Please enter all fields.")
            return
        # Create Customer and Order objects
        customer = Customer(name, car_model)
        price = {"Basic Wash": 25, "Deluxe Wash": 40, "Premium Detail": 60}[service]
        order = Order(service, price, date, customer)
        # Validate date and save order
        if not validate_date(date):
            messagebox.showerror("Invalid Date", "Choose a date within 1 year from today.")
            return

        save_order(order)
        messagebox.showinfo("Success", "Order saved!\n\n" + order.summary())

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
