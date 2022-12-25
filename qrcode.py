import pyqrcode
import png
from pyqrcode import QRCode
def generate_qrcode(url):
    code = pyqrcode.create(url)
    code.png('test.png', scale=8)


url = input('Enter your URL: ')
generate_qrcode(url)
print('Work ended look at the png (test.png) file!')