from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(0, 0, 0)

pdf.image('qr.png', x = 0, y = 0, w = 50, h = 50)
pdf.output('QRinPDF.pdf', 'F')




