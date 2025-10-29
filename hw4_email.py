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