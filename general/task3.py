import task1 as fileToArray
import csv
import os

def textFileProcesser(textFile:str):
    punc = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
    inArray = textFile.read().split(" ")
    try:
        for i in range(len(inArray)):
            inArray[i] = int(inArray[i])
    except TypeError:
        for word in inArray:
            for char in word:
                if char in punc and word != "n/a":
                    word = word.replace(char, "")
    
    data = fileToArray.ArrayHandler(inArray)
    return data.array

def csvFileProcesser(csvFile:str):
    data = []
    keys = []
    keys = csvFile.readline()
    csvDictReader = csv.DictReader(csvFile)
    for row in csvDictReader:
        data.append(row)
    
    if "application_id" not in keys:
        raise Exception("no key for application_id found")
    elif len(data) < 15:
        raise Exception(f"csv file has to little rows: {len(data)} < 15")
    elif len(data) > 50:
        raise Exception(f"csv file has to many rows: {len(data)} > 50")
    else:
        print("data read successfully")
        return data

def fileReader(fileName:str):
    try:
        outputFile = []
        _, extention = os.path.splitext(fileName)
        if(extention == ".txt"):
            with open(fileName, "r") as textFile:
                outputFile = textFileProcesser(textFile)
                textFile.close()
                return outputFile
        elif(extention == ".csv"):
            with open(fileName, "r") as csvFile:
                outputFile = csvFileProcesser(csvFile)
                csvFile.close()
                return outputFile
        else:
            if extention == "":
                raise Exception("no extention given")
            else:
                raise Exception(f"{extention} is not a file type that can be read")
    except NameError:
        raise Exception(f"{fileName} was not found within directory")

if __name__ == "__main__":
    fileToRead = "MBA_good.csv"
    read = fileReader(f"/Users/davidzhao/Dev/CodingQuestions/general/test_files/{fileToRead}")
    print(read)