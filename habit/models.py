from django.db import models

from users.models import User


class Habit(models.Model):
    """
    Модель, представляющая собой привычку пользователя.

    Поля:
    - user (ForeignKey): Пользователь, создавший привычку.
    - place (CharField): Место, в котором необходимо выполнять привычку.
    - notification_time (CharField): Уведомление до начала привычки.
    - time (TimeField): Время, когда необходимо выполнять привычку.
    - action (CharField): Действие, которое представляет из себя привычку.
    - is_reward (BooleanField): Признак приятной привычки.
    - related_habit (ForeignKey): Связанная привычка, если таковая имеется.
    - frequency (CharField): Периодичность выполнения привычки для напоминания в днях.
    - weekday (CharField): Старт выполнения привычки.
    - reward (CharField): Вознаграждение за выполнение привычки.
    - estimated_time (IntegerField): Время, которое предположительно потратит пользователь на выполнение привычки.
    - is_public (BooleanField): Признак публичности привычки.
    - date_of_start (DateField): Дата создания привычки и потом старта (нужно для еженедельного уведомления)
    - is_starting (BooleanField): Признак начала рассылки привычки, началась или нет в основ нужна для еженедельной.
    - notification (CharField): Тип уведомления телеграм/почта
    """
    NOTIFICATION_TIME_CHOICES = [
        ('fifteen', 'За 15 минут'),
        ('thirty', 'За 30 минут'),
        ('hour', 'За час'),
        ('two_hours', 'За 2 часа'),
        ('day', 'За 24 часа'),

    ]
    FREQUENCY_CHOICES = [
        ('daily', 'Ежедневная'),
        ('weekly', 'Еженедельная'),
    ]
    WEEKDAY_CHOICES = [
        ('today', 'Сегодня'),
        ('tomorrow', 'Завтра'),
    ]
    NOTIFICATION_CHOICES = [
        ('telegram', 'Телеграм'),
        ('email', 'Почта'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, help_text="Место, в котором необходимо выполнять привычку.")
    notification_time = models.CharField(max_length=20, choices=NOTIFICATION_TIME_CHOICES, default='thirty',
                                         help_text="За сколько присылать уведомления до начала привычки")
    time = models.TimeField(help_text="Время, когда необходимо выполнять привычку.")
    action = models.CharField(max_length=255, help_text="Действие, которое представляет из себя привычку.")
    is_reward = models.BooleanField(default=False, help_text="Признак приятной привычки.")
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                      help_text="Связанная привычка, если таковая имеется.")
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='daily',
                                 help_text="Периодичность выполнения привычки для напоминания в днях.")
    weekday = models.CharField(max_length=20, choices=WEEKDAY_CHOICES, default='today',
                               help_text="Старт выполнения привычки.")
    reward = models.CharField(max_length=255, blank=True, help_text="Вознаграждение за выполнение привычки.")
    estimated_time = models.IntegerField(
        help_text="Время, которое предположительно потратит пользователь на выполнение привычки.")
    is_public = models.BooleanField(default=False, help_text="Признак публичности привычки.")
    date_of_start = models.DateField(auto_now_add=True)
    is_starting = models.BooleanField(default=False)
    notification = models.CharField(max_length=20, choices=NOTIFICATION_CHOICES, default='telegram',
                                    help_text="Тип оповощения telegram/email.")

    def __repr__(self):
        """
        Возвращает строковое представление объекта привычки.

        Returns:
            str: Строковое представление объекта привычки.
        """
        return f"Habit{self.time, self.related_habit, self.frequency, self.weekday, self.date_of_start}"

    def __str__(self):
        """
        Возвращает строку, описывающую привычку.

        Returns:
            str: Строка с описанием привычки.
        """
        return f'Я буду {self.action} в {self.time}, в {self.place}'

    def get_message(self):
        """
        Возвращает сообщение, описывающее привычку.

        Если привычка является приятной (is_reward=True), сообщение включает информацию о действии, времени, месте,
        вознаграждении и, если есть, связанной привычке. В противном случае, сообщение содержит только информацию о
        действии, времени и месте выполнения привычки.

        Returns:
            str: Сообщение о привычке.
        """
        if not self.is_reward:
            message = f'Я буду {self.action} в {self.time}, в {self.place}.\n' \
                      f'Мне дается на это {self.estimated_time} секунд.\n'
            if self.related_habit:
                message += self.related_habit.get_message()
        else:
            message = f'Я буду {self.action} в {self.time}, в {self.place}.\n' \
                      f'Мне дается на это {self.estimated_time} секунд.\n'

        return message
