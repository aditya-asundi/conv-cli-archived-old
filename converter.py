from PIL import Image

def convert_image(input_file, output_file):
    img = Image.open(input_file)
    img.save(output_file)