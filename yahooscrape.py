from bs4 import BeautifulSoup
import time
# import urllib.request
from urllib.request import urlopen

def getStockURL(quote, urltype):

    baseStringURL = "https://sg.finance.yahoo.com/quote/"
    summaryURL = "?p="
    statisticsURL = "/key-statistics?p="
    financialsURL = "/financials?p=" #income statement
    balanceSheetURL = "/balance-sheet?p="
    cashflowURL = "/cash-flow?p="
    profileURL = "/profile?p="

    switcher = {
        "summary": baseStringURL + quote + summaryURL + quote,
        "statistics": baseStringURL + quote + statisticsURL + quote,
        "income": baseStringURL + quote + financialsURL + quote,
        "balancesheet": baseStringURL + quote + balanceSheetURL + quote,
        "cashflow": baseStringURL + quote + cashflowURL + quote,
        "profileURL": baseStringURL + quote + profileURL + quote,
    }

    return switcher.get(urltype, "na")

def stockHTMLcode(quote, urltype):

    sourceCode = urlopen(getStockURL(quote, urltype))

    return sourceCode

#dictionary of key stats
keyStats = {}

def getSouped(quote, urltype):
    soup = BeautifulSoup(stockHTMLcode(quote, urltype), "html.parser")
    return soup
# print(soup.table.prettify())

# printTables("C61U.SI", "statistics")

def printStatistics(quote):
    soup = getSouped(quote, "statistics")
    tables = soup.find_all(attrs={"class":"table-qsp-stats Mt(10px)"})

    dataArray = {}

    for table in tables:
        for row in table.find_all("tr"):
            keyText = row.find_all("td")[0].find_all(text=True)[0]
            dataArray[keyText] = row.find_all("td")[1].get_text()

 # ''.join(text for text in p.find_all(text=True) if text.parent.name != "a")

    for key in dataArray:
        print(key + " : " + dataArray[key])

    print("total number of items = " + str(len(dataArray)))

    return

printStatistics("C61U.SI")




