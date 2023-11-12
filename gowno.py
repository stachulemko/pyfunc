from PIL import Image


def image_to_bits(image_path):
    image = Image.open(image_path)
    width, height = image.size

    # Konwertuj każdy piksel na ciąg bitów (RGBA)
    bits = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            rgba_bits = [format(component, '08b') for component in pixel]
            bits.extend(rgba_bits)

    return ''.join(bits)

     
print(image_to_bits("C:\\tmp\\lambo.bmp"))

