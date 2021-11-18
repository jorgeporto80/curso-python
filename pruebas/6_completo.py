# importo librerías
from fpdf import FPDF
import qrcode
import requests
import pyttsx3

# Configuro el PDF
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(0, 0, 0)

# Invoco a la API y guardo el JSON en un diccionario
url = 'http://172.23.0.42:8087/api/comex/saldo?nroCuenta=1000008783&tipoDeCuenta=1'
resp = requests.get(url)
mi_diccionario = resp.json()

x = 20
y = 30
data = ""

# Inserto el logo del banco y el título
pdf.image('bs.png', x = x, y = 1, w = 50, h = 20)   # def image(x,y,w,h):
pdf.text(x,25,"INFORMACIÓN DE CUENTA")

# recorro el diccionario y escribo linea por linea el PDF
# Guardo la información para el QR
for clave, valor in mi_diccionario.items():
    y +=5
    linea = "{_clave}:\t {_valor}".format(_clave = clave, _valor = valor)
    pdf.text(x,y,linea)
    data = data +  linea + ', '

# Genero QR
img = qrcode.make(data)
img.save("qr.png")
# Inserto QR en el PDF
pdf.image('qr.png', x = 150, y = 10, w = 50, h = 50)
# Genero archivo PDF
pdf.output('Informe.pdf', 'F')

# Inicializo, seteo Español, velocidad de voz, texto a leer
quien_dice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

engine = pyttsx3.init()
engine.setProperty('voice',quien_dice)
engine.setProperty('rate',130)
engine.say(data)
engine.runAndWait()







