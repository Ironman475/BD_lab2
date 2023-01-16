import psycopg2


def select_one(connection, tableName, attributeId):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.\"{}\" WHERE {}_id = {}".format(tableName, tableName.lower(), attributeId))

    record = cursor.fetchall()
    return record


def select_all(connection, tableName):
    try:
        cursor = connection.cursor()
        cursor.execute("select * from public.\"{}\"".format(tableName, tableName))

        record = cursor.fetchall()
        return record

    except(Exception, psycopg2.Error) as error:
        print("Error with fetching all data", error)


def insert_one_gamer(connection, Login, Password, Email):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Gamer\" (login, password, email)"
                       "values ('{}', '{}', '{}')".format(Login, Password, Email))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with gamer inserting", error)


def insert_many_random_gamers(connection, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Gamer\" (login, password, email)"
                       "select left(md5(random()::text), 5),"
                       "left(md5(random()::text), 8), concat(left(md5(random()::text), 5),'@gmail.com')"
                       "FROM generate_series(1, {})".format(count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with gamer inserting", error)


def insert_one_character(connection, Name, Hit_Points, LVL, gamer_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Character\" (name, hit_points, lvl, gamer_id)"
                       "values ('{}', {}, {}, {})".format(Name, Hit_Points, LVL, gamer_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with character inserting", error)


def insert_many_characters(connection, character_id, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Character\" (name, hit_points, lvl, gamer_id)"
                       "select left(md5(random()::text), 5), "
                       "trunc((random()::int*300 + 1),5), trunc((random()::int*45), 5), {} "
                       "from generate_series(1, {})".format(character_id, count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with character inserting", error)


def insert_one_location(connection, Loc_Name, Population, Treat_level, Character_id, Boss_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "insert into public.\"Location\" (loc_name, population, threat_level, character_id, boss_id)"
            "values ('{}', {}, '{}', {}, {})".format(Loc_Name, Population, Treat_level, Character_id,
                                                         Boss_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with comment inserting", error)


def insert_many_random_location(connection, Character_Id, Boss_id, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Location\" (loc_name, population, threat_level, character_id, boss_id)"
                       "select left(md5(random()::text), 5),"
                       "trunc((random()::int), 5),"
                       "left(md5(random()::text), 5),"
                       "{}, {} from generate_series(1, {})".format(Character_Id, Boss_id, count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with location inserting", error)


def insert_boss(connection, Boss_Name, Damage, Hit_Points, LVL, Experience):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Boss\" (boss_name, damage, hit_Points, lvl, experience)"
                       "values ('{}', {}, {}, {}, {})".format(Boss_Name, Damage, Hit_Points, LVL, Experience))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with boss inserting", error)


def insert_random_bosses(connection, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Boss\" (boss_name, damage, hit_points, lvl, experience)"
                       "select left(md5(random()::text), 5),"
                       "trunc((random()::int*250),5),"
                       "trunc((random()::int*1500),5),"
                       "trunc((random()::int*15),5),"
                       "trunc((random()::int*150),5) "
                       "from generate_series(1, {})".format(count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with boss inserting", error)


def insert_item(connection, Item_Name, Rarity, Damage, Character_id, Boss_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Item\" (item_name, rarity, damage, character_id, boss_id)"
                       "values ('{}', '{}', {}, {}, {})".format(Item_Name, Rarity, Damage, Character_id, Boss_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with item inserting", error)


def insert_random_item(connection, Boss_Name, Character_id, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Item\" (item_name, rarity, damage, character_id, boss_id)"
                       "select left(md5(random()::text), 5),"
                       "left(md5(random()::text), 5),"
                       "trunc((random()::int*150), 3),"
                       "{}, {} from generate_series(1, {})".format(Boss_Name, Character_id, count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with item inserting", error)


def update_character(connection, Character_id, Name, Hit_Points, LVL, Gamer_id):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"Character\" set name = '{}', hit_points = {}, lvl = {}, gamer_id = {}"
                       "where character_id = {}".format(Name, Hit_Points, LVL, Gamer_id, Character_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with character updating", error)


def update_gamer(connection, Gamer_id, Login, Password, Email):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"Gamer\" set login = '{}', password = '{}', email = '{}'"
                       "where gamer_id = {}".format(Login, Password, Email, Gamer_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with gamer updating", error)


def update_location(connection, Location_id, Loc_Name, Population, Threat_level, Character_id, Boss_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "update public.\"Location\" set loc_name = '{}', population = {}, threat_level = '{}', character_id = {}, "
            "boss_id = {}"
            "where location_id = {}".format(Loc_Name, Population, Threat_level, Character_id, Boss_id, Location_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with location updating", error)


def update_item(connection, Item_id, Item_Name, Rarity, Damage, Character_id,
                Boss_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "update public.\"Item\" set item_name = '{}', rarity = '{}', damage = {}, character_id = {}, boss_id = {}"
            "where item_id = {}".format(Item_Name, Rarity, Damage, Character_id,
                                        Boss_id, Item_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with item updating", error)


def update_boss(connection, Boss_id, Boss_Name, Damage, Hit_Points, LVL, Experience):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "update public.\"Boss\" set boss_name = '{}', damage = {}, hit_points = {}, lvl = {}, experience = {}"
            "where boss_id = '{}'".format(Boss_Name, Damage, Hit_Points, LVL, Experience, Boss_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with boss updating", error)


def delete_one(connection, tableName, elementId):
    try:
        cursor = connection.cursor()
        cursor.execute("delete from public.\"{}\" where {}_id = {}".format(tableName, tableName.lower(), elementId))
        connection.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error with deleting", error)
