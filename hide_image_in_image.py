from PIL import Image
def rysunek_do_szyfrowany ():
    image_path = "C:\\tmp\\adrew_legit16.bmp"
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
    bitowa_reprezetacja1 = [f"{byte:02X}" for byte in image_binary]
    return bitowa_reprezetacja1

def rysunek_szyfrowany (x):
    image_path = "C:\\tmp\\adrew_legit16.bmp"
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
    bitowa_reprezentacja0 = [f"{byte:02X}" for byte in image_binary]
    licznik=0
    licznik2=0
    for i in bitowa_reprezentacja0[84:]:
        licznik+=1
        if licznik == 24:
            bitowa_reprezentacja0[bitowa_reprezentacja0.index(i)]==x[licznik2]
            licznik==0
            

x=rysunek_do_szyfrowany()
rysunek_szyfrowany(x)     