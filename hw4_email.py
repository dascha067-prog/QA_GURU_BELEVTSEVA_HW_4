from datetime import date

# 1. создаём словарь письма

email = {
    "subject": "Project meeting",
    "from": "manager@example.com",
    "to": "daria@example.com",
    "body": "Hi Daria! Reminder: meeting at 15:00. See you!"
}

# 2. создаём переменную с текущей датой в формате YYYY-MM-DD
send_date = date.today().strftime("%Y-%m-%d")

# добавляем дату в словарь
email["date"] = send_date

print(email)

# 3. Нормализация e-mail адресов: убрать пробелы по краям и привести к нижнему регистру
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Извлечь логин и домен из адреса отправителя
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# 5. Короткая версия текста: первые 10 символов + "..."
email["short_body"] = email["body"][:10] + "..."

# Выводим результат для проверки
print(email["short_body"])

# 6. Создаем списки доменов (личные и корпоративные)
personal_domains = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com',
    'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru'
]
corporate_domains = [
    'company.ru', 'corporation.com', 'university.edu',
    'organization.org', 'company.org', 'business.net'
]

# 7. Проверяем, что нет пересечений
intersection = set(personal_domains) & set(corporate_domains)
# Выводим результат
if intersection:
    raise ValueError(f"Personal and corporate domains intersect: {intersection}")

# 8. # Получаем домен отправителя из email["from"]
sender_domain = email["from"].split("@")[1]
#  Булево — отправитель корпоративный
is_corporate = sender_domain in corporate_domains

print(f"Is corporate sender: {is_corporate}")
