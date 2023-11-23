import pytest

from habit.models import Habit


@pytest.mark.django_db
def test_habit_model(habit):
    habit.save()
    retrieved_habit = Habit.objects.get(pk=1)

    assert retrieved_habit.user == habit.user
    assert retrieved_habit.place == "Тестовое место"


@pytest.mark.django_db
def test_habit_str_method(habit):
    str_representation = str(habit)
    assert "Тестовое действие" in str_representation
    assert "12:00:00" in str_representation
    assert "Тестовое место" in str_representation


@pytest.mark.django_db
def test_habit_get_message_method(habit):
    message = habit.get_message()
    assert "Тестовое действие" in message
    assert "12:00:00" in message
    assert "Тестовое место" in message
