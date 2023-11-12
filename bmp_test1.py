image_file = open(path, "rb")
# Blindly skip the BMP header.
image_file.seek(54)
while True:
  r_string = image_file.read(1)
  g_string = image_file.read(1)
  b_string = image_file.read(1)
  if len(r_string) == 0:
    # This is expected to happen when we've read everything.
    break
   if len(g_string) == 0:
    break
   if len(b_string) == 0:
    break

image_file.close()
