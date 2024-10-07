from task4 import stringFindAll

def showPages(pageArray:list, pageIndex:int, pageSize:int):
    '''
        pageArray is array of pages
        pageIndex is the index of the page of interest
        pageSize is the amount of characters in a line
    '''

    page = pageArray[pageIndex]
    page = page.replace('\n', " ")
    newChars = pageSize
    spacesArray = stringFindAll(page, " ")
    #must cast as list because python string is immutable
    page = list(page)

    for i, space in enumerate(spacesArray):
        if i + 1 < len(spacesArray):
            #make a new line in the next space when we are above the amount of characters, making the text the size of the page
            if spacesArray[i + 1] > newChars:
                page[space] = '\n'
                newChars = space + pageSize
    page = "".join(page)
    return page

def test_task5():
    textFile= "general/test_files/pagesTest.txt"
    with open(textFile) as pages:
        pageArray = pages.read().split("^p")
        pages.close()
    pageIndex = 2
    pageSize = 20
    print(showPages(pageArray, pageIndex, pageSize))


if __name__ == "__main__":
    test_task5()