#Задание
#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#
# Превратите строку "01/01/25 12:10:03.234567" в объект datetime

#Импортируем datetime
import datetime

#День назад
one_days = datetime.datetime.today() - datetime.timedelta(days=1)

#Сегодня

dt_now = datetime.datetime.now()

#30 дней назад
tri_deys = datetime.datetime.today() + datetime.timedelta(days=30)

# Превратите строку "01/01/25 12:10:03.234567" в объект datetime -> strftime("%Y/%m/%d/%H:%M:%S"))
print("Вчера" , one_days.strftime("%Y/%m/%d/%H:%M:%S"))
print("Сегодня" , dt_now.strftime("%Y/%m/%d/%H:%M:%S"))
print("30 дней назад" , tri_deys.strftime("%Y/%m/%d/%H:%M:%S"))

