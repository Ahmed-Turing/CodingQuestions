class DataStore():
    def __init__(self):
        self.values = []
        self.keys = []

    def createKey(self, key, value):
        if(key in self.keys):
            valueIndex = self.keys.index(key)
            self.values[valueIndex] = value
        elif(key not in self.keys):
            self.keys.append(key)
            self.values.append(value)
        else:
            raise Exception("Issue when creating key")
        
    def readKey(self,key):
        if(key in self.keys):
            valueIndex = self.keys.index(key)
            return self.values[valueIndex]
        else:
            raise Exception(f"'{key}' does not exist as a key: Cannot read")
        
    def updateKey(self, key, value):
            if(key in self.keys):
                valueIndex = self.keys.index[key]
                self.values[valueIndex] = value
            else:
                raise Exception(f"'{key}' does not exist as a key: Cannot update")
            
    def deleteKey(self, key):
        if(key in self.keys):
            valueIndex = self.keys.index[key]
            self.keys.remove(key)
            self.values.pop(valueIndex)
        else:
            raise Exception(f"'{key}' does not exist as a key: Cannot delete")
    
class DataStoreDict(dict):
    def __init__(self, store=dict):
        self.store = store
    def createKey(self, key, value):
        self.store.setdefault(key, value)
    def readKey(self,key):
        return self.store.get(key)
    def updateKey(self,key,value):
        self.store[key] = value
    def deleteKey(self, key):
        return self.store.pop(key)