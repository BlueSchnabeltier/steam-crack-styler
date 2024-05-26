from json import dump
from bs4 import BeautifulSoup
from os import listdir, path, makedirs
from urllib.request import urlretrieve
from vdf import load, binary_load, binary_dump

steam_path = input("Steam Path: ")

def rungameid_to_appid(rungameid: int):
    return round(rungameid * 2.32830643653e-10)

profile_ids = []
userdata_path = path.join(steam_path, "userdata")

for index, profile_id in enumerate(listdir(userdata_path)):
    localconfig_path = path.join(userdata_path, profile_id, "config\\localconfig.vdf")
    username = load(open(localconfig_path))["UserLocalConfigStore"]["friends"]["PersonaName"]

    print(f"[{index}] {username} ({profile_id})")
    profile_ids.append(profile_id)

while True:
    input_index = input("> ")

    try:
        input_index = int(input_index)
        if input_index > (len(profile_ids) - 1):
            print("Invalid input, try again!")
        else:
            profile_path = path.join(userdata_path, profile_ids[input_index])
            break

    except ValueError:
        print("Invalid input, try again!")

input("DISCLAIMER: To select a game, it must be launched at least once. If you haven't already done so, please run the game now. Note: If a game has been added and removed from your library, it may appear twice. To ensure the correct game is selected, create a desktop shortcut, right-click it, and check the rungameid in the properties.\n\nPress ENTER to continue...")

screenshots_vdf_path = path.join(profile_path, "760\\screenshots.vdf")
games_dict = load(open(screenshots_vdf_path))["screenshots"]["shortcutnames"]
games_list = [(name, int(id)) for id, name in games_dict.items()]
games_list_converted_ids = [(name, rungameid_to_appid(int(id))) for id, name in games_dict.items()]

for index, game in enumerate(games_list):
    print(f"[{index}] {game[0]} ({game[1]})")

while True:
    input_index = input("> ")

    try:
        input_index = int(input_index)
        if input_index > (len(games_list) - 1):
            print("Invalid input, try again!")
        else:
            game = games_list_converted_ids[input_index]
            break

    except ValueError:
        print("Invalid input, try again!")

shortcuts_vdf_path = path.join(profile_path, "config\\shortcuts.vdf")
shortcuts_list = list(binary_load(open(shortcuts_vdf_path, "rb"))["shortcuts"].values())

for index, shortcut in enumerate(shortcuts_list):
    if shortcut["AppName"] == game[0]:
        break

steamdb_html_path = input("Path to the steamdb.info HTML file: ")
steamdb_html = BeautifulSoup(open(steamdb_html_path, encoding="utf-8"), "html.parser")
name = steamdb_html.select("#main > div > div.header-wrapper > div > div.pagehead > div.d-flex.flex-grow > h1")[0].text
appid = steamdb_html.select("#main > div > div.header-wrapper > div > div.row.app-row > div.span8 > table > tbody > tr:nth-child(1) > td:nth-child(2)")[0].text
clienticon = steamdb_html.find("td", string="clienticon").find_next_sibling("td").find("a")["href"]
clienttga = steamdb_html.find("td", string="clienttga").find_next_sibling("td").find("a")["href"]
library_capsule = steamdb_html.find("td", string="library_capsule").find_next_sibling("td").find("a")["href"]
library_hero = steamdb_html.find("td", string="library_hero").find_next_sibling("td").find("a")["href"]
library_logo = steamdb_html.find("td", string="library_logo").find_next_sibling("td").find("a")["href"]
pinned_position = steamdb_html.find("td", string="logo_position/pinned_position").find_next_sibling("td").text
width_pct = steamdb_html.find("td", string="logo_position/width_pct").find_next_sibling("td").text
height_pct = steamdb_html.find("td", string="logo_position/height_pct").find_next_sibling("td").text
grid_dir_path = path.join(profile_path, "config\\grid")
grid_position_data = {
    "nVersion": 1,
    "logoPosition": {
        "pinnedPosition": pinned_position,
        "nWidthPct": float(width_pct),
        "nHeightPct": float(height_pct)
    }
}
icons_dir = path.join(grid_dir_path, "icons")
clienticon_path = path.join(icons_dir, f"{game[1]}.ico")
clienttga_path = path.join(icons_dir, f"{game[1]}.tga")
shortcut["AppName"] = name
shortcut["icon"] = clienttga_path
shortcuts_list[index] = shortcut

makedirs(icons_dir, exist_ok=True)
urlretrieve(library_capsule, path.join(grid_dir_path, f"{game[1]}p.{library_capsule[library_capsule.rfind('.')+1:].split('?')[0]}"))
urlretrieve(library_hero, path.join(grid_dir_path, f"{game[1]}_hero.{library_hero[library_hero.rfind('.')+1:].split('?')[0]}"))
urlretrieve(library_logo, path.join(grid_dir_path, f"{game[1]}_logo.{library_logo[library_logo.rfind('.')+1:].split('?')[0]}"))
urlretrieve(clienticon, clienticon_path)
urlretrieve(clienttga, clienttga_path)
dump(grid_position_data, open(path.join(grid_dir_path, f"{game[1]}.json"), "w+"))

shortcuts_dict = {}

for index, shortcut in enumerate(shortcuts_list):
    shortcuts_dict[str(index)] = shortcut

binary_dump({"shortcuts": shortcuts_dict}, open(shortcuts_vdf_path, "wb"))
print("Your game has been styled successfully! Please restart Steam to see the changes.")
