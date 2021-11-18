import cv2

decoder = cv2.QRCodeDetector()
file_name = "qr.png"
image = cv2.imread(file_name)

link, data_points, straight_qrcode = decoder.detectAndDecode(image)

print(link)
print(data_points)
print(straight_qrcode)

# print(type(link))
# print(type(data_points))
# print(type(straight_qrcode))