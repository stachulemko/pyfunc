def modifyBit(n,  p,  b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


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

            # Modify the bits as needed (e.g., flipping a specific bit at the given position)
    # for i in range(54, len(bmp_data)):
    #    # XOR with 1 at the specific bit position
    #    bmp_data[i] = bmp_data[i] ^ (1 << bit_position)
    #bmp_data[bit_position+54] = 1
    with open(output_file, "wb") as f:
        f.write(bmp_data)


input_bmp = "C:\\tmp\\lambo.bmp"
output_bmp = "C:\\tmp\\output.bmp"


manipulate_bmp(input_bmp, output_bmp)
