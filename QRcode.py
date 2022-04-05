import qrcode
img = qrcode.make('The link that you want to generate QR code for')
img.save("imageName.png")