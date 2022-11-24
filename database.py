import pymongo
from pymongo import MongoClient

class DataBase:
    character = {}
    helmets = {}
    chestplates = {}
    pants = {}
    boots = {}
    weapons = {}
    artifacts = {}
    def __init__(self):
        cluster = MongoClient("mongodb+srv://inventtle:1234@cluster0.xdubogw.mongodb.net/?retryWrites=true&w=majority")
        db = cluster['inventtle']
        
        self.helmets = db['helmets']
        self.chestplates = db['chestplates']
        self.pants = db['pants']
        self.boots = db['boots']
        self.weapons = db['weapons']
        self.artifacts = db['artifacts']
        self.character = db['character'].find({})[0]