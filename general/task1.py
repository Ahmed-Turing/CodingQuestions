import os

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

class ArrayHandler():
    def __init__(self, inArray:list):
        self.isNumeric = checkNumeric(inArray)
        self.isString = checkString(inArray)
        if self.isString and not self.isNumeric:
            self.array = StringArray(inArray=inArray)
        elif self.isNumeric and not self.isString:
            self.array = NumericArray(inArray=inArray)
        else:
            raise Exception("Array is of neither numeric and string, unknown case")

class NumericArray(list):
    def __init__(self, inArray:list):
        self.min = 0
        self.max = 0
        self.mean = 0
        self.median = 0
        self.mode = 0
        self.sortingList = []
        self.sortList(inArray)

    def sortList(self, inArray):
        total = 0
        apperance = {}
        numberOfValues = len(inArray)
        #Change min,max,mean,median,mode here
        for i in inArray:
            if isinstance(i,str) == False:
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
            number1 = int(numberOfValues / 2)
            number2 = int(number1 - 1)
            self.median = (self.sortingList[number1] + self.sortingList[number2])/2
        else:
            raise Exception("No median found")

        self.mode = max(apperance, key=apperance.get)

class StringArray(list):
    def __init__(self, inArray:list):
        self.frequency = {}
        self.array = []
        self.calcFrequency(inArray)
    def calcFrequency(self, inArray):
        total = 0
        punc = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        for word in inArray:
            for char in word:
                if char in punc and word != "n/a" and word != "^p":
                    word = word.replace(char, "")
            self.array.append(word)
            if word in self.frequency:
                self.frequency[word] += 1
                total += 1
            elif word not in self.frequency:
                self.frequency.setdefault(word,1)
                total += 1
            else:
                raise Exception("Error making frequency table")
        for i in self.frequency.keys():
            self.frequency[i] /= total

def text_task1():
    lotsOfStringsFile = "/Users/davidzhao/Dev/CodingQuestions/general/test_files/string_array.txt"
    with open(lotsOfStringsFile) as stringFile:
        stringTestArray = stringFile.read().split()
        stringArrayFormater = ArrayHandler(stringTestArray)
        print(stringArrayFormater.array.frequency)
        stringFile.close()
    lotsOfNumbersFile = "/Users/davidzhao/Dev/CodingQuestions/general/test_files/numbers.txt"
    with open(lotsOfNumbersFile) as numberFile:
        numTestArray = numberFile.read().split()
        for i in range(len(numTestArray)):
            if(numTestArray[i] != "n/a"):
                numTestArray[i] = int(numTestArray[i])
        numArrayFormater = ArrayHandler(numTestArray)
        print(numArrayFormater.array.min)
        print(numArrayFormater.array.max)
        print(numArrayFormater.array.mode)
        print(numArrayFormater.array.median)
        print(numArrayFormater.array.mean)
        print(numArrayFormater.array.sortingList)
        numberFile.close()
    try:
        stringTestArray.extend(numTestArray)
        brokenFormater = ArrayHandler(stringTestArray)
    except Exception as e:
        if str(e) == "Array is of neither numeric and string, unknown case":
            print("array of multiple types is catched")
        else:
            raise Exception(e)
        
if __name__ == "__main__":
    text_task1()



        

    
