from rembg import remove
from PIL import Image

input_path = 'C:\\Users\\suchin\\Desktop\\SHARP\\ดิบ\\Photo\\images.png'
output_path = 'C:\\Users\\suchin\\Desktop\\SHARP\\ดิบ\\Photo\\output.png'
input = Image.open( input_path )

output = remove( input )
output.save( output_path)