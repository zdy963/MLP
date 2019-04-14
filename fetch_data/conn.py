import pymysql


def get_config(key=None):
    config = {
        "host": "119.29.53.97",
        "port": 3306,
        "user": "root",
        "password": "admin",
        "db": "mlp",
        "charset": "utf8"
    }
    return config


def conn_db(dic=True):
    """
    Connect to local database
    :return: The cursor of local database
    """
    config = get_config('db')
    if dic:
        config['cursorclass'] = pymysql.cursors.DictCursor
        db = pymysql.connect(**config,local_infile=1)
    else:
        db = pymysql.connect(**config)
    return db


class dbconn():
    def __init__(self,dic=True):
        self.db = conn_db(dic)

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()