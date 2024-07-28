from db.mysql_repository import *

repo = MysqlRepository()

def load_chord():
    mysongs = repo.load_chord()

    #update number
    # assert len(mysongs) == tbd