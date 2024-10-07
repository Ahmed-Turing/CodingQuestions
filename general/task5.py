#assume array is a block of text, and the sign for next page is some string or int
#assume sign for page is ^p and 
#can also assume one page is capped at 500 words if no marker is created
import task3 as fileHandler

def createPages(toPages:list):
    pageCounter = 1;
    page = {
        f"page {pageCounter}": []
    }
    for word in toPages:
        currentPage = page[f"page {pageCounter}"]
        if word != "^p":
            currentPage.append(word)
        elif word == "^p":
            pageCounter += 1
            page[f"page {pageCounter}"] = []
        elif len(currentPage) == 500:
            pageCounter += 1
            page[f"page {pageCounter}"] = []
        else:
            raise Exception("Error making pages for document")
    return page
        
if __name__ == "__main__":
    textFile = fileHandler.fileReader("/Users/davidzhao/Dev/CodingQuestions/general/test_files/pagesTest.txt")
    pages = createPages(textFile.array)
    print(pages["page 2"])