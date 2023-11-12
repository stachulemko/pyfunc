def rysunek_do_szyfrowany():
    image_path = "C:\\tmp\\lambo2.bmp"
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
    bitowa_reprezentacja1 = [f"{byte:02X}" for byte in image_binary]
    return bitowa_reprezentacja1


def rysunek_szyfrowany(x):
    image_path = "C:\\tmp\\lambo.bmp"
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
    bitowa_reprezentacja0 = [f"{byte:02X}" for byte in image_binary]
    licznik = 0
    licznik2 = 0
    for i in range(84, len(bitowa_reprezentacja0)):
        licznik += 1
        if licznik == 24:
            bitowa_reprezentacja0[i] = x[licznik2]
            licznik = 0
            licznik2 += 1

    with open("C:\\tmp\\zaszyfrowany_obrazek.bmp", "wb") as output_file:
        output_file.write(bytes.fromhex(''.join(bitowa_reprezentacja0)))

    with open("C:\\tmp\\gowno_psa.txt", "w") as txt_file:
        # Zapisuje bitową reprezentację jako tekst
        txt_file.write(' '.join(bitowa_reprezentacja0))


x = rysunek_do_szyfrowany()
rysunek_szyfrowany(x)
