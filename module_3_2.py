def send_email(message, recipient, * ,sender = "university.help@gmail.com"):
    endings =(".com", ".ru", ".net")
    check1= False
    check2 = False
    if "@" in recipient and "@" in sender:
        check1= True
    if recipient.endswith(endings) and sender.endswith(endings):
        check2=True
    if check1== False or check2== False:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == recipient:
        print("нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса", sender, "на адрес", recipient, ".")



send_email("Это сообщение для проверки связи", "vasyok 1337@gmail.com")
send_email("вы видите это сообщение как лучший студент курса!", "urban, fan@mail.ru", sender= "urban.infogmail.com")
send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru",)
send_email("напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")





