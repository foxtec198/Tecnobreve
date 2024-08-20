from flask import Flask, render_template
from os import getenv

app = Flask(__name__)

@app.route('/rinele')
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    port = int(getenv('PORT','3605'))
    app.run(debug=False, host='0.0.0.0', port=port)