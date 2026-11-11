import qrcode
import os

url = input("Enter the url that you need to convert into qr code : ")
filename = input("In which name you want to save it with ? \n")

if not(filename.endswith(".png")):
    filename += ".png"


img = qrcode.make(url)
output_path = os.path.join(os.path.dirname(__file__), filename)
img.save(output_path)
