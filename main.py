from conn import Connection, default_connection

if __name__ == "__main__":
    with Connection(**default_connection) as db:
        db.item.drop()
        db.item.insert_many([{
            'name': 'Item 1',
            'description': 'This is an item',
        },{
            'name': 'Item 2',
            'description': 'This is another item',
        }])
        cursor = db.item.find()
        for item in cursor:
            print(item)
