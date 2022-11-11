import qrcode

data = "Generating QR code"

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(back_color = 'white', fill_color='red')



img.save("/myqrimg.png")