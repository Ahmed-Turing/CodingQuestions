import task1 as fileToArray
import csv
import os

def textFileProcesser(textFile:str):
    punc = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
    inArray = textFile.read().split()
    try:
        for i in range(len(inArray)):
            if inArray[i] != "n/a":
                inArray[i] = int(inArray[i])
    except Exception as e:
        for word in inArray:
            for char in word:
                if char in punc and word != "n/a" and word != "^p":
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
    except FileNotFoundError:
        raise Exception(f"{fileName} was not found within directory")

def test_task3():
    flies = {
        "txtFile" : "general/test_files/alice_in_wonderland.txt",
        "goodCsv" : "general/test_files/MBA_good.csv",
        "noIdCsv" : "general/test_files/MBA_missing_id.csv",
        "tooLongCsv" : "general/test_files/MBA_too_long.csv",
        "tooShortCsv" : "general/test_files/MBA_too_short.csv",
        "numberTxtFile" : "general/test_files/numbers.txt",
        "badFileName" : "general/test_files/does_not_exist.txt",
        "noExtention" : "general/test_files/bad_extention_1",
        "WrongExtention" : "general/test_files/bad_extention_2.dat",
    }
    for key, value in flies.items():
        match key:
            case "noIdCsv":
                try:
                    fileReader(value)
                except Exception as e:
                    if str(e) == "no key for application_id found":
                        print("no id error handling is correct")
                    else:
                        print(e)
            case "tooLongCsv":
                try:
                    fileReader(value)
                except Exception as e:
                    if str(e) == "csv file has to many rows: 74 > 50":
                        print("csv file too long error handling is correct")
                    else:
                        print(e)
            case "tooShortCsv":
                try:
                    fileReader(value)
                except Exception as e:
                    if str(e) == "csv file has to little rows: 8 < 15":
                        print("csv file too short error handling is correct")
                    else:
                        print(e)
            case "badFileName":
                try:
                    fileReader(value)
                except Exception as e:
                    if str(e) == "general/test_files/does_not_exist.txt was not found within directory":
                        print("file not found error handling is correct")
                    else:
                        print(e)
            case "noExtention":
                try:
                    fileReader(value)
                except Exception as e:
                    if str(e) == "no extention given":
                        print("no extention error handling is correct")
                    else:
                        print(e)
            case "WrongExtention":
                try:
                    fileReader(value)
                except Exception as e:
                    if str(e) == ".dat is not a file type that can be read":
                        print("invalid extention error handling is correct")
                    else:
                        print(e)
            case _:
                fileReader(value)
                print(f"{key} run successful")

if __name__ == "__main__":
    test_task3()



