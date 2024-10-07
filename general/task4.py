#upper case takes higher priority (appears first)

class SearchBar():
    def __init__(self, inArray:list):
        self.searchString = " ".join(inArray)
   
    def query(self, query:str):
        result = []
        check = False
        for i, _ in enumerate(self.searchString):
            if len(query) > len(self.searchString) - i:
                break
            else:
                for n, c in enumerate(query.lower()):
                    if c == self.searchString[i+n].lower():
                        check = True
                    else:
                        check = False
                        break
                if check:
                    result.append(i)
        return result

def stringFindAll(searchString:str, query:str):
    return [c for c in range(len(searchString)) if searchString.lower().startswith(query.lower(), c)]

def test_task4():
    textFile= "/Users/davidzhao/Dev/CodingQuestions/general/test_files/string_array.txt"
    query = "fact"
    with open(textFile) as pages:
        pageArray = pages.read().replace("n/a", " ").split()
        pages.close()
    search = SearchBar(pageArray)
    print(search.query(query))
    print(stringFindAll(" ".join(pageArray), query))
if __name__ == "__main__":
    test_task4()
