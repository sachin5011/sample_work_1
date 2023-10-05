import pyqrcode, png

code = pyqrcode.create('youtube.com')
code.png("Youtube.png")