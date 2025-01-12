import pyqrcode # type: ignore

link = input("กรอกข้อมูล QR-CODE : ")
qr_code = pyqrcode.create(link)
qr_code.png( "QRCode.png", scale = 5)
qr_code.show