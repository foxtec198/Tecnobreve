import smtplib
import email.message as em

class Email:
    def __init__(self) -> None:
        self.host = 'smtp.gmail.com'
        self.port = '587'
        self.email = 'foxtec198@gmail.com'
        self.senha = 'fwmeylchtupgrmeb'
        
    def enviar(self, emailTo, body='HTML'):
        server = self.conectar()
        
        msg = em.Message()
        msg['From'] = self.email
        msg['To'] = emailTo
        msg['Subject'] = 'Novo Contato - (Não Responder)'

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body)
        server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

    def conectar(self):
        server = smtplib.SMTP(self.host, self.port)
        server.ehlo()
        server.starttls()
        server.login(self.email, self.senha)
        return server
