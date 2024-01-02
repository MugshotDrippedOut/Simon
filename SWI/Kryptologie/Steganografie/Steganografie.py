from PIL import Image
def generate_data(data):
    new_data = []

    for i in data:
        new_data.append(format(ord(i), '08b'))
    return new_data


def modify_pixel(pixel, data):
    data_index = 0
    pixel_list = []

    for i in pixel:
        if data_index < len(data):
            pixel_list.append(int(bin(i)[:-1] + data[data_index], 2))
            data_index += 1
        else:
            pixel_list.append(i)
    return tuple(pixel_list)


def modify_pixels(pixels, data):
    data_index = 0

    for pixel in pixels:
        pixels[data_index] = modify_pixel(pixel, data[data_index])
        data_index += 1
        if data_index >= len(data):
            break
    return pixels


def modify_image(image, data):
    width, height = image.size
    pixels = list(image.getdata())
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(modify_pixels(pixels, data))
    return new_image


def encode(image, data):
    new_image = modify_image(image, generate_data(data))
    new_image.save("encoded_image.png", "PNG")
    
    
def decode(image):
    pixels = list(image.getdata())
    data = ""
    for pixel in pixels:
        data += bin(pixel[-1])[-1]
    data = [data[i:i+8] for i in range(0, len(data), 8)]
    message = ""
    for i in data:
        message += chr(int(i, 2))
        if message[-5:] == "#####":
            break
    return message[:-5]




def print_progress(myInput):
    print(generate_data(myInput))

if __name__ == "__main__":
    print ("Steganografie.py")
    myInput = "Ahoj"
    #encode(Image.open("256x256-00ffaaff.png"), myInput)
    decoded_image = Image.open("encoded_image.png")
    print(decode(decoded_image))
    print_progress(myInput)