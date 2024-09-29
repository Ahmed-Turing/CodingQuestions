
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
        self.sortingList = []
        total = 0
        apperance = {}
        numberOfValues = len(inArray)
        #Change min,max,mean,median,mode here
        for i in inArray:
            if isinstance(i,str) != False:
                self.sortingList.append(i)
                total += i
                if i in apperance.keys():
                    apperance[i] += 1
                else:
                    apperance.setdefault(i,1)
            else:
                numberOfValues -= 1
            
        for i in range(0, numberOfValues):
            for j in range(i+1, numberOfValues):
                if self.sortingList[i] >= self.sortingList[j]:
                    self.sortingList[i], self.sortingList[j] = self.sortingList[j],self.sortingList[i]
        
        self.min = self.sortingList[0]
        self.max = self.sortingList[numberOfValues - 1]
        self.mean = total/numberOfValues

        if numberOfValues % 2 == 1:
            middleNumber = numberOfValues // 2
            self.median = self.sortingList[middleNumber]
        elif numberOfValues % 2 == 0:
            number1 = numberOfValues / 2
            number2 = number1 - 1
            self.median = (self.sortingList[number1] + self.sortingList[number2])/2
        else:
            raise Exception("No median found")

        self.mode = max(apperance, key=apperance.get)



    
