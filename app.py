from flask import Flask, render_template, jsonify
import os

#=========================================================

app = Flask(__name__)

app.debug=True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') \
        if os.environ.get('DATABASE_URL') else 'sqlite:///test.db'

#=========================================================

@app.route('/')
def landing_page(name=None):
    return render_template('landing.html', name=name)

#@app.route('/register')

#@app.login('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)