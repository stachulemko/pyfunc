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


def encode_bmp(input_bmp, secret_bmp, output_bmp):
    secret_bits = second_picture(secret_bmp)
    secret_length = len(secret_bits)

    with open(input_bmp, "rb") as f:
        bmp_data = bytearray(f.read())
        offset = 100
        bit_index = 0

        for i in range(offset, len(bmp_data)):
            if bit_index >= secret_length:
                break

            bmp_data[i] = modifyBit(bmp_data[i], 0, secret_bits[bit_index])
            bit_index += 1

    with open(output_bmp, "wb") as f:
        f.write(bmp_data)

    return secret_length


def decode_bmp(input_bmp, output_secret, secret_length):
    secret_bits = []

    with open(input_bmp, "rb") as f:
        bmp_data = bytearray(f.read())
        for i in range(100, min(100 + secret_length, len(bmp_data))):
            secret_bits.append(get_last_bit(bmp_data[i]))

    secret_bytes = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)]
    secret_bytes = [int("".join(map(str, byte)), 2) for byte in secret_bytes]

    with open(output_secret, "wb") as f:
        f.write(bytearray(secret_bytes))


base_image = "C:\\tmp\\lambo.bmp"
secret_image = "C:\\tmp\\moon.bmp"
output_bmp = "C:\\tmp\\output_5.bmp"

size = encode_bmp(base_image, secret_image, output_bmp)
decode_bmp(output_bmp, "C:\\tmp\\decoded_secret.bmp", size)
