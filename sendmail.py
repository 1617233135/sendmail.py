import smtplib
import email.mime.multipart
import email.mime.text

msg=email.mime.multipart.MIMEMultipart()
msg['frmom']='13236093861@163.com'
msg['to']='147951030@qq.com'
msg['subject']='test'
content='''''
    你好，
          这是一封自动发送的邮件。
          
          
'''
txt=mail.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib
smtp=smtplib.SMTP()
smtp.connect('smtp.qq.com','25')
smtp.login('13236093861@163.com','zxy510302')
smtp.sendmail('13236093861@163.com','1479510302@qq.com',str(msg))
smtp.quit()
