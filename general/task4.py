#upper case takes higher priority (appears first)

class SearchBar():
    def __init__(self, inArray:list):
        self.inArray = inArray.sort()
   
    def query(self, query:str) -> list:
        result = []
        for word in self.inArray:
            if query.lower() in word.lower():
                result.append(word)
        return result
