import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address = 'poczta.o2.pl'
port = 465
login = 'stachulemko@o2.pl'
password = 'Iwonabos9'
#app_password = 'wbmvedrkrlcinmbh'

# Tworzenie wiadomości
wiadomosc = MIMEMultipart()
wiadomosc['From'] = 'stachulemko@o2.pl'
wiadomosc['To'] = 'akepka@o2.pl'
wiadomosc['Subject'] = 'Temat'
tresc = 'Ala ma kota'
wiadomosc.attach(MIMEText(tresc, 'plain'))

smtpObj = smtplib.SMTP_SSL(address, port)
print(type(smtpObj))

code, msg = smtpObj.ehlo()

if code == 250:
    # smtpObj.starttls() #tylko dla TLS (NIE-SSL)

    code_auth, msg_auth = smtpObj.login(login, password)
    if code_auth == 235:
        for i in range(10):
            smtpObj.sendmail('stachulemko@o2.pl',
                             'akepka@o2.pl',
                             wiadomosc.as_string()
                             )
        smtpObj.quit()
        print("Finish")
    else:
        print(code_auth, msg_auth)

else:
    print(code, msg)
