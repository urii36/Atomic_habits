from datetime import datetime, timedelta

from rest_framework import serializers


def validate_related_habit(value):
    """
    Валидатор: Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """
    if value['related_habit'] and value['reward']:
        raise serializers.ValidationError("You can't choose both a related habit and a reward.")


def validate_estimated_time(value):
    """
    Валидатор: Время выполнения должно быть не больше 120 секунд.
    """
    if value['estimated_time'] > 120:
        raise serializers.ValidationError("Estimated time should not exceed 120 seconds.")


def validate_rewarding_habit(value):
    """
    Валидатор: У приятной привычки не может быть вознаграждения или связанной привычки.
    """
    if value['is_reward'] and (value['reward'] or value['related_habit']):
        raise serializers.ValidationError("A rewarding habit should not have a reward or a related habit.")


def validate_frequency(value):
    """
    Валидатор: Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    """
    if value.get('frequency') not in ['daily', 'weekly']:
        raise serializers.ValidationError("The minimum frequency is once in 7 days for non-daily habits.")


def validate_notification_time(value):
    """
    Валидатор: Проверяет, можно ли установить уведомление для заданной привычки и времени уведомления
    """
    frequency = value.get('frequency')
    notification_time = value.get('notification_time')
    time = value['time']
    date_of_creation = datetime.now()
    mailing_date = datetime.combine(date_of_creation.date(), time)
    if notification_time == 'fifteen':
        mailing_date -= timedelta(minutes=15)
    elif notification_time == 'thirty':
        mailing_date -= timedelta(minutes=30)
    elif notification_time == 'hour':
        mailing_date -= timedelta(hours=1)
    elif notification_time == 'two_hours':
        mailing_date -= timedelta(hours=2)
    else:
        mailing_date -= timedelta(days=1)
    if notification_time == 'day' and frequency != 'weekly':
        raise serializers.ValidationError('24 hours is only enough for a weekly habit')
    elif mailing_date <= date_of_creation:
        raise serializers.ValidationError("You can't assign a habit for today")
