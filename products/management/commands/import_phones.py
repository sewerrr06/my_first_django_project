import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from products.models import Phone # Імпортуємо нашу модель

class Command(BaseCommand):
    help = 'Парсить телефони з Webscraper.io і зберігає в БД'

    def handle(self, *args, **kwargs):
        # 1. Налаштування
        url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
        self.stdout.write("🚀 Починаю завантаження сайту...")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.select('.thumbnail')
        
        self.stdout.write(f"🔎 Знайдено товарів: {len(items)}")

        # 2. Цикл по товарах
        for item in items:
            try:
                # --- ЛОГІКА ПАРСИНГУ (як у твоєму скрипті) ---
                dirty_name = item.select_one('.title').text
                name = dirty_name.strip()
                price_raw = item.select_one('.price').text
                price = int(float(price_raw.replace('$', ''))) # Чистимо ціну для БД
                
                description = item.select_one('.description').text
                
                url_tail = item.select_one('.title')['href']
                full_link = f"https://webscraper.io{url_tail}"

                dirty_reviews = item.select_one('.ratings').text
                reviews = int(dirty_reviews.strip().replace(' reviews', ''))
                # --- ЛОГІКА DJANGO (Збереження) ---
                # get_or_create перевіряє: якщо такий телефон (за назвою) є - не чіпає його.
                # Якщо немає - створює. Це рятує від дублікатів!
                phone, created = Phone.objects.get_or_create(
                    name=name,
                    defaults={
                        'price': price,
                        'description': description,
                        'url': full_link,
                        'reviews' : reviews
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'✅ Додано: {name} , {reviews}'))
                else:
                    self.stdout.write(f'zzz Вже є: {name} , {reviews}')
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Помилка: {e}'))

        self.stdout.write(self.style.SUCCESS('🎉 Робота завершена!'))