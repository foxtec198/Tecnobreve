from flask import Flask, render_template, redirect
from os import getenv
from time import strftime as st
from datetime import datetime as dt, timezone, timedelta
import email.message as em
import smtplib
from psycopg2 import connect

app = Flask(__name__)


def now():
    tz_brl = timezone(timedelta(hours=-3))
    return dt.now().astimezone(tz_brl)

# HOME - TECNOBREVE ===============================================================
@app.route('/')
def home():
    return render_template('tecnobreve.html')

@app.route('/rfs')
def rfs():
    return render_template('rfs.html')

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
        <p style="position: fixed; bottom: 10px; color: gray; font-style: italic; margin-top: 20px;">Desenvolvido por Tecnobreve © {now().strftime('%Y')} </p>
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

# CHOPP MANIA =====================================================================
def enviar_email(nomeForm, emailForm, telForm, dataForm, dataEnvio, emailTo, pedido):
    # PARAMETROS DE EMAIL
    html = f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <div style="background-color: #000; padding: 10px; border-radius: 20px; margin: 20px;">
        <img src="https://firebasestorage.googleapis.com/v0/b/choppmania-828ed.appspot.com/o/modoBranco.png?alt=media&token=73957963-b24d-4331-b905-f6905cb3726d" width="100" style="margin-left: 10px;">
    </div>
    <div style="text-align: left; padding: 10px; margin: 20px;">
        <h1>Novo Pedido !</h1>
        <h4>Você tem um novo pedido a ser realizado!</h4>
        <hr>
        <p><b>Pedido:</b> {pedido}</p>
        <p><b>Nome:</b> {nomeForm}</p>
        <p><b>Email:</b> {emailForm}</p>
        <p><b>Telefone:</b> {telForm}</p>
        <p><b>Data do Evento:</b> {dataForm.strftime('%d/%m/%Y %H:%M')}</p>
        <p><b>Data do Pedido:</b> {dataEnvio.strftime('%d/%m/%Y %H:%M')}</p>
        <a href="https://api.whatsapp.com/send/?phone=55{telForm}">
            <button style="background: #a7c957; color: #fff; font-size: 16px;"> 
                <img src="https://firebasestorage.googleapis.com/v0/b/choppmania-828ed.appspot.com/o/icons8-whatsapp-50.png?alt=media&token=addb7a5a-9cec-4cd3-907b-20ce5be75295" width= "15">
                Enviar Mensagem 
            </button>
        </a>
        <hr>
        <p style="position: fixed; bottom: 10px; color: gray; font-style: italic; margin-top: 20px;">Desenvolvido por Tecnobreve © {now().strftime('%Y')} </p>
    </div>
    """ 
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
    msg['Subject'] = 'Novo Pedido'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html)
    server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    server.quit()
    print(f'Email enviado com sucesso para {emailTo}')

def get_brl():
    c.execute('rollback')
    c.execute('select tipo, valor from barril')
    return c.fetchall()

@app.route('/choppmania/')
def home_cm():
    global c
    with connect(host='stately-allowing-snapper.data-1.use1.tembo.io', port='5432', user='postgres', password='H6KAGLThX39kcNNH', database="RDC") as conn:
        c = conn.cursor()
        barris = sorted(get_brl())
        return render_template('choppmania.html', barris=barris)

@app.route('/choppmania/enviar/<nome>_<email>_<telefone>_<data>_<produto>')
def envio_choppmania(nome, email, telefone, data, produto):
    data = data.replace('T', ' ')
    data = now().strptime(data, '%Y-%m-%d %H:%M')
    dataEnvio = now()
    enviar_email(nome, email, telefone, data, dataEnvio, 'foxtec198@gmail.com', produto)
    enviar_email(nome, email, telefone, data, dataEnvio, 'contato.choppmania@gmail.com', produto)
    return redirect('/choppmania/enviado')

@app.route('/choppmania/enviado/')
def enviado_choppmania():
    return render_template('enviadochoppmania.html')

# IMOB 4Projetta ==================================================================
def enviar_email_imob(nome, telefone, emailTo, dataEnvio = st('%d/%m/%Y %H:%M')):
    # PARAMETROS DE EMAIL
    html = f"""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <div style="border: 2px solid #006494; padding: 10px; border-radius: 20px; margin: 20px;">
        <img src="https://firebasestorage.googleapis.com/v0/b/choppmania-828ed.appspot.com/o/marca.png?alt=media&token=8a902127-2005-40aa-9435-6a56be9f011a" width="100" style="margin-left: 10px;">
    </div>
    <div style="text-align: left; padding: 10px; margin: 20px;">
        <h1><b>Novo Lojista!</b></h1>
        <h4>Você tem um novo lojista a ser atendido!</h4>
        <hr>
        <p><b>Nome:</b> {nome}</p>
        <p><b>Telefone:</b> {telefone}</p>
        <p><b>Data do Contato:</b> {dataEnvio}</p>
        <a href="https://api.whatsapp.com/send/?phone={telefone}">
            <button style="background: #a7c957; color: #fff; font-size: 16px;"> 
                <img src="https://firebasestorage.googleapis.com/v0/b/choppmania-828ed.appspot.com/o/icons8-whatsapp-50.png?alt=media&token=addb7a5a-9cec-4cd3-907b-20ce5be75295" width= "15">
                Enviar Mensagem 
            </button>
        </a>
        <hr>
        <p style="position: fixed; bottom: 10px; color: gray; font-style: italic; margin-top: 20px;">Desenvolvido por Tecnobreve © {now().strftime('%Y')} </p>
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
    msg['Subject'] = 'Novo Lojista!'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html)
    server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    server.quit()
   
@app.route('/imob/')
def homeImob():
    return render_template('imob.html')

@app.route('/imob/enviar/<nome>_<telefone>')
def enviar_imob(nome, telefone):
    enviar_email_imob(nome, telefone, '4quattroprojetta@gmail.com')
    # enviar_email_imob(nome, telefone, 'ghostlagado@gmail.com')
    return redirect('/imob')

if __name__ == '__main__':
    port = getenv('PORT','8601')
    app.run(debug=True, host='0.0.0.0', port=port)