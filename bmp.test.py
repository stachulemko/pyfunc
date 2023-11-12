def modifyBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def get_bits_from_byte(byte):
    bits = []
    for i in range(7, -1, -1):
        bit = (byte >> i) & 1
        bits.append(bit)
    return bits


def second_picture():
    kupa = "C:\\tmp\\moon.bmp"
    with open(kupa, "rb") as f:
        bmp_data = bytearray(f.read())
        bity_dziecko = []
        for byte in bmp_data:
            bity_dziecko.extend(get_bits_from_byte(byte))
        return bity_dziecko


def manipulate_bmp(input_file, output_file):
    bitydziecko = second_picture()  
    dlugoscbitow = len(bitydziecko)

    with open(input_file, "rb") as f:
        bmp_data = bytearray(f.read())
        size = len(bmp_data)
        print(size)
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


input_bmp = "C:\\tmp\\lambo.bmp"
output_bmp = "C:\\tmp\\output_5.bmp"

manipulate_bmp(input_bmp, output_bmp)
