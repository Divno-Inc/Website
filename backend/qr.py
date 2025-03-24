import qrcode
from PIL import Image

URL = "https://divno-inc.github.io/Website/"

#Sizing stuff self explantory
qr = qrcode.QRCode(
    version=3, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,  
    border=1, 
)


qr.add_URL(URL)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="White", back_color="#FFC83F").convert("RGB")

#This is where you put image in center of qrcode. NEEDS RO BE IN SMAE DIRECTORY
logo = Image.open("colorLogoCopy.png") 

#Screen szing
logo_size = (qr_img.size[0] // 4, qr_img.size[1] // 4)  
logo = logo.resize(logo_size)

#Logo position
position = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

qr_img.paste(logo, position, mask=logo)

#download im and opens it
qr_img.save("DivnoLogo.png")
qr_img.show()