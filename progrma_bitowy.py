from PIL import Image


def bits_to_image(bits, output_path, width, height):
    image = Image.new("RGBA", (width, height))
    pixel_index = 0

    for y in range(height):
        for x in range(width):
            red = int(bits[pixel_index], 2)
            green = int(bits[pixel_index + 1], 2)
            blue = int(bits[pixel_index + 2], 2)
            alpha = int(bits[pixel_index + 3], 2)

            pixel = (red, green, blue, alpha)
            image.putpixel((x, y), pixel)
            pixel_index += 4

    image.save(output_path)
    print("Zapisano obraz:", output_path)


def read_bits_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    input_bits = read_bits_from_file("kupa.txt")
    # Usunięcie znaków inne niż '0' i '1'
    input_bits = ''.join(filter(lambda x: x in ['0', '1'], input_bits))
    output_path = 'C:\\tmp\\lambo10.bmp'
    width = 1980  # Długość obrazu
    height = 1320  # Wysokość obrazu

    bits_to_image(input_bits, output_path, width, height)


if __name__ == "__main__":
    main()
