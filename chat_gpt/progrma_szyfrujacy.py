from contextlib import nullcontext
from PIL import Image
import ctypes


def convert(s):

    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

    # return string
    return new


def rysunek_do_szyfrowania():
    return image_to_bits2("C:\\tmp\\lambo.bmp")

    # return rysunek_do_szyfrowania


def rysunek_szyfrowany():
    return image_to_bits2("C:\\tmp\\help.bmp")


def image_to_bits2(image_path):
    list = []
    with open(image_path, "rb") as f:
        binary_data = f.read()
        #list = [format(byte, '08b') for byte in binary_data]
        for byte in binary_data:
            pass
            txt_byte = format(byte, '08b')
            for i in range(8):
                pass
                list.append(txt_byte[i])
        #custom_text = "".join(format(byte, '08b') for byte in binary_data)
        #mutable = ctypes.create_string_buffer(custom_text)
        #list = [*string]
        return list


def szyfrowanie(bity_rysunku_w_szyfrowanym, bity_rysunku_szyfrowanego):
    licznik1 = 0
    licznik2 = 0
    size = len(bity_rysunku_szyfrowanego)
    # print(len(bity_rysunku_w_szyfrowanym))
    # print(type(bity_rysunku_w_szyfrowanym))
    # print(type(bity_rysunku_szyfrowanego))
    for i in bity_rysunku_w_szyfrowanym[54:]:
        # print(licznik1)
        licznik1 += 1
        if licznik1 % 8 == 0:
            # print(bity_rysunku_szyfrowanego[licznik2])
            if licznik2 < size:
                bity_rysunku_w_szyfrowanym[licznik1] = bity_rysunku_szyfrowanego[licznik2]
                licznik2 += 1
    # print(bity_rysunku_w_szyfrowanym)
    binary_bytes = []
    # print(licznik2)
    # print(licznik1)
    with open("C:\\tmp\\zaszyfrowany_obrazek_lambo.bmp", "wb") as f:
        for i in range(0, len(bity_rysunku_w_szyfrowanym), 8):
            # print(bity_rysunku_w_szyfrowanym[i:i+8])
            try:
                binary_byte = int(
                    convert(bity_rysunku_w_szyfrowanym[i:i+8]), 2)
                binary_bytes.append(binary_byte)
            except Exception as e:
                print("Error")
                print(bity_rysunku_w_szyfrowanym[i:i+8])

        # binary_bytes = bytes([int(bity_rysunku_w_szyfrowanym[i:i+8], 2)
        # for i in range(0, len(bity_rysunku_w_szyfrowanym), 8)])
        f.write(bytearray(binary_bytes))


def decrypt(image_path):
    text_bits = image_to_bits2(image_path)
    output_bits = ""
    for i in range(0, len(text_bits[54:]), 8):
        output_bits.join(i)

    return bity_rysunku_w_szyfrowanym


bity_rysunku_w_szyfrowanym = rysunek_do_szyfrowania()
# print(bity_rysunku_w_szyfrowanym)

bity_rysunku_szyfrowanego = rysunek_szyfrowany()
x = szyfrowanie(bity_rysunku_w_szyfrowanym, bity_rysunku_szyfrowanego)
# print(x)
