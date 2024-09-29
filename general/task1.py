
class ArrayHandler():
    def __init__(self, inArray:list):
        self.state = ""
        self.array = []
        self.isNumeric = self.checkNumeric(inArray)
        self.isString = self.checkString(inArray)
        if self.isNumeric and self.isString:
            raise Exception("Array is of both numeric and string, unknown case")
        elif self.isString:
            state = "string"
        elif self.isNumeric:
            state = "numeric"
        else:
            raise Exception("Array is of neither numeric and string, unknown case")
        match state:
            case "numeric":
                
            case "string":
            
    def checkString(inArray:list):
        for item in inArray:
            if isinstance(item, str) and item != "n/a":
                return True
        return False

    def checkNumeric(inArray:list):
        check = False
        for item in inArray:
            if isinstance(item, int):
                check = True
                break
            elif isinstance(item, float):
                check = True
                break
        return check

class NumericArray(list):
    def __init__(self):
        self.min = 0
        self.max = 0
        self.mean = 0
        self.median = 0
        self.mode = 0

    def sortList(self, list):
        
class StringArray(list):
    def __init__(self):
        self.uniques = {}
    
