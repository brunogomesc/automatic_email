import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fromaddr = EMAIL_DE_ENVIO
toaddr = EMAIL_DESTINATARIO

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['to'] = toaddr

msg['subject'] = "Teste de envio de e-mail automático"

html = """ 
<html>
      <body>
            <p>
                  Olá, <br>
                  Estou realizando teste de envio de e-mail utilizando Python.
                  <br>
                  <a href="">Clique neste link e assista esse video</a>
                  <br>
                  <br>
                  Att,
                  <br>
                  <br>
                  4DevTI
            </p>
      </body>
</html>
"""

part1 = MIMEText(html, "html")

msg.attach(part1)

s = smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login(fromaddr, SENHA_EMAIL)

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
