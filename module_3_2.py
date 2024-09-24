def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if print('@' not in recipient, sender) and print(".com" or ".ru" or ".net" not in recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
                 sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
                 sender='urban.teacher@mail.ru'))
