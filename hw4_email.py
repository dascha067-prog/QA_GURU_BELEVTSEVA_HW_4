import math
from datetime import date

# 1. Создаю словарь письма

email = {
    "subject": "Project meeting",
    "from": "manager@example.com",
    "to": "daria@example.com",
    "body": "Hi Daria! Reminder: meeting at 15:00. See you!"
}

# 2. Создаю переменную с текущей датой в формате YYYY-MM-DD
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

# сделать списки уникальными, сохранив порядок
personal_domains  = list(dict.fromkeys(personal_domains))
corporate_domains = list(dict.fromkeys(corporate_domains))

print("Личные домены без дублей:", personal_domains)
print("Корпоративные домены без дублей:", corporate_domains)


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

# 12. Проверяю пустоту темы и тела письма
is_subject_empty = not email["subject"]
is_body_empty = not email["body"]

print("Пустая тема письма:", is_subject_empty)
print("Пустое тело письма:", is_body_empty)

# 13. Создаю «маску» e-mail отправителя
sender = email["from"]  # Беру адрес отправителя
login, domain = sender.split("@")  # Разделяю логин и домен по символу "@"
email["masked_from"] = login[:2] + "***@" + domain  # Беру первые 2 буквы логина и добавляю маску

print("Маска отправителя:", email["masked_from"])

# 14. Удаляю из списка личных доменов значения "list.ru" и "bk.ru"'
if "list.ru" in personal_domains:
    personal_domains.remove("list.ru")
if "bk.ru" in personal_domains:
    personal_domains.remove("bk.ru")

print("Личные домены:", personal_domains)

# Финальные принты для проверки
print(email)
print(is_corporate, is_subject_empty, is_body_empty, pages)
