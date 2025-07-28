from datetime import datetime
from helper import validate_date, save_order
from date_picker import pick_date

# Define services
services = {
    "1": {"name": "Basic Wash", "price": 25},
    "2": {"name": "Deluxe Wash", "price": 40},
    "3": {"name": "Premium Detail", "price": 60}
}

class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name} - ${self.price}"

class Customer:
    def __init__(self, name, car_model):
        self.name = name
        self.car_model = car_model

    def get_info(self):
        return f"Customer Name: {self.name}, Car Model: {self.car_model}"

class Order(Service):  # Subclass of Service
    def __init__(self, name, price, appointment, customer):
        super().__init__(name, price)
        self.appointment = appointment
        self.customer = customer  # Customer object

    def summary(self):
        return (
            f"{self.customer.get_info()}"
            f"Service: {self.name}"
            f"Price: ${self.price}"
            f"Appointment: {self.appointment}"
        )

def select_package():
    print("Available Car Wash Packages:")
    for key, value in services.items():
        print(f"{key}. {value['name']} - ${value['price']}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in services:
            selected = services[choice]
            return Service(selected["name"], selected["price"])
        else:
            print("Invalid choice. Please try again.")

def main():
    print("=== Welcome to Mobile Car Wash Booking ===")

    # Get customer input
    customer_name = input("Enter your name: ")
    car_model = input("Enter your car model: ")
    customer = Customer(customer_name, car_model)

    # Select service
    service = select_package()

    # Pick date
    print("A calendar window will open for you to pick a date...")
    date_input = pick_date()
    if not validate_date(date_input):
        print("Invalid date. Please run the program again.")
        return

    # Create order
    order = Order(service.name, service.price, date_input, customer)

    # Display and save
    print("\nOrder Summary:")
    print(order.summary())
    save_order(order)
    print("Thank you for booking with us!")

if __name__ == "__main__":
    main()