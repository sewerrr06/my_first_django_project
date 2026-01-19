import os
from celery import Celery

# 1. Вказуємо, де лежать налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# 2. Створюємо самого "Кухаря" (додаток Celery)
app = Celery('core')

# 3. Кажемо йому читати налаштування з файлу settings.py (все, що починається на CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# 4. Автоматично знаходити завдання (tasks) у всіх додатках (app)
app.autodiscover_tasks()