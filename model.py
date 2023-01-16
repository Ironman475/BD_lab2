import psycopg2
import queriesSQL as SQL
import inspect


class Model(object):

    def __init__(self):
        self._connection = self.connect_to_db()

    @property
    def connection(self):
        return self._connection

    @staticmethod
    def connect_to_db():
        connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="qwerty")
        return connection

    def disconnect_from_db(self):
        if self.connection is not None:
            self.connection.close()


class ModelGamer(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Gamer"

    @property
    def tableName(self):
        return self._tableName

    def read_gamer(self, Gamer_id):
        return SQL.select_one(self.connection, self._tableName, Gamer_id)

    def read_gamers(self):
        return SQL.select_all(self.connection, self._tableName)

    def create_gamer(self, Login, Password, Email):
        return SQL.insert_one_gamer(self.connection, Login, Password, Email)

    def create_many_gamers(self, count):
        return SQL.insert_many_random_gamers(self.connection, count)

    def reform_gamer(self, Gamer_id, Login, Password, Email):
        return SQL.update_gamer(self.connection, Gamer_id, Login, Password, Email)

    def remove_gamer(self, Gamer_id):
        return SQL.delete_one(self.connection, self._tableName, Gamer_id)


class ModelCharacter(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Character"

    @property
    def tableName(self):
        return self._tableName

    def read_characters(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_character(self, Character_id):
        return SQL.select_one(self.connection, self._tableName, Character_id)

    def read_characterbyHP(self, first, second=None):
        return inspect.Inspect.findHP(self.connection, first, second)

    def create_character(self, Name, Hit_Points, LVL, gamer_id):
        return SQL.insert_one_character(self.connection, Name, Hit_Points, LVL, gamer_id)

    def create_many_characters(self, count):
        try:
            gamer_id = inspect.Inspect.findExistRow(self.connection, "Gamer")
            SQL.insert_many_characters(self.connection, gamer_id, count)
            return True
        except Exception as err:
            print(err)
            return False

    def reform_character(self, Character_id, Name, Hit_Points, LVL, Gamer_id):
        return SQL.update_character(self.connection, Character_id, Name, Hit_Points, LVL, Gamer_id)

    def remove_character(self, Character_id):
        return SQL.delete_one(self.connection, self._tableName, Character_id)


class ModelLocation(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Location"

    @property
    def tableName(self):
        return self._tableName

    def read_location(self, Location_Id):
        return SQL.select_one(self.connection, self._tableName, Location_Id)

    def read_Locations(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_location_by_Name(self, name):
        return inspect.Inspect.findLocName(self.connection, name)

    def create_location(self, Loc_Name, Population, Treat_level, Character_id, Boss_id):
        return SQL.insert_one_location(self.connection, Loc_Name, Population, Treat_level, Character_id, Boss_id)

    def create_many_location(self, count):
        try:
            Character_id = inspect.Inspect.findExistRow(self.connection, "Character")
            Boss_id = inspect.Inspect.findExistRow(self.connection, "Boss")
            SQL.insert_many_random_location(self.connection, Character_id, Boss_id, count)
            return True
        except Exception as err:
            print(err)
            return False

    def reform_location(self, Location_id, Loc_Name, Population, Threat_level, Character_id, Boss_id):
        return SQL.update_location(self.connection, Location_id, Loc_Name, Population, Threat_level, Character_id,
                                   Boss_id)

    def remove_location(self, Location_id):
        return SQL.delete_one(self.connection, self._tableName, Location_id)


class ModelBoss(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Boss"

    @property
    def tableName(self):
        return self._tableName

    def read_bosses(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_boss(self, Boss_id):
        return SQL.select_one(self.connection, self._tableName, Boss_id)

    def create_boss(self, Boss_Name, Damage, Hit_Points, LVL, Experience):
        return SQL.insert_boss(self.connection, Boss_Name, Damage, Hit_Points, LVL, Experience)

    def create_random_boss(self, count):
        return SQL.insert_random_bosses(self.connection, count)

    def reform_boss(self, Boss_id, Boss_Name, Damage, Hit_Points, LVL, Experience):
        return SQL.update_boss(self.connection, Boss_id, Boss_Name, Damage, Hit_Points, LVL, Experience)

    def remove_boss(self, Boss_id):
        return SQL.delete_one(self.connection, self._tableName, Boss_id)


class ModelItem(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Item"

    @property
    def tableName(self):
        return self._tableName

    def read_items(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_item(self, Item_id):
        return SQL.select_one(self.connection, self._tableName, Item_id)

    def create_item(self, Item_Name, Rarity, Damage, Character_id, Boss_id):
        return SQL.insert_item(self.connection, Item_Name, Rarity, Damage, Character_id, Boss_id)

    def create_random_items(self, count):
        try:
            Character_id = inspect.Inspect.findExistRow(self.connection, "Character")
            Boss_id = inspect.Inspect.findExistRow(self.connection, "Boss")
            SQL.insert_random_item(self.connection, Boss_id, Character_id, count)
            return True
        except Exception as err:
            print(err)
            return False

    def reform_item(self, Item_id, Item_Name, Rarity, Damage, Character_id, Boss_id):
        return SQL.update_item(self.connection, Item_id, Item_Name, Rarity, Damage, Character_id,
                               Boss_id)

    def remove_item(self, Item_id):
        return SQL.delete_one(self.connection, self._tableName, Item_id)
