import datetime
import os

current_year = datetime.date.today().year

name = os.environ.get("NAME")
year = int(os.environ.get("YEAR"))

age = current_year - year

if age < 0:
    print("You haven't been born yet!")
elif age < 18:
    print(f"Hello {name}, you are {age} years old. You are still a minor.")
else:
    print(f"Hello {name}, you are {age} years old. You are an adult.")
