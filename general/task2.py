class DataStore():
    def __init__(self):
        self.values = []
        self.keys = []

    def toString(self):
        items = ""
        for i in range(len(self.values)):
            items += f"{self.keys[i]}: {self.values[i]}, "
        return items
    
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
                valueIndex = self.keys.index(key)
                self.values[valueIndex] = value
            else:
                raise Exception(f"'{key}' does not exist as a key: Cannot update")
            
    def deleteKey(self, key):
        if(key in self.keys):
            valueIndex = self.keys.index(key)
            self.keys.remove(key)
            valueRemoved = self.values[valueIndex]
            self.values.pop(valueIndex)
            return valueRemoved
        else:
            raise Exception(f"'{key}' does not exist as a key: Cannot delete")
    
class DataStoreDict(dict):
    def __init__(self, store=dict):
        self.store = store

    def toString(self):
        return self.store
    
    def createKey(self, key, value):
        self.store.setdefault(key, value)

    def readKey(self,key):
        return self.store.get(key)
    
    def updateKey(self,key,value):
        self.store[key] = value

    def deleteKey(self, key):
        return self.store.pop(key)
    

if __name__ == "__main__":
    storage = DataStore()
    storage.createKey("id", "1")
    storage.createKey("Job", "Accountant")
    storage.createKey("Amount", 1)
    print(storage.toString())
    storage.createKey("Amount","4")
    storage.updateKey("Job", "Manager")
    #storage.updateKey("342",21)
    print(storage.toString())
    storage.updateKey("Amount", 2)
    print(storage.toString())
    print(storage.readKey("Job"))
    #print(storage.readKey("1"))
    print(storage.deleteKey("Amount"))
    #storage.deleteKey("123")
    print(storage.toString())
    dictStorage = DataStoreDict({})
    dictStorage.createKey("id", 1)
    dictStorage.createKey("Job", "Construction")
    dictStorage.createKey("Amount", 1)
    print(dictStorage.toString())
    dictStorage.updateKey("Job", "Manager")
    print(dictStorage.toString())
    print(dictStorage.readKey("Amount"))
    print(dictStorage.deleteKey("Job"))
    print(dictStorage.toString())
