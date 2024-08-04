from db.repository import *
import mysql.connector

# this code connects to the database
# class below inherits from Repository abstract class
class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost', # to run LOCALLY, this should be localhost (then back to 'host': 'db')
            'port': '32000', # to run LOCALLY, this should be 32000 (then back to 'port': '3306')
            'database': 'songs',
            'allow_local_infile': True
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    # below destructor code causes error "weakly-referenced object no longer exists"
    # need to research and fix later

    # destructor
    # when done this gets called and close the DB connection
    # def __del__(self):
    #     if self.cursor:
    #         self.cursor.close()
    #     if self.connection and self.connection.is_connected():
    #         self.connection.close()


    def load_songs(self):
        sql = 'SELECT * FROM song_data'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'url': url,
                    'chords': chords,
                    } for (id, url, chords) in self.cursor]
        return entries

    def load_chords(self):
        sql = 'SELECT chords FROM song_data'
        self.cursor.execute(sql)
        chords_list = []
        for row in self.cursor:
            chords_list.append(row[0])
        return chords_list


# if __name__ == '__main__':
#     repo = MysqlRepository()
#     mychords = repo.load_chords()
#     print(type(mychords))
