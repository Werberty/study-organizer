import calendar
from datetime import datetime


def list_days_month(date=datetime.now()):
    date_now = date
    year = date_now.year
    month = date_now.month

    calendario = calendar.monthcalendar(year, month)

    return calendario
