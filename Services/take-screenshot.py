import mss
from PIL import Image

region = {'left': 2840, 'top': 902, 'width': 297, 'height': 53}

with mss.mss() as sct:
    img = sct.grab(region)
    img_pil = Image.frombytes("RGB", img.size, img.rgb)
    img_pil.save("Replay-Button.png")

    print("Saved successfully")