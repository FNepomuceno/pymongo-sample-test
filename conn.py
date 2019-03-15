from pymongo import MongoClient

default_connection = {
    'hostname': '127.0.0.1',
    'port': 27017,
    'database': 'test-mongo'
}


class Connection:
    def __init__(self, hostname, port, database):
        self.hostname = hostname
        self.port = port
        self.database = database
        self.db = MongoClient(self.hostname, self.port)

    def __enter__(self):
        self.db.__enter__()
        return self.db[self.database]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.__exit__(exc_type, exc_val, exc_tb)
