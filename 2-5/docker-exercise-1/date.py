import datetime
import os


today = datetime.date.today()
print("Today's date is:", today)

env_vars = os.environ
for var in env_vars:
    print(var, ":", env_vars[var])
