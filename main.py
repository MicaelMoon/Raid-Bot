import argparse
from Services.menu_navigation_service import MenuNavigationService
from PIL import Image, ImageChops
from enteties.dungeon import Dungeon
from enteties.game_mode import GameMode
from enteties.click_coordinates import ClickCoordinate

menu_service = MenuNavigationService()

parser = argparse.ArgumentParser()
parser.add_argument("-gm", type=str, required=True, help="enter a game mode")
parser.add_argument("-d", type=str, required=True, help="enter a dungeon")
parser.add_argument("-r", type=int, required=True, help="enter the number of rematches")
args = parser.parse_args()

game_mode = args.gm
dungeon_args = args.d
menu_service.rematches = args.r

def start():

    menu_service.to_main_menu()
    menu_service.click(*ClickCoordinate.MAIN_MENU_BATTLE_BUTTON.value)

    match game_mode:
        case GameMode.DUNGEONS.value:
            menu_service.click(*ClickCoordinate.DUNGEON_BUTTON.value)

            if any(dungeon_args == dungeon.value for dungeon in Dungeon):
                print(f"Entering [{dungeon_args}]")
                menu_service.select_dungeon(dungeon_args)
            else:
                print("Invalid Dungeon")


start()
