from PIL import Image


def rysunek_do_szyfrowania():
    return image_to_bits("C:\\tmp\\lambo.bmp")


def rysunek_szyfrowany():
    return image_to_bits("C:\\tmp\\lambo2.bmp")


def image_to_bits(image_path):
    image = Image.open(image_path)
    width, height = image.size

    bits = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            rgba_bits = [format(component, '08b') for component in pixel]
            bits.extend(rgba_bits)

    return bits


def szyfrowanie(bity_rysunku_w_szyfrowanym, bity_rysunku_szyfrowanego):
    licznik1 = 0
    licznik2 = 0
    nowe_bity_szyfrowane = []

    for i in bity_rysunku_w_szyfrowanym:
        licznik1 += 1
        if licznik1 == 8:  # Poprawiona warunek
            licznik1 = 0    # Zmiana = na =
            nowe_bity_szyfrowane.append(bity_rysunku_szyfrowanego[licznik2])
            licznik2 += 1
        else:
            nowe_bity_szyfrowane.append(i)

    print(nowe_bity_szyfrowane)
    return nowe_bity_szyfrowane


def main():
    bity_rysunku_w_szyfrowanym = rysunek_do_szyfrowania()
    bity_rysunku_szyfrowanego = rysunek_szyfrowany()

    nowe_bity_szyfrowane = szyfrowanie(
        bity_rysunku_w_szyfrowanym, bity_rysunku_szyfrowanego)


if __name__ == "__main__":
    main()
