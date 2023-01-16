class Input(object):

    @staticmethod
    def input_update_gamer(Gamer):
        inputLogin = input("Enter login: ")
        inputPassword = input("Enter password: ")
        inputEmail = input("Enter user email: ")
        return {
            'login': inputLogin,
            'password': inputPassword,
            'email': inputEmail,
        }

    @staticmethod
    def input_update_character(Character):
        inputName = input("Enter name: ")
        inputHP = input("Enter hit_points: ")
        inputLVL = input("Enter lvl: ")
        inputGamer_id = input("Enter gamer_id: ")
        return {
            'name': inputName,
            'hit_points': inputHP,
            'lvl': inputLVL,
            'gamer_id': inputGamer_id
        }

    @staticmethod
    def input_update_location(Location):
        inputName = input("Enter name: ")
        inputPop = input("Enter population: ")
        inputThL = input("Enter threat level: ")
        inputCh_id = input("Enter character_id: ")
        inputBoss_id = input("Enter boss_id: ")
        return {
            'loc_name': inputName,
            'population': inputPop,
            'threat_level': inputThL,
            'character_id': inputCh_id,
            'boss_id': inputBoss_id
        }

    @staticmethod
    def input_update_boss(Boss):
        inputName = input("Enter name: ")
        inputDamage = input("Enter damage: ")
        inputHP = input("Enter hit points: ")
        inputLVL = input("Enter lvl: ")
        inputExp = input("Enter experience: ")
        return {
            'boss_name': inputName,
            'damage': inputDamage,
            'hit_points': inputHP,
            'lvl': inputLVL,
            'experience': inputExp
        }

    @staticmethod
    def input_update_item(item):
        inputName = input("Enter name: ")
        inputRarity = input("Enter rarity: ")
        inputDamage = input("Enter damage: ")
        inputCharacter_id = input("Enter character id (can be null) : ")
        inputBoss_id = input("Enter boss id (can be null) :  ")
        return {
            'item_name': inputName,
            'rarity': inputRarity,
            'damage': inputDamage,
            'character_id': inputCharacter_id,
            'boss_id': inputBoss_id
        }

    @staticmethod
    def input_id(tableName):
        inputId = input("Enter {} id: ".format(tableName))
        return inputId

    @staticmethod
    def input_count():
        inputCount = input("Enter more than 1 random row: ")
        return int(inputCount)

    @staticmethod
    def input_two_values():
        firstValue = input("Enter start value: ")
        secondValue = input("Enter finish value: ")
        return [firstValue, secondValue]

    @staticmethod
    def input_name():
        inputName = input("Enter name of location ")
        return inputName
