import qrcode

data = 'http://www.puntoserrano.com.ar/'
img = qrcode.make(data)
img.save("qr.png")