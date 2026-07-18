from PIL import Image

def convert_image(input_file, output_file):
    img = Image.open(input_file)
    img.save(output_file)

    # TODO: Figure out how to handle exceptions such as
    #       corrupted image files, non-existent paths,
    #       and other edge cases. Even stuff like other
    #       types of files disguised as image files.