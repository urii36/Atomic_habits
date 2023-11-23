import os

from django.conf import settings
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
        Команда для сброса и добавления тестовых данных в модель Payment.

        Метод `handle` выполняет следующие шаги:
        Создает пользователя-админа

        Attributes:
            help (str): Описание команды для вывода при запуске `python manage.py help`.
    """
    help = 'Create superuser'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()

        super_user = User.objects.create(
            email=settings.EMAIL_HOST_USER,
            first_name='Admin',
            last_name='AH',
            is_staff=True,
            is_superuser=True,
            chat_id=os.getenv('CHAT_ID_ADMIN'),
            is_active=True,
        )
        super_user.set_password(os.getenv('ADMIN_PASSWORD'))
        super_user.save()
