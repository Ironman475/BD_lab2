from timeit import default_timer as timer


class Inspect(object):
    @staticmethod
    def findExistRow(connection, tableName):
        cursor = connection.cursor()
        cursor.execute("select {}_id from public.\"{}\" ORDER BY random() LIMIT 1;"
                       .format(tableName.lower(), tableName))
        value = cursor.fetchall()
        return value[0][0]

    @staticmethod
    def findExistingId(connection, tableName, anyId):
        cursor = connection.cursor()
        cursor.execute("select {}_id from public.\"{}\" where {}_id={};"
                       .format(tableName.lower(), tableName, tableName.lower(), anyId))
        value = cursor.fetchall()
        return len(value) != 0

    @staticmethod
    def findHP(connection, first, second):
        cursor = connection.cursor()
        start = timer()
        cursor.execute(
            "SELECT character_id, public.\"Boss\".boss_id, public.\"Character\".hit_points, public.\"Boss\".hit_points, "
            "public.\"Character\".name, public.\"Boss\".boss_name "
            "FROM public.\"Boss\" INNER JOIN public.\"Character\" ON "
            "public.\"Character\".character_id = public.\"Boss\".boss_id"
            " WHERE public.\"Character\".hit_points  BETWEEN {} and {} and public.\"Boss\".hit_points BETWEEN {} and {} ;".format(first, second, first, second))
        value = cursor.fetchall()
        end = timer()
        print('Searching time - ', end - start)
        return value

    @staticmethod
    def findLocName(connection, name):
        cursor = connection.cursor()
        start = timer()
        cursor.execute("select location_id, loc_name, population, threat_level, character_id, boss_id"
                       " from public.\"Location\" "
                       " where loc_name like '%{}%';".format(name))
        value = cursor.fetchall()
        end = timer()
        print('Searching time - ', end - start)
        return value
