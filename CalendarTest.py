import calendar
import datetime

today_date = datetime.date.today()
today = today_date.strftime("%B %d")
tomorrow = (today_date + datetime.timedelta(days=1)).strftime("%B %d")
dayafter1 = (today_date + datetime.timedelta(days=2)).strftime("%B %d")
dayafter2 = (today_date + datetime.timedelta(days=3)).strftime("%B %d")