import pyqrcode

url = input("enter url: ")

url = pyqrcode.create(url)
url.svg("newQR.svg", scale=8)