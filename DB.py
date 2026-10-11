from init_glob_vars import *


# Хранилище игроков в оперативной памяти (вместо SQLite)
class DB:
    # Общее для всех экземпляров: имя -> [high_score, cur_level]
    users = {}

    def __init__(self):
        self.db = DB.users

    def add_data(self, user_name_):
        if user_name_ not in self.db:
            self.db[user_name_] = [0, 1]

    def get_data(self):
        rows = [(name, data[0], data[1]) for name, data in self.db.items()]
        return sorted(rows, key=lambda row: row[1], reverse=True)

    def close_db(self):
        pass

    def set_hscore(self, user_name_, hscore_):
        self.db[user_name_][0] = hscore_

    def get_hscore(self, user_name_):
        return self.db[user_name_][0]
