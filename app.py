from flask import Flask, render_template, request, redirect, url_for, session, send_file, send_from_directory
import pyqrcode
import png
from pyqrcode import QRCode
from qrcode import get_qrcode

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def index():
	if request.method == 'POST' and 'text' in request.form:
		text = request.form['text']
		return get_qrcode()
	else:
		msg = 'Please Insert text !'
		return render_template('index.html', msg = msg)
@app.route('/download', methods=['GET','POST'])
def downloadfile():
      path = "/qr.png"
      return send_file(path, as_attachment=True)

if __name__ == '__main__':
   app.run(debug=True)
