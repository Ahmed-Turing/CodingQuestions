import task1 as fileToArray
import csv
import os

def textFileProcesser(textFile):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    inArray = list(textFile.read())
    for word in inArray:
        for char in word:
            if char in punc:
                word = word.replace(char, "")
    data = fileToArray.ArrayHandler(inArray)
    return data.array

def csvFileProcesser(csvFile):
    data = []
    keys = []
    csvReader = csv.reader(csvFile)
    keys = csvReader.readline()
    if "application_id" in keys:
        csvDictReader = csv.DictReader(csvFile)
        for row in csvDictReader:
            data.append(row)
    elif "application_id" not in keys:
        raise Exception("no key for application_id found")
    else:
        raise Exception("error when reading csv file")
    return data

def binaryFileProcesser(binaryFile):
    inArray = []
    for i in binaryFile:
        pass
    
def fileReader(fileName):
    try:
        _, extention = os.path.splitext(fileName)
        if(extention == ".txt"):
            with open(fileName, "r") as textFile:
                textFileProcesser(textFile)
                textFile.close()
        elif(extention == ".csv"):
            with open(fileName, "r") as csvFile:
                csvFileProcesser(csvFile)
                csvFile.close()
        elif(extention == ".bin" or extention == ".dat"):
            with open(fileName, "rb") as binaryFile:
                binaryFileProcesser(binaryFile)
                binaryFile.close()


    except NameError:
        raise Exception(f"'{fileName}' cannot be found within directory")
