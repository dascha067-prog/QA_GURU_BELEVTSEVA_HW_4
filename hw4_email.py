import math
from datetime import date

# 1. создаю словарь письма

email = {
    "subject": "Project meeting",
    "from": "manager@example.com",
    "to": "daria@example.com",
    "body": "Hi Daria! Reminder: meeting at 15:00. See you!"
}

# 2. создаю переменную с текущей датой в формате YYYY-MM-DD
send_date = date.today().strftime("%Y-%m-%d")

# добавляею дату в словарь
email["date"] = send_date

print(email)

# 3. Нормализую e-mail адресов: убрать пробелы по краям и привести к нижнему регистру
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Извлекаю логин и домен из адреса отправителя
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# 5. Короткая версия текста: первые 10 символов + "..."
email["short_body"] = email["body"][:10] + "..."

# Вывожу результат для проверки
print(email["short_body"])

# 6. Создаю списки доменов (личные и корпоративные)
personal_domains = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com',
    'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru'
]
corporate_domains = [
    'company.ru', 'corporation.com', 'university.edu',
    'organization.org', 'company.org', 'business.net'
]

# 7. Проверяю, что нет пересечений
intersection = set(personal_domains) & set(corporate_domains)
# Выводим результат
if intersection:
    raise ValueError(f"Personal and corporate domains intersect: {intersection}")

# 8. Получаю домен отправителя из email["from"]
sender_domain = email["from"].split("@")[1]
#  Булево — отправитель корпоративный
is_corporate = sender_domain in corporate_domains

print(f"Is corporate sender: {is_corporate}")

# 9. Заменяю табы и переводы строк на пробелы
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# Вывожу результат
print(email["clean_body"])

# 10. Формирую длинный текст отправленного письма
email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]}
{email["clean_body"]}"""

# Вывожу результат
print(email["sent_text"])

#  11. Рассчитываю количество страниц печати
pages = math.ceil(len(email["sent_text"]) / 500)

print("Количество страниц:", pages)
