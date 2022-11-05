import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Password  Recovery'
msg['From'] = '@gmail.com'
msg['To'] = 'nimishwadhawan12@gmail.com'
msg.set_content('Your  password  for  parkingclick  account  is  :: ')
smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp.login('parkingclickofficial@gmail.com','hhuryikxggjiwfnu')
smtp.send_message(msg)