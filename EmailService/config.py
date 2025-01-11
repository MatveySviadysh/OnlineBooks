from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')
