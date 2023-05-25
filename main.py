import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = ''
email['to'] = ''
email['subject'] = 'jy wen fokkol'

email.set_content(' I am a Python MAster')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username', 'password')
    smtp.send_message(email)
    print('all good boss')


