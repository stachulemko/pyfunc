def rysunek_do_szyfrowany():
    image_path = "C:\\tmp\\lambo.bmp"
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
    bitowa_reprezetacja1 = [f"{byte:02X}" for byte in image_binary]
    return bitowa_reprezetacja1


def rysunek_szyfrowany(x):
    image_path = "C:\\tmp\\lambo2.bmp"
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
    bitowa_reprezentacja0 = [f"{byte:02X}" for byte in image_binary]
    licznik = 0
    licznik2 = 0
    for i in bitowa_reprezentacja0[84:]:
        licznik += 1
        if licznik == 24:
            bitowa_reprezentacja0[bitowa_reprezentacja0.index(i)] = x[licznik2]
            licznik = 0
            licznik2 += 1
    with open("C:\\tmp\\bebzon.bmp", "wb") as output_file:
        output_file.write(bytes.fromhex(''.join(bitowa_reprezentacja0)))


x = rysunek_do_szyfrowany()
rysunek_szyfrowany(x)
