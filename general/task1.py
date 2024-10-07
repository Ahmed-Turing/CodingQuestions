
#checks if an array is all strings with some n/a
def checkString(inArray:list):
        for item in inArray:
            if isinstance(item, str) and item != "n/a":
                return True
        return False

#checks if an array is all numerical values with some n/a
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

'''
    processes done to an numeric array:
        1. find min
        2. find max
        3. find mean, median, mode
        4. sort the list of numbers
'''
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
        #removes instances of n/a from numeric list and keeps track of each numbers apperiance in a hashmap
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
        
        #sorts the list from least to greatest
        for i in range(0, numberOfValues):
            for j in range(i+1, numberOfValues):
                if self.sortingList[i] >= self.sortingList[j]:
                    self.sortingList[i], self.sortingList[j] = self.sortingList[j],self.sortingList[i]
        
        #defines min, max, and mean
        self.min = self.sortingList[0]
        self.max = self.sortingList[numberOfValues - 1]
        self.mean = total/numberOfValues
        
        #if an odd amount of numbers inputed, median is the value at the middle index, else average out the two center values
        if numberOfValues % 2 == 1:
            middleNumber = numberOfValues // 2
            self.median = self.sortingList[middleNumber]
        elif numberOfValues % 2 == 0:
            number1 = int(numberOfValues / 2)
            number2 = int(number1 - 1)
            self.median = (self.sortingList[number1] + self.sortingList[number2])/2
        else:
            raise Exception("No median found")

        #define the mode from hashmap
        self.mode = max(apperance, key=apperance.get)
'''
    processes done to an string array:
        1. find frequency of strings apperiance
        2. remove symbols from words if present
'''
class StringArray(list):
    def __init__(self, inArray:list):
        self.frequency = {}
        self.array = []
        self.calcFrequency(inArray)
        
    def calcFrequency(self, inArray):
        total = 0
        punc = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        for word in inArray:
            #remove punctuation from word if present, then adds the word to different array
            for char in word:
                if char in punc and word != "n/a" and word != "^p":
                    word = word.replace(char, "")
            if word != "n/a" and word != "^p":
                self.array.append(word)

            #create hashmap to find frequency of word appereance
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
    #test files
    lotsOfStringsFile = "general/test_files/string_array.txt"
    lotsOfNumbersFile = "general/test_files/numbers.txt"
    checkSort = False

    #tests the string array handling
    with open(lotsOfStringsFile) as stringFile:
        stringTestArray = stringFile.read().split()
        stringArrayFormater = ArrayHandler(stringTestArray)
        print(f"frequency of n/a: {stringArrayFormater.array.frequency['n/a']}")
        stringFile.close()
    print("string array handled correctly\n")

    #tests the numeric array handling
    with open(lotsOfNumbersFile) as numberFile:
        numTestArray = numberFile.read().split()
        for i in range(len(numTestArray)):
            if(numTestArray[i] != "n/a"):
                numTestArray[i] = int(numTestArray[i])
        numArrayFormater = ArrayHandler(numTestArray)
        print(f"min: {numArrayFormater.array.min}")
        print(f"max: {numArrayFormater.array.max}")
        print(f"mode: {numArrayFormater.array.mode}")
        print(f"median: {numArrayFormater.array.median}")
        print(f"mean: {numArrayFormater.array.mean}")
        for i in range(len(numArrayFormater.array.sortingList)):
            if i + 1 < len(numArrayFormater.array.sortingList):
                if i < i+1:
                    checkSort = True 
                else:
                    checkSort = False
                    break
        if checkSort:
            print("numeric list is sorted")
        else:
            raise Exception("numeric list is not sorted")
        numberFile.close()

    #checks if user inputs an array with both string and numeric values
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
