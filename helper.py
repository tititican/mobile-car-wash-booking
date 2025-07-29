# This code is module, part of a mobile car wash booking system.
from datetime import datetime, timedelta
# Define the Customer and Order classes
def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%y")  # tkcalendar format
        today = datetime.today()
        one_year = today + timedelta(days=365)
        return today <= date_obj <= one_year
    except ValueError:
        return False
# Define a function to save the order summary to a file
def save_order(order):
    with open("order_summary.txt", "w") as file:
        file.write(order.summary())