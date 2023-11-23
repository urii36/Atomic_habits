from rest_framework import serializers

from habit.models import Habit
from habit.validators import validate_related_habit, validate_estimated_time, validate_rewarding_habit, \
    validate_frequency, validate_notification_time


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.
    """

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        Валидаторы для модели Habit.
        """
        validate_related_habit(data)
        validate_estimated_time(data)
        validate_rewarding_habit(data)
        validate_frequency(data)
        validate_notification_time(data)
        return data
