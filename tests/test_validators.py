from datetime import time

import pytest
from habit.validators import (
    validate_related_habit,
    validate_estimated_time,
    validate_rewarding_habit,
    validate_frequency,
    validate_notification_time
)
from rest_framework.exceptions import ValidationError


def test_validate_related_habit():
    valid_data = {'related_habit': None, 'reward': ''}
    validate_related_habit(valid_data)  # Не должно вызывать ошибку

    invalid_data = {'related_habit': 1, 'reward': 'Тестовая награда'}
    with pytest.raises(ValidationError):
        validate_related_habit(invalid_data)


def test_validate_estimated_time():
    valid_data = {'estimated_time': 60}
    validate_estimated_time(valid_data)  # Не должно вызывать ошибку

    invalid_data = {'estimated_time': 150}
    with pytest.raises(ValidationError):
        validate_estimated_time(invalid_data)


def test_validate_rewarding_habit():
    valid_data = {'is_reward': True, 'reward': '', 'related_habit': None}
    validate_rewarding_habit(valid_data)  # Не должно вызывать ошибку

    invalid_data = {'is_reward': True, 'reward': 'Тестовая награда', 'related_habit': None}
    with pytest.raises(ValidationError):
        validate_rewarding_habit(invalid_data)


def test_validate_frequency():
    valid_data = {'frequency': 'daily'}
    validate_frequency(valid_data)  # Не должно вызывать ошибку

    invalid_data = {'frequency': 'monthly'}
    with pytest.raises(ValidationError):
        validate_frequency(invalid_data)


