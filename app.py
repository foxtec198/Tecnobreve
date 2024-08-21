from flask import Flask, render_template, redirect
from os import getenv
from time import strftime as st
from datetime import datetime as dt
import email.message as em
import smtplib

app = Flask(__name__)

# HOME - TECNOBREVE ===============================================================
@app.route('/')
def home():
    return redirect('https://tecnobreve.my.canva.site/portifolio')
# =================================================================================

# RINELE - PSICOLOGA ==============================================================
def enviar_email(nome, telefone, emailTo, dataEnvio = st('%d/%m/%Y %H:%M')):
    # PARAMETROS DE EMAIL
    html = f"""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <div style="background-color: #006494; padding: 10px; border-radius: 20px; margin: 20px;">
        <img src="https://firebasestorage.googleapis.com/v0/b/choppmania-828ed.appspot.com/o/logoWhite.png?alt=media&token=3d861237-d85f-4c14-83bd-4138f973ecea" width="100" style="margin-left: 10px;">
    </div>
    <div style="text-align: left; padding: 10px; margin: 20px;">
        <h1><b>Novo contato!</b></h1>
        <h4>Você tem um novo contato a ser realizado!</h4>
        <hr>
        <p><b>Nome:</b> {nome}</p>
        <p><b>Telefone:</b> {telefone}</p>
        <p><b>Data do Pedido:</b> {dataEnvio}</p>
        <a href="https://api.whatsapp.com/send/?phone=55{telefone}">
            <button style="background: #a7c957; color: #fff; font-size: 16px;"> 
                <img src="https://firebasestorage.googleapis.com/v0/b/choppmania-828ed.appspot.com/o/icons8-whatsapp-50.png?alt=media&token=addb7a5a-9cec-4cd3-907b-20ce5be75295" width= "15">
                Enviar Mensagem 
            </button>
        </a>
        <hr>
        <p style="position: fixed; bottom: 10px; color: gray; font-style: italic; margin-top: 20px;">Desenvolvido por Tecnobreve © {dt.now().strftime('%Y')} </p>
    </div>""" 

    host = 'smtp.gmail.com'
    port = '587'
    email = 'foxtec198@gmail.com'
    senha = 'fwmeylchtupgrmeb'
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(email, senha)
    
    # EMAIL EM SI
    msg = em.Message()
    msg['From'] = email
    msg['To'] = emailTo
    msg['Subject'] = 'Novo Contato'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html)
    server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    server.quit()

@app.route('/rinele/')
def rinele():
    return render_template('rinele.html')

@app.route('/rinele/enviar/<nome>_<telefone>')
def enviar(nome, telefone):
    enviar_email(nome, telefone, 'psicologarinelemazaquatro@hotmail.com')
    return redirect('/rinele')
# ==================================================================================

if __name__ == '__main__':
    port = getenv('PORT','8601')
    app.run(debug=True, host='0.0.0.0', port=port)