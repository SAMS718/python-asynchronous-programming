import asyncio
import smtplib #simple mail transfer protocol (similar to HTTP).

async def send_email(subject,body,to):
    content="Hello World"
    mail=smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender='sams2005******@gmail.com'
    recipient='sriramkolapalli18@gmail.com'
    mail.login('sriramkolapalli18@gmail.com',' ****** ')
    header='To:'+receipient+'\n'+'From:' \
    +sender+'\n'+'subject: testmail\n'
    content=header+content
    mail.sendmail(sender, recipient, content)
    mail.close()

async def main():
    asyncio.create_task(send_email("xxxxxxx", "xxxxxxxx", "sriramkolapalli18@gmail.com"))
    print("Done")

asyncio.run(main())

'''
Refer this sendgrid repository for better understanding...
mail sent proof in pictures...
link : https://github.com/sendgrid/sendgrid-python/blob/main/use_cases/asynchronous_mail_send.md
'''
