from PIL import Image
import numpy as np


def rysunek_do_szyfrowania():
    ścieżka_obrazka = "C:\\tmp\\lambo2.bmp"
    with open(ścieżka_obrazka, "rb") as plik_obrazka:
        binarna_reprezentacja_obrazka = plik_obrazka.read()
    bitowa_reprezentacja1 = [
        f"{bajt:02X}" for bajt in binarna_reprezentacja_obrazka]
    return bitowa_reprezentacja1


def rysunek_szyfrowany(x):
    ścieżka_obrazka = "C:\\tmp\\lambo.bmp"
    with open(ścieżka_obrazka, "rb") as plik_obrazka:
        binarna_reprezentacja_obrazka = plik_obrazka.read()
    bitowa_reprezentacja0 = [
        f"{bajt:02X}" for bajt in binarna_reprezentacja_obrazka]
    lista_gotowa = []
    licznik = 0
    licznik2 = 0
    for i in bitowa_reprezentacja0[84:]:
        licznik += 1
        if licznik == 24:
            bitowa_reprezentacja0[bitowa_reprezentacja0.index(i)] = x[licznik2]
            licznik = 0
            licznik2 += 1
        lista_gotowa.append(i)

    nowy_obrazek = np.array(bytes.fromhex(
        ''.join(bitowa_reprezentacja0)), dtype=np.uint8)
    nowy_obrazek = nowy_obrazek.reshape((240, 320, 3))

    # Zapisanie obrazka do pliku
    obrazek_wyjściowy = Image.fromarray(nowy_obrazek)
    ścieżka_obrazka_wyjściowego = "C:\\tmp\\zaszyfrowany_obrazek5.bmp"
    obrazek_wyjściowy.save(ścieżka_obrazka_wyjściowego)

    # Wyświetlenie obrazka
    obrazek_wyjściowy.show()


x = rysunek_do_szyfrowania()
rysunek_szyfrowany(x)
