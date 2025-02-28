import smtplib
import random
from email.mime.text import MIMEText


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


EMAIL_ADDRESS = "yuor@gmail.com"
EMAIL_PASSWORD = "abcd efgs hjds lomp"


def send_verification_code(receiver_email):
    verification_code = str(random.randint(100000, 999999))

    subject = "Ваш код подтверждения"
    body = f"Ваш код: {verification_code}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())
        server.quit()
        print(f"✅ Код {verification_code} отправлен на {receiver_email}")
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}")



receiver_email = input("Введите ваш email: ").strip()
send_verification_code(receiver_email)
