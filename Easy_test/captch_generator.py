from captcha.image import ImageCaptcha
from PIL import Image

image = ImageCaptcha (width = 300, height = 100)
captcha_text = input ("กำหนดข้อความ :")
data = image.generate(captcha_text)
image.write( captcha_text , 'CAPTCHA1.png')
Image.open('CAPTCHA1.png')
