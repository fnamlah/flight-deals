import smtplib
import os
my_email = os.environ.get("my_email")
my_password = os.environ.get("my_password")
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # making the connection secure
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="faisal.python02@yahoo.com",
                                msg=f"Subject:Deal of the day\n\n{message}")
