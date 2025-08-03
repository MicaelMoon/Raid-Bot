import mss
from PIL import Image

region = {'left': 2320, 'top': 330, 'width': 710, 'height': 150}

with mss.mss() as sct:
    img = sct.grab(region)
    img_pil = Image.frombytes("RGB", img.size, img.rgb)
    img_pil.save("Daily-Mission.png")

    print("Saved successfully")