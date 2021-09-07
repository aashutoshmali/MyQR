from flask import Flask, render_template, request, redirect, url_for, session, send_file, send_from_directory
import pyqrcode
import png
from pyqrcode import QRCode
import os
app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def index():
	if request.method == 'POST' and 'text' in request.form:
		text = request.form['text']
		return get_qrcode(text=text)
	else:
		msg = 'Please Insert text !'
		return render_template('index.html', msg = msg)
def get_qrcode(text):
    qr = pyqrcode.create(text)
    qr.png('qr.png',scale = 8)
    qr.svg("qr.svg", scale = 8)
    img = 'qr.png'
    return render_template('qr.html', text=text)

@app.route('/download', methods=['GET','POST'])
def downloadfile():
     path = 'qr.png'
     return send_file(path, as_attachment=True)
@app.route('/save', methods=['GET','POST'])
def save():
     path = 'qr.svg'
     return send_file(path, as_attachment=True)
if __name__ == '__main__':
   app.run(debug=True)
