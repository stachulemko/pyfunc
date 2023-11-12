
image_path = "C:\\tmp\\adrew_legit16.bmp"
with open(image_path, "rb") as image_file:
    image_binary = image_file.read()

for byte in image_binary:
    print(f"{byte:02X}", end=" ")
