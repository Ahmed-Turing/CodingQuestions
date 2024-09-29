
class ArrayHandler():
    def __init__(self, inArray:list):
        self.state = ""
        self.array = []
        self.isNumeric = self.checkNumeric(inArray)
        self.isString = self.checkString(inArray)
        if self.isString:
            raise Exception("Array contains a string that isn't 'n/a'")
        elif self.isNumeric:
            self.array = NumericArray(inArray=inArray)
        else:
            raise Exception("Array is of neither numeric and string, unknown case")

                
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
    def __init__(self, inArray:list):
        self.min = 0
        self.max = 0
        self.mean = 0
        self.median = 0
        self.mode = 0
        self.sortList(inArray)

    def sortList(self, inArray):
        self.sortingList = inArray
        #Change min,max,mean,median,mode here
    
