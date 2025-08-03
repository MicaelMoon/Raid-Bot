import argparse
from Services.menu_navigation_service import MenuNavigationService
from PIL import Image, ImageChops
from enteties.dungeon import Dungeon
from enteties.game_mode import GameMode
from enteties.click_coordinates import ClickCoordinate
from enteties.screenshot_region import ScreenshotRegion

menu_service = MenuNavigationService()

parser = argparse.ArgumentParser()
parser.add_argument("-a", type=str, required=True, help="enter main action")
parser.add_argument("-gm", type=str, required=False, help="enter a game mode")
parser.add_argument("-d", type=str, required=False, help="enter a dungeon")
parser.add_argument("-r", type=int, required=False, help="enter the number of rematches")
args = parser.parse_args()

action = args.a
game_mode = args.gm
dungeon_args = args.d
menu_service.rematches = None
if (args.r != None):
    menu_service.rematches = args.r
else:
    menu_service.rematches = 1

daily_quests = [
    "Summon.png",
    "Level.png",
    "Artifact.png",
    "Battle.png",
    "Boss.png"
]

def start():
    match action:
        case "daily":
            print("Starting daily quests")
            daily_quest_search()
        case "play":
            print("Starting play workflow")
            play()

def daily_quest_search():
    menu_service.to_main_menu()
    menu_service.click(*ClickCoordinate.QUESTS_BUTTON.value)
    menu_service.click(*ClickCoordinate.DAILY_QUESTS_TAB_BUTTON.value)
    
    for i in range(len(daily_quests)):
        print(f"Daily quest path = {daily_quests[i]}")
        daily = menu_service.screens_match(f"Daily-Missions\\{daily_quests[i]}", ScreenshotRegion.TOP_DAILY_QUEST.value)

        if(daily == True):
            menu_service.click(*ClickCoordinate.DAILY_QUEST_BUTTON.value)
            do_daily_quest(daily_quests[i])



def do_daily_quest(quest:str):
    match quest:
        case "Summon.png":
            menu_service.summon_champion("Mystery", 3, False)

        # Add additional quest function calls

def play():
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

daily_quest_order = [
    "Summon 3 champions",
    "Increase Chamption's Level in the Tavern 3 times",
    "Make 4 Artifact/Accessory upgrade attempts",
    "Win Campaign Battles 7 times"
]

start()