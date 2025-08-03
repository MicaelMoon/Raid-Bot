import mss
import time
from PIL import Image, ImageChops
import pyautogui
from path_utils import get_image_path
from enteties.dungeon import Dungeon

class MenuNavigationService:
    dungoens_page_2 = [
        "ice",
        "spider",
        "dragon",
        "fire",
        "sand",
        "phantom"
    ]

    dungeons_cordinates = {
        Dungeon.IRON_TWINS_FORTRESS.value: (2525, 445),
        Dungeon.ICE_GOLEMS_PEEK.value: (1980, 280),
        Dungeon.SPIDERS_DEN.value: (2040, 500),
        Dungeon.DRAGONS_LAYER.value: (2500, 300)
    }

    rematches = 1

    def click(self, x:int, y:int):
        pyautogui.click(x, y)
        time.sleep(0.8)

    def screens_match(self, image_file:str, region) -> bool:
        image = Image.open(get_image_path(image_file))

        with mss.mss() as sct:
            raw_image = sct.grab(region)
            new_image = Image.frombytes("RGB", raw_image.size, raw_image.rgb)
            new_image.save("New-image.png")

            diff = ImageChops.difference(image, new_image)

            if not diff.getbbox(): # A match
                return True

        return False

    def to_main_menu(self) -> bool:
        battle_button = Image.open(f"{get_image_path("Battle-Button.png")}")

        region = {'left': 3556, 'top': 957, 'width': 120, 'height': 28}
        
        if(self.screens_match("Battle-Button.png", region)):
            print("In main menu")
            return True

        print("Not in main menu")
        self.clear_ads()

        self.check_nesting()
        return False
    
    def clear_ads(self):
        print("Checking for ads")
        close_ad_button_region = {'left': 3682, 'top': 58, 'width': 36, 'height': 35}

        attempts = 0

        while True:
            time.sleep(3)

            if (self.screens_match("Close-Ad-Button.png", close_ad_button_region)):
                print("Closing ad")
                self.click(3678, 54)
                pyautogui.moveTo(3800,80)
            else:
                print("No ads detected")
                return

            
        attempts = attempts + 1

        if attempts >= 10:
            raise RuntimeError("Close add loop exceeded safe iteration limit of 10")


    def check_nesting(self):
        print("Not implimented")

    def select_dungeon(self, dungeon:str):
        if(dungeon in self.dungoens_page_2):
            print("Scrolling page")
            self.scroll_page(3800, 1932, True) # Scroll Dungeons page

        coords = self.dungeons_cordinates.get(dungeon)
        self.click(coords[0], coords[1]) # Click Dungeon
        self.click(3600, 1000) # Click Stage

        self.start_battle()


    def scroll_page(self, start:int, finish:int, horizontal:bool):
        if(horizontal):
            print("horizontal scroll")
            pyautogui.moveTo(start,800)

            pyautogui.mouseDown()
            pyautogui.moveTo(finish,800, 1)
            pyautogui.mouseUp()
    
    def start_battle(self):
        replay_button_region = {'left': 2840, 'top': 902, 'width': 297, 'height': 53}

        for i in range(self.rematches):
            if(i == 0):
                self.click(3600, 944)
                pyautogui.moveTo(1996,40)
                time.sleep(2)
            else:
                while not self.screens_match("Replay-Button.png", replay_button_region):
                    time.sleep(5)
                    print("No Replay Button found")

                self.click(3000, 960)
                pyautogui.moveTo(1996,40)
            print(f"Starting game: {i+1}/{self.rematches}")
        print("Runs are finishing")


        return