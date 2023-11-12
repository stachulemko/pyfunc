def encrypt_images(image1_path, image2_path, output_path):
    with open(image1_path, "rb") as f1, open(image2_path, "rb") as f2:
        image1_data = bytearray(f1.read())
        image2_data = bytearray(f2.read())

    if len(image2_data) > len(image1_data):
        raise ValueError(
            "The second image must be smaller or equal in size to the first image")

    encrypted_data = bytearray(image1_data)

    for i in range(len(image2_data)):
        encrypted_data[i] = (image1_data[i] & 0xF0) | (image2_data[i] >> 4)

    with open(output_path, "wb") as f_out:
        f_out.write(encrypted_data)


image1 = "C:\\tmp\\lambo.bmp"
image2 = "C:\\tmp\\lambo2.bmp"
output_image = "C:\\tmp\\encrypted_output.bmp"

encrypt_images(image1, image2, output_image)
