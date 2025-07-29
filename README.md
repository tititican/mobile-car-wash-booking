# mobile-car-wash-booking
CIS-30A Course Project
This is a Python program for scheduling mobile car wash services.

## Features
- Choose from 3 car wash packages
- Enter your name and car model
- Select a service date using a calendar (tkcalendar)
- Save summary to `order_summary.txt`

## Classes
- `Service`: Describes wash packages
- `Customer`: Stores name and car model
- `Order`: Inherits from `Service`, includes customer and date

## How to Run
1. Install `tkcalendar`:
   ```
   pip install tkcalendar
   ```
2. Install `tkinter`:
   ```
   pip install tkinter
   ```
3. Run the program:
   ```
   python main_GUI.py
   ```

## Files
- `main_GUI.py`: Main logic
- `helper.py`: Validation and file-saving
- `date_picker.py`: GUI calendar picker
- `order_summary.txt`: Output file
