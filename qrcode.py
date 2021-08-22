
import pyqrcode
def get_qrcode():
    qr = pyqrcode.create('text')
    qr.png('qr.png',scale = 8)
    qr.svg("qr.svg", scale = 8) 