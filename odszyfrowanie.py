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

    with open(output_file, "wb") as f:
        f.write(bmp_data)
input_bmp = "C:\\tmp\\output_5.bmp"
output_bmp = "C:\\tmp\\output_5.bmp"
