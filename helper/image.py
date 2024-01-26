from PIL import Image

def compress_image(input_path, output_path, quality = 85):
  with Image.open(input_path) as img:
    img.save(output_path, 'JPEG', quality=quality)    

# Example usage
input_image = './downloaded_image.png'
output_image = './compressed_image.jpeg'

compress_image(input_image, output_image)
print(f'Image compressed: {output_image}')