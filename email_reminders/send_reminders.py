from datetime import date, timedelta
from reminders import childbirth_reminder, doula_reminder, marriage_reminder, baby_home_reminder

# Add 14 days to current date to send 2 week reminder
the_date = date.today() + timedelta(days=14)


if __name__ == "__main__":
    childbirth_reminder.send_childbirth_class_email_reminder(the_date)
    doula_reminder.send_doula_workshop_email_reminder(the_date)
    marriage_reminder.send_marriage_class_email_reminder(the_date)
    baby_home_reminder.send_bringing_baby_home_class_email_reminder(the_date)
