from pymongo import MongoClient

class DataBase:

    def __init__(self):
        cluster = MongoClient("mongodb+srv://inventtle:1234@cluster0.xdubogw.mongodb.net/?retryWrites=true&w=majority")
        db = cluster['inventtle']
        
        self.helmets = list(db['helmets'].find({}))
        self.chestplates = list(db['chestplates'].find({}))
        self.pants = list(db['pants'].find({}))
        self.boots = list(db['boots'].find({}))
        self.weapons = list(db['weapons'].find({}))
        self.artifacts = list(db['artifacts'].find({}))
        self.character = db['character'].find({})[0]
        self.data = db