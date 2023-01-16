from consolemenu import *
from consolemenu.items import *


def menu(Gamer, Character, Location, Boss, Item):
    newGamer = {
        'login': "DkS4",
        'password': "qwerty123",
        'email': "darkside4@gmail.com",
    }
    newCharacter = {
        'name': "DarkSide4",
        'hit_points': "500",
        'lvl': "27",
        'gamer_id': "4"
    }
    newLocation = {
        'loc_name': "Stratholme",
        'population': "15000",
        'threat_level': "Hard",
        'character_id': "4",
        'boss_id': '4'
    }
    newBoss = {
        'boss_name': "Butcher",
        'damage': "150",
        'hit_points': "780",
        'lvl': "45",
        'experience': '1000'
    }

    newItem = {
        'item_name': "Staff of Homa",
        'rarity': "Legendary",
        'damage': "608",
        'character_id': "4",
        'boss_id': 'null'
    }
    mainMenu = ConsoleMenu("BD Game")
    menu_gamer = ConsoleMenu("Gamer")
    menu_character = ConsoleMenu("Character")
    menu_location = ConsoleMenu("Location")
    menu_boss = ConsoleMenu("Boss")
    menu_item = ConsoleMenu("Item")

    function_insert_Gamer = FunctionItem("Create gamer", Gamer.insert_gamer, [newGamer])
    function_insert_many_Gamer = FunctionItem("Create many random gamers", Gamer.insert_many_gamers, [])
    function_show_Gamers = FunctionItem("Show Gamers", Gamer.show_gamers, [])
    function_show_Gamer = FunctionItem("Show Gamer", Gamer.show_gamer, [])
    function_update_Gamer = FunctionItem("Update Gamer", Gamer.update_gamer, [newGamer])
    function_delete_Gamer = FunctionItem("Delete Gamer", Gamer.delete_gamer, [])
    menu_gamer.append_item(function_insert_Gamer)
    menu_gamer.append_item(function_insert_many_Gamer)
    menu_gamer.append_item(function_show_Gamer)
    menu_gamer.append_item(function_show_Gamers)
    menu_gamer.append_item(function_update_Gamer)
    menu_gamer.append_item(function_delete_Gamer)

    function_show_character = FunctionItem("Show Character", Character.show_character, [])
    function_show_characters = FunctionItem("Show Characters", Character.show_characters, [])
    function_insert_character = FunctionItem("Create Character", Character.insert_character, [newCharacter])
    function_insert_many_characters = FunctionItem("Create random Characters", Character.insert_many_characters, [])
    function_update_character = FunctionItem("Update Character", Character.update_character, [newCharacter])
    function_delete_character = FunctionItem("Delete Character", Character.delete_character, [])
    function_findHP_character = FunctionItem("Find Character\Boss by hit points", Character.character_findHP, [])
    menu_character.append_item(function_show_character)
    menu_character.append_item(function_show_characters)
    menu_character.append_item(function_insert_character)
    menu_character.append_item(function_insert_many_characters)
    menu_character.append_item(function_update_character)
    menu_character.append_item(function_delete_character)
    menu_character.append_item(function_findHP_character)

    function_show_locations = FunctionItem("Show Locations", Location.show_locations, [])
    function_show_location = FunctionItem("Show Location", Location.show_location, [])
    function_insert_location = FunctionItem("Create Location", Location.insert_location, [newLocation])
    function_insert_many_location = FunctionItem("Create random Locations", Location.insert_many_locations, [])
    function_update_location = FunctionItem("Update Location", Location.update_location, [newLocation])
    function_delete_location = FunctionItem("Delete Location", Location.delete_location, [])
    function_findpop_location = FunctionItem("Find Location by id", Location.show_location_by_Name, [])
    menu_location.append_item(function_show_locations)
    menu_location.append_item(function_show_location)
    menu_location.append_item(function_insert_location)
    menu_location.append_item(function_insert_many_location)
    menu_location.append_item(function_update_location)
    menu_location.append_item(function_delete_location)
    menu_location.append_item(function_findpop_location)

    function_show_bosses = FunctionItem("Show bosses", Boss.show_bosses, [])
    function_show_boss = FunctionItem("Show boss", Boss.show_boss, [])
    function_insert_boss = FunctionItem("Create boss", Boss.insert_boss,
                                        [newBoss])
    function_random_boss = FunctionItem("Create random bosses",
                                        Boss.insert_random_boss, [])
    function_update_boss = FunctionItem("Update boss", Boss.update_boss,
                                        [newBoss])
    function_delete_boss = FunctionItem("Delete boss", Boss.delete_boss, [])
    menu_boss.append_item(function_show_bosses)
    menu_boss.append_item(function_show_boss)
    menu_boss.append_item(function_insert_boss)
    menu_boss.append_item(function_random_boss)
    menu_boss.append_item(function_update_boss)
    menu_boss.append_item(function_delete_boss)

    function_show_items = FunctionItem("Show items", Item.show_items,
                                       [])
    function_show_item = FunctionItem("Show item", Item.show_item, [])
    function_insert_item = FunctionItem("Create item", Item.insert_item,
                                        [newItem])
    function_random_item = FunctionItem("Create random items",
                                        Item.insert_random_item, [])
    function_update_item = FunctionItem("Update item", Item.update_item,
                                        [newItem])
    function_delete_item = FunctionItem("Delete item", Item.delete_item,
                                        [])

    menu_item.append_item(function_show_items)
    menu_item.append_item(function_show_item)
    menu_item.append_item(function_insert_item)
    menu_item.append_item(function_random_item)
    menu_item.append_item(function_update_item)
    menu_item.append_item(function_delete_item)

    submenu_gamer = SubmenuItem("Gamer", menu_gamer, mainMenu)
    submenu_character = SubmenuItem("Character", menu_character, mainMenu)
    submenu_location = SubmenuItem("Location", menu_location, mainMenu)
    submenu_boss = SubmenuItem("Boss", menu_boss, mainMenu)
    submenu_Item = SubmenuItem("Item", menu_item, mainMenu)
    mainMenu.append_item(submenu_gamer)
    mainMenu.append_item(submenu_character)
    mainMenu.append_item(submenu_location)
    mainMenu.append_item(submenu_boss)
    mainMenu.append_item(submenu_Item)
    mainMenu.show()
