import smtplib
import random
from info import user, passwd, name_dict

# Словарь имя - мейл находится в отдельном файле


# данные почтового сервиса
server = "smtp.mail.ru"
port = 587

keys_name = list(name_dict.keys())
list_choice_name = keys_name[:]


def choice_():
    for name in keys_name:
        list_choice_name.remove(name)
        choice_name_true = random.choice(list_choice_name)
        list_choice_name.append(name)
        name_dict[name] = (name_dict[name], choice_name_true)


def letter(name, info):
    # тема письма
    subject = 'Секретный санта.'
    # кому
    to = info[0]
    # кодировка письма
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'
    # текст письма
    text = f"Привет, {name}! Ты даришь подарок {info[1]}"

    # формируем тело письма
    body = "\r\n".join((f"From: {user}", f"To: {to}",
                        f"Subject: {subject}", mime, charset, "", text))
    smtp.sendmail(user, to, body.encode('utf-8'))


if __name__ == '__main__':
    choice_()
    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(user, passwd)
        # пробуем послать письмо
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    for i in list(name_dict.keys()):
        letter(i, name_dict[i])
    smtp.quit()
