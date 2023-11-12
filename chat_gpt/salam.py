from PIL import Image


def image_to_bits(image_path):
    image = Image.open(image_path)
    width, height = image.size

    bits = ""
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            rgba_bits = [format(component, '08b') for component in pixel]
            bits += ''.join(rgba_bits)

    return bits


def bits_to_image(bits, width, height):
    new_image = Image.new("RGBA", (width, height))
    pixel_list = [bits[i:i+32] for i in range(0, len(bits), 32)]

    for y in range(height):
        for x in range(width):
            index = y * width + x
            if index < len(pixel_list):
                rgba_bits = pixel_list[index]
                rgba = tuple(int(rgba_bits[i:i+8], 2) for i in range(0, 32, 8))
                new_image.putpixel((x, y), rgba)

    return new_image


def szyfrowanie(bity_rysunku_w_szyfrowanym, bity_rysunku_szyfrowanego):
    bity_wynikowe = list(bity_rysunku_w_szyfrowanym)
    licznik2 = 0
    for i in range(84, len(bity_wynikowe)):
        bity_wynikowe[i] = bity_rysunku_szyfrowanego[licznik2]
        licznik2 += 1
        if licznik2 == len(bity_rysunku_szyfrowanego):
            break
    return ''.join(bity_wynikowe)


bity_rysunku_w_szyfrowanym = image_to_bits("C:\\tmp\\lambo.bmp")
bity_rysunku_szyfrowanego = image_to_bits("C:\\tmp\\lambo2.bmp")

x = szyfrowanie(bity_rysunku_w_szyfrowanym, bity_rysunku_szyfrowanego)

width = 1980  # Wprowadź szerokość obrazu
height = 1320  # Wprowadź wysokość obrazu

zmieniony_obraz = bits_to_image(x, width, height)
zmieniony_obraz.save("C:\\tmp\\zmieniony_obraz.bmp")

print("Zmieniony obraz został zapisany.")
