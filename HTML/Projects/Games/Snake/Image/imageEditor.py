# change the size of the image based on percentage
# and save it as a new file with selected name

from PIL import Image


image = Image.open("Snake.png")

def resize_image(image, percentage):
    width, height = image.size
    new_width = int(width * percentage / 100)
    new_height = int(height * percentage / 100)
    new_image = image.resize((new_width, new_height))
    return new_image


resize_image(image, 90).save("Snake.png")





