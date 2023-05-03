import calendar
from datetime import datetime
from utils.suport.dicts import meses_translate


def list_days_month(date=datetime.now()):
    date_now = date
    year = date_now.year
    month = date_now.month
    month_name = date_now.strftime("%B")
    month_name_translate = month_name.replace(
        month_name, meses_translate[month_name]
    )

    # Configurar para semana começar no Domingo
    calendar.setfirstweekday(6)

    calendario = calendar.monthcalendar(year, month)

    return calendario, month_name_translate
