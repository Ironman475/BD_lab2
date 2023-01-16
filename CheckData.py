class Check(object):
    @staticmethod
    def isGamerAttributes(Gamer):
        if 'login' and 'password' and 'email' not in Gamer:
            return False
        return True

    @staticmethod
    def isCharacterAttributes(character):
        if 'name' and 'hit_points' and 'lvl' and 'gamer_id' not in character:
            return False
        return True

    @staticmethod
    def isLocationAttributes(location):
        if 'loc_name' and 'population' and 'threat_level' and 'character_id' and 'boss_id' not in location:
            return False
        return True

    @staticmethod
    def isBossAttributes(boss):
        if 'boss_name' and 'hit_points' and 'damage' and 'lvl' and 'experience' not in boss:
            return False
        return True

    @staticmethod
    def isItemAttributes(item):
        if 'item_name' and 'rarity' and 'damage' and 'character_id' and 'boss_id' not in item:
            return False
        return True

    @staticmethod
    def updateGamer(gamer, older):
        i = 0
        options = ['login', 'password', 'email']
        for key in options:
            i += 1
            if key not in gamer:
                gamer[key] = older[0][i]
        return gamer

    @staticmethod
    def updateCharacter(character, older):
        i = 0
        options = ['name', 'hit_points', 'lvl', 'gamer_id']
        for key in options:
            i += 1
            if key not in character:
                character[key] = older[0][i]
        return character

    @staticmethod
    def updateLocation(location, older):
        i = 0
        options = ['loc_name', 'population', 'threat_level', 'character_id', 'boss_id']
        for key in options:
            i += 1
            if key not in location:
                location[key] = older[0][i]
        return location

    @staticmethod
    def updateBoss(boss, older):
        i = 0
        options = ['boss_name', 'damage', 'hit_points', 'lvl', 'experience']
        for key in options:
            i += 1
            if key not in boss:
                boss[key] = older[0][i]
        return boss

    @staticmethod
    def updateItem(item, older):
        i = 0
        options = ['item_name', 'rarity', 'damage', 'character_id', 'boss_id']
        for key in options:
            i += 1
            if key not in item:
                item[key] = older[0][i]
        return item
