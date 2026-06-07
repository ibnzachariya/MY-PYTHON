import smtplib

my_email = "zaabdulfataio@gmail.com"
password = "password"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="ibnzachariya@gmail.com",
#                     msg="Subject:Hello\n\nThanks for viewing")
# connection.close()
#......OR..... to avoid using the connection.close
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="ibnzachariya@gmail.com",
                        msg="Subject:Hello\n\nThanks for viewing")
