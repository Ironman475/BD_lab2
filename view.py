class View(object):

    @staticmethod
    def show_list_gamers(Gamers):
        if Gamers:
            print("---------------------------Gamers---------------------------")
            print("|GamerId|", "Login|", "Password|", "  Email  |")
            for row in Gamers:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|")
            print("-----------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_characters(Characters):
        if Characters:
            print("-----------------------------------------Characters---------------------------------------")
            print("|Char_id|", "         Name         |", "   Hit_Points    |", "      LVL       |", "GamerId|")
            for row in Characters:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("-------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_locations(Locations):
        if Locations:
            print("--------------------------------------Locations---------------------------------------")
            print("|LocId|", "  Loc_Name  |", "Population |", "Threat_level|", "Char_id|", "Boss_id |")
            for row in Locations:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5], "|")
            print("-------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_bosses(Bosses):
        if Bosses:
            print("-----------------------------------Bosses-------------------------------------------")
            print("|BossId|", " Boss_Name  |", "Damage|", "LVL |", "Experience|")
            for row in Bosses:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("------------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_items(Items):
        if Items:
            print("--------------------------------Items-----------------------------------------------------")
            print("|ItemId|", " Item_Name  |", "Rarity    |", "Damage|", "Char_id|", "Boss_id |")
            for row in Items:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5], "|")
            print("------------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_boss_or_Character_ByHP(data):
        if data:
            print("--------------------------------------Boss+Character-------------------------------------")
            print("|Character_id|", "Boss_id|", "Char_Hit_Points|", "Boss_Hit_Points|", " Character_Name   |", " Boss_Name   |")
            for row in data:
                print("|", row[0], "\t|", row[1], "\t|", row[2],
                      "|", row[3], "|", row[4], row[5], "\t|", "|")
            print("----------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")
    @staticmethod
    def delete_connection():
        print('**************************************************************')
        print("PostgresSQL connection is closed")
        print('**************************************************************')

    @staticmethod
    def display_added(name, tableName):
        print('\033[92m++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Created new {} - {} to  {}'
              .format(tableName.lower(), name, tableName))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_many_added(count, tableName):
        print('\033[92m++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Created new {} random rows to  {}'
              .format(count, tableName))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_deletion(anyId, tableName):
        print('--------------------------------------------------------------')
        print('Deleted row with id:{} from table {}'
              .format(anyId, tableName))
        print('--------------------------------------------------------------')

    @staticmethod
    def display_gamer_updated(GamerId, oldLogin, oldPassword, oldEmail, newLogin, newPassword, newEmail):
        print('--------------------------------------------------------------')
        print('Change {} login: {} --> {}'
              .format(GamerId, oldLogin, newLogin))
        print('Change {} password: {} --> {}'
              .format(GamerId, oldPassword, newPassword))
        print('Change {} email: {} --> {}'
              .format(GamerId, oldEmail, newEmail))
        print('--------------------------------------------------------------')
