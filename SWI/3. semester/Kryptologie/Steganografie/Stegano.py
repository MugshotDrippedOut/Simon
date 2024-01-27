from stegano import lsb
from PIL import Image
from unidecode import unidecode
import numpy as np
import os



def hide_text_in_image(image, text, output_file_name="encoded_image.png"):
    if text == "":
        raise Exception("No text to hide.")
    text = unidecode(text)
    secret = lsb.hide(image, text)
    if not os.path.exists("Images"):
        os.makedirs("Images")
    secret.save(os.path.join("Images", output_file_name), "PNG")

def get_text_from_image(image):
    text = lsb.reveal(image)
    return text


def generate_image(width, height, unicolor=False, color=[255, 0, 0], output_file_name="random_image.png"):
    if unicolor:
        image = np.zeros((width, height, 3), dtype=np.uint8)
        image[:] = color
    else:
        image = np.random.randint(0, 255, (width, height, 3), dtype=np.uint8)
    img = Image.fromarray(image, 'RGB')
    if not os.path.exists("Images"):
        os.makedirs("Images")
    img.save(os.path.join("Images", output_file_name))
    return os.path.join("Images", output_file_name)


def get_image_info(image):
    img = Image.open(image)
    width, height = img.size
    number_of_pixels = width * height
    color = img.mode
    size = os.path.getsize(image)
    path = os.path.join("Images", image)
    return [width, height, number_of_pixels, color, size, path]




if __name__ == "__main__":
    generate_image(256, 256, False, [255, 255, 0], "a.png")
    hide_text_in_image("Images/a.png", "ahoj", "b.png")
    print(get_text_from_image("Images/b.png"))