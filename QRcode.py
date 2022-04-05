import qrcode
img = qrcode.make('https://www.instagram.com/salah.azzouzi/')
img.save("some_file.png")