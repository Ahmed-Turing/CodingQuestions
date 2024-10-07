#upper case takes higher priority (appears first)

class SearchBar():
    def __init__(self, inArray:list):
        #make array into a string to search through
        self.searchString = " ".join(inArray)
   
    def query(self, query:str):
        result = []
        check = False
        #find each string from query by looping through the searchString and the query
        for i, _ in enumerate(self.searchString):
            if len(query) > len(self.searchString) - i:
                break
            else:
                for n, c in enumerate(query.lower()):
                    #if all characters in the section of string matches the query, add the word's index to result
                    if c == self.searchString[i+n].lower():
                        check = True
                    else:
                        check = False
                        break
                if check:
                    result.append(i)
        return result

#same process using python methods
def stringFindAll(searchString:str, query:str):
    '''
        searchString is a string containing all words
        query is a string containing the item we look for
    '''
    return [c for c in range(len(searchString)) if searchString.lower().startswith(query.lower(), c)]

def test_task4():
    #test using string_array.txt
    textFile= "general/test_files/string_array.txt"
    query = "fact"
    with open(textFile) as pages:
        pageArray = pages.read().replace("n/a", " ").split()
        pages.close()
    search = SearchBar(pageArray)
    #prints result of both search methods
    print(search.query(query))
    print(stringFindAll(" ".join(pageArray), query))


if __name__ == "__main__":
    test_task4()
