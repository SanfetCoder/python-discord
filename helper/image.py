from PIL import Image

def compress_image(input_path, output_path, quality = 85):
  with Image.open(input_path) as img:
    img.save(output_path, 'JPEG', quality=quality)    
