import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "zaabdulfataio@gmail.com"
MY_PASSWORD = "jhrxtbpiotpjlywb"

# Load birthdays
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

# Today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# If today matches a birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # Pick a random letter template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ibnzachariya@gmail.com",
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
