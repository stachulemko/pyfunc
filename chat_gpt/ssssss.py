from PIL import Image


def encrypt_images(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    if image2.size[0] > image1.size[0] or image2.size[1] > image1.size[1]:
        raise ValueError(
            "The second image must be smaller or equal in size to the first image")

    encrypted_image = image1.copy()

    for x in range(image2.size[0]):
        for y in range(image2.size[1]):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            encrypted_pixel = (pixel1[0] & 0xF0 | (pixel2[0] >> 4),
                               pixel1[1],
                               pixel1[2])
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save(output_path)


image1 = "C:\\tmp\\lambo.bmp"
image2 = "C:\\tmp\\lambo2.bmp"
output_image = "C:\\tmp\\salam.bmp"

encrypt_images(image1, image2, output_image)
