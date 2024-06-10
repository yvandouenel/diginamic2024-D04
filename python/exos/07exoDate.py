from datetime import datetime

current_date = datetime.today()


# datetime in string format for may 25 1999
input = "1998/10/23"
format = "%Y/%m/%d"

# convert from string format to datetime format
birth_date = datetime.strptime(input, format)


# différence entre les 2 dates
date_difference = current_date - birth_date

# Nombre d'années
years_difference = date_difference.days / 365

print(f"Age : {int(years_difference)}")
