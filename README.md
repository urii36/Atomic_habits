Atomic Habits App
Добро пожаловать в приложение "Atomic Habits"! Это приложение поможет вам управлять вашими привычками и целями, соблюдать регулярность и отслеживать свой прогресс. В этом README мы предоставим вам информацию о проекте и его настройках.

Описание проекта
Atomic Habits - это веб-приложение, разработанное для помощи пользователям создавать, отслеживать и поддерживать полезные привычки. Приложение предоставляет возможность создавать привычки, устанавливать напоминания и отслеживать выполнение целей.

Стек технологий
Проект разработан с использованием следующего технологического стека:

Python 3.11
Django: веб-фреймворк для создания веб-приложений
Django REST framework: библиотека для создания RESTful API
Celery: для асинхронных задач
Redis: как брокер сообщений для Celery
HTML/CSS: для пользовательского интерфейса
Инструкция по установке
Чтобы развернуть проект и начать использовать его, выполните следующие шаги:

Склонируйте репозиторий: Выполните команду Git для клонирования репозитория на свой локальный компьютер.

git clone https://github.com/AndreyAgeew/atomic_habits.git
Установите зависимости::

cd atomic_habits
pip install -r requirements.txt
Настройте файл .env: Создайте файл .env в корневой директории проекта и добавьте в него переменные среды, например:

SECRET_KEY='your_secret_key'
DOMAIN_NAME='http://127.0.0.1:8000/'
DATABASES_NAME='your_database_name'
DATABASES_PASSWORD='your_database_password'
EMAIL_HOST_USER='your_email@gmail.com'
EMAIL_HOST_PASSWORD='your_email_password'
CACHES_LOCATION='redis://127.0.0.1:6379'
ADMIN_PASSWORD='your_admin_password'
CHAT_ID_ADMIN='your_chat_id'
MODERATOR_EMAIL='your_moderator_email'
STRIPE_API_KEY='your_stripe_api_key' #необязательно
CELERY_BROKER_HOST='redis://127.0.0.1:6379/0'
TELEGRAM_API_TOKEN='your_telegram_api_token'
Выполните миграции для создания базы данных:

python manage.py migrate
Запустите приложение:

python manage.py runserver
Откройте приложение: Перейдите в веб-браузере по адресу http://127.0.0.1:8000/ и начните использовать приложение.

Краткая инструкция по эндпоинтам
В приложении "Atomic Habits" есть несколько важных эндпоинтов:

/habits/ - список и создание привычек.
/habits/int:pk/ - просмотр, обновление и удаление привычки.
/habits/public/ - список публичных привычек.
Важаный момент Celery для Windows
Запустите Celery для асинхронной обработки задач, таких как отправка уведомлений:

celery -A atomic_habits worker -l info -P eventlet
celery -A atomic_habits beat
