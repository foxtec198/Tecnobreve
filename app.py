from flask import Flask, render_template
from os import getenv

app = Flask(__name__)

@app.route('/')
def homer():
    return render_template('index2.html')
    
if __name__ == '__main__':
    port = getenv('PORT','8601')
    app.run(host='0.0.0.0', port=port)