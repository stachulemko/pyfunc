from PIL import Image


def hide_image(source_image_path, secret_image_path, output_image_path):
    source_image = Image.open(source_image_path)
    secret_image = Image.open(secret_image_path)

    width, height = source_image.size
    secret_image = secret_image.resize((width, height))

    output_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            source_pixel = source_image.getpixel((x, y))
            secret_pixel = secret_image.getpixel((x, y))
            new_pixel = (
                (source_pixel[0] & 0xFE) | (secret_pixel[0] >> 7),
                (source_pixel[1] & 0xFE) | ((secret_pixel[1] >> 7) & 0x01),
                (source_pixel[2] & 0xFE) | ((secret_pixel[2] >> 7) & 0x01)
            )
            output_image.putpixel((x, y), new_pixel)

    output_image.save(output_image_path)


def reveal_hidden_image(output_image_path, revealed_image_path):
    output_image = Image.open(output_image_path)

    width, height = output_image.size
    revealed_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            output_pixel = output_image.getpixel((x, y))
            revealed_pixel = (
                (output_pixel[0] & 0x01) << 7,
                (output_pixel[1] & 0x01) << 7,
                (output_pixel[2] & 0x01) << 7
            )
            revealed_image.putpixel((x, y), revealed_pixel)

    revealed_image.save(revealed_image_path)


source_image_path = "C:\\tmp\\lambo.bmp"
secret_image_path = "C:\\tmp\\lambo2.bmp"
output_image_path = "C:\\tmp\\zaszyfrowany.bmp"
combined_image_path = "C:\\tmp\\polaczony.bmp"
revealed_image_path = "C:\\tmp\\odszyfrowany.bmp"

hide_image(source_image_path, secret_image_path, output_image_path)
reveal_hidden_image(output_image_path, revealed_image_path)

combined_image = Image.open(output_image_path)
combined_image.paste(Image.open(secret_image_path), (0, 0))
combined_image.save(combined_image_path)
