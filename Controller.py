import InputData
import CheckData


class ControllerGamer(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_gamers(self):
        Gamers = self.model.read_gamers()
        self.view.show_list_gamers(Gamers)

    def show_gamer(self):
        Gamer_id = InputData.Input.input_id(self.model.tableName)
        Gamer = self.model.read_gamer(Gamer_id)
        self.view.show_list_gamers(Gamer)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def insert_gamer(self, Gamer):
        try:
            Gamer = InputData.Input.input_update_gamer(Gamer)
            assert CheckData.Check.isGamerAttributes(Gamer), 'Some gamer attribute was not add'
            self.model.create_gamer(Gamer['login'], Gamer['password'], Gamer['email'])
            self.view.display_added(Gamer['login'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_gamers(self):
        try:
            count = InputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_gamers(count)
            self.view.display_many_added(count, self.model.tableName)
        except Exception as err:
            print(err)

    def update_gamer(self, Gamer):
        try:
            Gamer_id = InputData.Input.input_id(self.model.tableName)
            Gamer = InputData.Input.input_update_gamer(Gamer)
            old = self.model.read_gamer(Gamer_id)
            newGamer = CheckData.Check.updateGamer(Gamer, old)
            self.model.reform_gamer(Gamer_id, newGamer['login'], newGamer['password'], newGamer['email'])
            self.view.display_added(Gamer['login'], self.model.tableName)
            self.view.display_gamer_updated(Gamer_id, old[0][1], old[0][2], newGamer['login'], newGamer['password'],
                                            newGamer['email'])
        except Exception as err:
            print(err)

    def delete_gamer(self):
        try:
            Gamer_Id = InputData.Input.input_id(self.model.tableName)
            self.model.remove_gamer(Gamer_Id)
            self.view.display_deletion(Gamer_Id, self.model.tableName)
        except Exception as err:
            print(err)


class ControllerCharacter(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_characters(self):
        characters = self.model.read_characters()
        self.view.show_list_characters(characters)

    def show_character(self):
        Character_id = InputData.Input.input_id(self.model.tableName)
        characters = self.model.read_characterbyHP(Character_id)
        self.view.show_list_characters(characters)

    def character_findHP(self):
        hp = InputData.Input.input_two_values()
        character = self.model.read_characterbyHP(hp[0], hp[1])
        self.view.show_boss_or_Character_ByHP(character)

    def insert_character(self, character):
        try:
            character = InputData.Input.input_update_character(character)
            assert CheckData.Check.isCharacterAttributes(character), 'Some character attribute was not add'
            check = self.model.create_character(character['name'], character['hit_points'],
                                                character['lvl'],
                                                character['gamer_id'])
            if check:
                self.view.display_added(character['name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_characters(self):
        try:
            count = InputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_characters(count)
            self.view.display_many_added(count, self.model.tableName)
        except Exception as err:
            print(err)

    def update_character(self, character):
        try:
            Character_id = InputData.Input.input_id(self.model.tableName)
            character = InputData.Input.input_update_character(character)
            old = self.model.read_character(Character_id)
            newCharacter = CheckData.Check.updateCharacter(character, old)
            check = self.model.reform_character(Character_id, newCharacter['name'],
                                                newCharacter['hit_points'],
                                                newCharacter['lvl'],
                                                newCharacter['gamer_id'])
            if check:
                self.view.display_added(character['name'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_character(self):
        try:
            Character_id = InputData.Input.input_id(self.model.tableName)
            self.model.remove_character(Character_id)
            self.view.display_deletion(Character_id, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()


class ControllerLocation(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_locations(self):
        locations = self.model.read_Locations()
        self.view.show_list_locations(locations)

    def show_location(self):
        Location_id = InputData.Input.input_id(self.model.tableName)
        Location = self.model.read_location(Location_id)
        self.view.show_list_locations(Location)

    def show_location_by_Name(self):
        name = InputData.Input.input_name()
        location = self.model.read_location_by_Name(name)
        self.view.show_list_locations(location)

    def insert_location(self, location):
        try:
            location = InputData.Input.input_update_location(location)
            assert CheckData.Check.isLocationAttributes(location), 'Some location attribute was not add'
            check = self.model.create_location(location['loc_name'], location['population'],
                                               location['threat_level'],
                                               location['character_id'], location['boss_id'])
            if check:
                self.view.display_added(location['loc_name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_locations(self):
        try:
            count = InputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_location(count)
            self.view.display_many_added(count, self.model.tableName)
        except Exception as err:
            print(err)

    def update_location(self, location):
        try:
            Location_id = InputData.Input.input_id(self.model.tableName)
            location = InputData.Input.input_update_location(location)
            old = self.model.read_location(Location_id)
            newLocation = CheckData.Check.updateLocation(location, old)
            assert CheckData.Check.isLocationAttributes(location), 'Some location attribute was not add'
            check = self.model.reform_location(Location_id, newLocation['loc_name'], newLocation['population'],
                                               newLocation['threat_level'],
                                               newLocation['character_id'],
                                               newLocation['boss_id'])
            if check:
                self.view.display_added(location['loc_name'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_location(self):
        try:
            Location_id = InputData.Input.input_id(self.model.tableName)
            self.model.remove_location(Location_id)
            self.view.display_deletion(Location_id, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()


class ControllerBoss(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_bosses(self):
        bosses = self.model.read_bosses()
        self.view.show_list_bosses(bosses)

    def show_boss(self):
        Boss_id = InputData.Input.input_id(self.model.tableName)
        boss = self.model.read_boss(Boss_id)
        self.view.show_list_bosses(boss)

    def insert_boss(self, boss):
        try:
            boss = InputData.Input.input_update_boss(boss)
            assert CheckData.Check.isBossAttributes(boss), 'Some boss attribute was not add'
            check = self.model.create_boss(boss['boss_name'], boss['hit_points'], boss['damage'],
                                           boss['lvl'],
                                           boss['experience'])
            if check:
                self.view.display_added(boss['boss_name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_random_boss(self):
        try:
            count = InputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_random_boss(count)
            self.view.display_added('random', self.model.tableName)
        except Exception as err:
            print(err)

    def update_boss(self, boss):
        try:
            Boss_id = InputData.Input.input_id(self.model.tableName)
            boss = InputData.Input.input_update_boss(boss)
            old = self.model.read_boss(Boss_id)
            newBoss = CheckData.Check.updateBoss(boss, old)
            assert CheckData.Check.isBossAttributes(boss), 'Some boss attribute was not add'
            check = self.model.reform_boss(Boss_id, newBoss['boss_name'], newBoss['hit_points'],
                                           newBoss['damage'],
                                           newBoss['lvl'],
                                           newBoss['experience'])
            if check:
                self.view.display_added(newBoss['boss_name'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_boss(self):
        try:
            Boss_id = InputData.Input.input_id(self.model.tableName)
            self.model.remove_boss(Boss_id)
            self.view.display_deletion(Boss_id, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()


class ControllerItem(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_items(self):
        item = self.model.read_items()
        self.view.show_list_items(item)

    def show_item(self):
        Item_id = InputData.Input.input_id(self.model.tableName)
        item = self.model.read_item(Item_id)
        self.view.show_list_items(item)

    def insert_item(self, item):
        try:
            item = InputData.Input.input_update_item(item)
            assert CheckData.Check.isItemAttributes(item), 'Some item attribute was not add'
            check = self.model.create_item(item['item_name'], item['rarity'],
                                           item['damage'],
                                           item['character_id'],
                                           item['boss_id'])
            if check:
                self.view.display_added(item['item_name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_random_item(self):
        try:
            count = InputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_random_items(count)
            self.view.display_added('random', self.model.tableName)
        except Exception as err:
            print(err)

    def update_item(self, item):
        try:
            Item_id = InputData.Input.input_id(self.model.tableName)
            item = InputData.Input.input_update_item(item)
            old = self.model.read_item(Item_id)
            newItem = CheckData.Check.updateItem(item, old)
            assert CheckData.Check.isItemAttributes(item), 'Some item attribute was not add'
            check = self.model.reform_item(Item_id, newItem['item_name'],
                                           newItem['rarity'],
                                           newItem['damage'],
                                           newItem['character_id'],
                                           newItem['boss_id'])
            if check:
                self.view.display_added(newItem['item_name'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_item(self):
        try:
            Item_id = InputData.Input.input_id(self.model.tableName)
            self.model.remove_item(Item_id)
            self.view.display_deletion(Item_id, self.model.tableName)
        except Exception as err:
            print(err)

    def delete_comment_reaction(self):
        try:
            Item_id = InputData.Input.input_id(self.model.tableName)
            self.model.remove_item(Item_id)
            self.view.display_deletion(Item_id, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()
