def modifyBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def get_last_bit(bajt):
    return bajt & 1


def get_bits_from_byte(byte):
    bits = []
    for i in range(7, -1, -1):
        bit = (byte >> i) & 1
        bits.append(bit)
    return bits


def second_picture(image_path):
    with open(image_path, "rb") as f:
        bmp_data = bytearray(f.read())
        bity_dziecko = []
        for byte in bmp_data:
            bity_dziecko.extend(get_bits_from_byte(byte))
        return bity_dziecko


def manipulate_bmp(input_file, secret_file, output_file):
    bitydziecko = second_picture(secret_file)
    dlugoscbitow = len(bitydziecko)
    print(F'secret img bits:{dlugoscbitow}')
    with open(input_file, "rb") as f:
        bmp_data = bytearray(f.read())
        size = len(bmp_data)
        print(F'base img bits:{size}')
        offset = 100
        licznik = 0
        while offset < size:
            if licznik >= dlugoscbitow:
                break

            bmp_data[offset] = modifyBit(
                bmp_data[offset], 0, bitydziecko[licznik])
            offset += 1
            licznik += 1

    with open(output_file, "wb") as f:
        f.write(bmp_data)

    return dlugoscbitow


base_image = "C:\\tmp\\lambo.bmp"
#secret_image = "C:\\tmp\\moon256.bmp"
secret_image = "C:\\tmp\\nissan.bmp"
output_bmp = "C:\\tmp\\secret_lambo.bmp"
encrypted_secret_image = "C:\\tmp\\encrypted_moon256.bmp"


def odszyfrowywanie(image_path, output_encrypted_path, secret_image_size):
    secret_bajt = ""
    secret_list = []
    with open(image_path, "rb") as f:
        rozmiar = (secret_image_size)+1
        bmp_data = bytearray(f.read())
        for i in range(100, rozmiar+100):
            secret_bajt += str(get_last_bit(bmp_data[i]))
            if len(secret_bajt) == 8:
                secret_list.append(int(secret_bajt, 2))
                secret_bajt = ""
        with open(output_encrypted_path, "wb") as f:
            f.write(bytearray(secret_list))


size = manipulate_bmp(base_image, secret_image, output_bmp)
print(size)
odszyfrowywanie(output_bmp, encrypted_secret_image, size)
