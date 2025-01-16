from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def redeem():
    current_time = datetime.now().strftime("%d %B %Y, %I:%M:%S %p")
    return render_template('redeem.html', current_time=current_time)

@app.route('/redeemed')
def redeemed():
    return render_template('redeemed.html')

if __name__ == '__main__':
    app.run(debug=True)
