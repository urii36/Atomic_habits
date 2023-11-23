import os

from django.core.management import BaseCommand
from faker import Faker

from habit.models import Habit
from users.models import User

fake = Faker()


class Command(BaseCommand):
    """
        Команда для сброса и добавления тестовых данных в модель Payment.

        Метод `handle` выполняет следующие шаги:
        1. Удаляет все записи в моделях User, Habit.
        2. Создает 5 фейковых пользователей и 15 фейковых привычек для каждого пользователя.

        Raises:
            Exception: В случае возникновения ошибки при импорте данных.


        Attributes:
            help (str): Описание команды для вывода при запуске `python manage.py help`.
    """
    help = 'Reset and add User and Habit models'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Habit.objects.all().delete()
        try:
            for _ in range(5):
                email = fake.email()
                phone = fake.numerify()
                country = fake.country()
                first_name = fake.first_name()
                last_name = fake.last_name()
                user = User.objects.create(email=email, phone=phone, country=country,
                                           first_name=first_name, last_name=last_name)
                user.set_password(os.getenv('ADMIN_PASSWORD'))
                user.save()
                for _ in range(15):
                    Habit.objects.create(
                        user=user,
                        place=fake.word(),
                        time=fake.time(),
                        action=fake.sentence(),
                        is_reward=fake.boolean(),
                        related_habit=None,
                        frequency=fake.word(),
                        reward=fake.sentence(),
                        estimated_time=fake.random_int(min=1, max=120),
                        is_public=fake.boolean())
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте данных: {e}'))

        else:
            self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных'))
