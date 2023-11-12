import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email
from email.header import decode_header
# Konfiguracja parametrów
email_adres = 'stachulemko@o2.pl'
haslo = 'Iwonabos9'
odbiorca = 'akepka@o2.pl'
temat = 'Temat wiadomości'
tresc = 'Treść wiadomości'

# Tworzenie wiadomości
wiadomosc = MIMEMultipart()
wiadomosc['From'] = email_adres
wiadomosc['To'] = odbiorca
wiadomosc['Subject'] = temat

wiadomosc.attach(MIMEText(tresc, 'plain'))

# Ustanawianie połączenia z serwerem SMTP Gmail
serwer_smtp = smtplib.SMTP('poczta.o2.pl', 465)
serwer_smtp.starttls()

# Logowanie do konta Gmail
serwer_smtp.login(email_adres, haslo)

# Wysyłanie wiadomości
serwer_smtp.sendmail(email_adres, odbiorca, wiadomosc.as_string())

# Zamykanie połączenia
serwer_smtp.quit()


# -----------up_send------down_response-------

# # Konfiguracja parametrów
# email_adres = 'twoj@gmail.com'
# haslo = 'twoje_haslo'

# # Ustanawianie połączenia z serwerem IMAP Gmail
# serwer_imap = imaplib.IMAP4_SSL('imap.gmail.com')

# # Logowanie do konta Gmail
# serwer_imap.login(email_adres, haslo)

# # Wybieranie skrzynki pocztowej (np. 'inbox')
# serwer_imap.select('inbox')

# # Wyszukiwanie wiadomości - na przykład, odczytanie najnowszej wiadomości
# status, wiadomosc_ids = serwer_imap.search(None, 'ALL')

# # Pobieranie treści wiadomości
# wiadomosc_id = wiadomosc_ids[0].split()[-1]  # Ostatnia wiadomość
# status, wiadomosc_data = serwer_imap.fetch(wiadomosc_id, '(RFC822)')

# wiadomosc_raw = wiadomosc_data[0][1]
# wiadomosc = email.message_from_bytes(wiadomosc_raw)

# # Odczytywanie treści wiadomości
# temat = decode_header(wiadomosc['Subject'])[0][0]
# od_kogo = decode_header(wiadomosc['From'])[0][0]
# treść = ''

# if wiadomosc.is_multipart():
#     for part in wiadomosc.walk():
#         if part.get_content_type() == "text/plain":
#             treść = part.get_payload(decode=True).decode()
# else:
#     treść = wiadomosc.get_payload(decode=True).decode()

# print(f"Temat: {temat}")
# print(f"Od: {od_kogo}")
# print("Treść wiadomości:")
# print(treść)

# # Zamykanie połączenia
# serwer_imap.logout()
