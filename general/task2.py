class DataStore():
    #could be a dictionary or hashmap
    pass
class DataStoreDict(dict):
    def __init__(self, store=dict):
        self.store = store
    def createKey(self,key, value):
        self.store.setdefault(key, value)
    def readKey(self,key):
        return self.store.get(key)
    def updateKey(self,key,value):
        self.store[key] = value
    def deleteKey(self, key):
        return self.store.pop(key)