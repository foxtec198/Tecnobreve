from flask import Flask, render_template
from os import getenv

app = Flask('tecnobreve')

@app.route('/')
def home():
    return render_template('index2.html')
    
if __name__ == '__main__':
    port = getenv('PORT','5000')
    app.run(host='0.0.0.0', port=port)