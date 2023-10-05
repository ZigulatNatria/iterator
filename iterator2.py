from datetime import date, timedelta   # импортируем необходимые модули из библиотеки datetime

"""
Вданном варианте решения задачи для получения календаря
будет использоваться модуль datetime
"""
cur = date(2022, 1, 1)                        # берём любую стартовую дату
yesterday = date.today() - timedelta(days=1)  # вычисляем вчерашний день :)
delta = timedelta(days=1)                     # определяем шаг в 1 день
dates = []                                    # список для хранения дат
while cur <= yesterday:                       # создаём цикл с условием
    dates.append(cur.strftime('%d %B'))       # добавляем полученное отформатированное значение
    cur += delta                              # делаем шаг +1 день

dares_iter = iter(dates)                      # преобразуем список в итератор

while True:
    print(next(dares_iter))                   # запускаем цикл вызова функции next()
                                              # по окончании списка будет вызвана ошибка StopIteration
