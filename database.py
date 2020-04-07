import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite")
        self.cursor = self.conn.cursor()
        self.create_database()

    def __del__(self):
        self.conn.close()

    def create_database(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS male_names(
                        name text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS female_names(
                        name text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS surnames(
                        surname text)""")
        self.conn.commit()

    def get_male_name_list(self):
        self.cursor.execute("SELECT name FROM male_names")
        male_name_list = [record[0] for record in self.cursor.fetchall()]
        return male_name_list

    def get_female_name_list(self):
        self.cursor.execute("SELECT name FROM female_names")
        female_name_list = [record[0] for record in self.cursor.fetchall()]
        return female_name_list

    def get_surname_list(self):
        self.cursor.execute("SELECT surname FROM surnames")
        surname_list = [record[0] for record in self.cursor.fetchall()]
        return surname_list



# if __name__== '__main__':
#     database = Database()
#     with open('London 1920s NPC Names List - First Names.csv') as csv_file:
#         lines = csv_file.readlines()
#         for line in lines:
#             name_list = line.split(',')
#             if name_list[0] != "":
#                 name = name_list[0].lower().capitalize()
#                 database.cursor.execute(f"INSERT INTO male_names (name) VALUES ('{name}')")
#             if name_list[1] != "":
#                 name = name_list[1].lower().capitalize()
#                 database.cursor.execute(f"INSERT INTO female_names (name) VALUES ('{name}')")
#
#     database.conn.commit()

# if __name__== '__main__':
#     database = Database()
#     with open('London 1920s NPC Names List - Surnames.csv') as csv_file:
#         lines = csv_file.readlines()
#         for surname in lines:
#             database.cursor.execute(f"INSERT INTO surnames (surname) VALUES ('{surname}')")
#
#     database.conn.commit()







