from datetime import datetime, timedelta


def _check_starting(habit, current_day):
    """
    Проверяет, начинается ли привычка сегодня или завтра, и устанавливает флаг `is_starting` в True, если так.

    :param habit: Привычка для проверки
    :param current_day: Текущий день
    """
    if not habit.is_starting:
        if habit.weekday == 'today':
            habit.is_starting = True
        elif habit.weekday == 'tomorrow' and current_day == habit.date_of_start.day + 1:
            habit.is_starting = True
        habit.save()


def _check_frequency_weekly(habit):
    """
    Обновляет дату начала привычки в зависимости от выбранной частоты (ежедневно или еженедельно).

    :param habit: Привычка, для которой обновляется дата начала
    """
    if habit.frequency == 'weekly':
        habit.date_of_start += timedelta(days=7)
    else:
        habit.date_of_start += timedelta(days=1)
    habit.save()


def _get_mailing_time(habit):
    """
    Возвращает день, час и минуту для отправки уведомления о привычке.

    :param habit: Привычка для которой вычисляется время уведомления
    :return: Кортеж (день, час, минута)
    """
    mailing_date = datetime.combine(habit.date_of_start, habit.time)

    if habit.notification_time == 'fifteen':
        mailing_date -= timedelta(minutes=15)
    elif habit.notification_time == 'thirty':
        mailing_date -= timedelta(minutes=30)
    elif habit.notification_time == 'hour':
        mailing_date -= timedelta(hours=1)
    elif habit.notification_time == 'two_hours':
        mailing_date -= timedelta(hours=2)
    else:
        mailing_date -= timedelta(days=1)

    return mailing_date.day, mailing_date.hour, mailing_date.minute
