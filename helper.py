from datetime import datetime, timedelta

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%y")  # tkcalendar format
        today = datetime.today()
        one_year = today + timedelta(days=365)
        return today <= date_obj <= one_year
    except ValueError:
        return False

def save_order(order):
    with open("order_summary.txt", "w") as file:
        file.write(order.summary())