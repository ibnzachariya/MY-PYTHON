# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=year, month=month, day=day_of_week)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "zaabdulfataio@gmail.com"
PASSWORD = "jhrxtbpiotpjlywb"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ibnzachariya@gmail.com", msg=f"Subject:Weekend Quote\n\n{quote}")
