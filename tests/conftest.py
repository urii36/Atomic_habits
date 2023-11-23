import pytest

from habit.models import Habit
from users.models import User


@pytest.fixture
def user():
    return User.objects.create(email='testuser@example.com', password='testpassword')


@pytest.fixture
def habit(user):
    return Habit(
        user=user,
        place="Тестовое место",
        notification_time="thirty",
        time="12:00:00",
        action="Тестовое действие",
        is_reward=False,
        frequency="daily",
        weekday="today",
        reward="Тестовая награда",
        estimated_time=60,
        is_public=True,
        is_starting=False,
        notification="telegram"
    )
