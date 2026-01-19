import requests
import csv  # <--- 1. Імпортуємо бібліотеку для роботи з файлами
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.select('.thumbnail')

# 2. Відкриваємо файл на запис ('w' - write)
# encoding='utf-8' важливо, щоб коректно записало гривні чи кирилицю
with open('phones.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # 3. Пишемо заголовки стовпчиків (перший рядок у Excel)
    writer.writerow(['Назва', 'Ціна', 'Опис', 'Посилання'])

    print(f"🚀 Починаю запис {len(items)} товарів у файл...")

    for item in items:
        name = item.select_one('.title').text
        price_clean = item.select_one('.price').text.replace('$', '')
        description = item.select_one('.description').text
        url_tail = item.select_one('.title')['href']
        full_link = f"https://webscraper.io{url_tail}"

        # 4. Записуємо дані у файл замість виводу на екран
        writer.writerow([name, price_clean, description, full_link])

print("✅ Готово! Перевір файл phones.csv у папці з проєктом.")