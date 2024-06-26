import schedule
import time
import subprocess
import shutil
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def backup_files():
    source = "/path/to/source"
    destination = "/path/to/destination"
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_name = f"backup_{timestamp}.tar.gz"
    backup_path = shutil.make_archive(backup_name, 'gztar', source)
    shutil.move(backup_path, destination)
    print(f"備份完成：{backup_name}")
    send_email(backup_name)

def send_email(backup_name):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_password"

    subject = "自動化備份通知"
    body = f"文件備份已完成：{backup_name}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("通知郵件已發送")
    except Exception as e:
        print(f"郵件發送失敗：{e}")
    finally:
        server.quit()

schedule.every().day.at("01:00").do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(60)
