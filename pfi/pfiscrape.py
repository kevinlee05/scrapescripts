#adapted from MechanicalSoup example.py
from __future__ import print_function
import mechanicalsoup
from passwords import PFILOGIN, PFIPASS



def getPFIpage(url):
    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'html.parser'},
        # raise_on_404=True
    )

    # browser.open("http://www.pfie.com/sign-in") #pfi sign in page
    # browser.select_form('#signonform')
    # browser["username"] = PFILOGIN
    # browser["passWord"] = PFIPASS
    # browser.submit_selected()

    browser.open(url)
    page = browser.get_current_page()

    return page

def getURLandWriteHTML(url, writemode):
    soup = getPFIpage(url)
    links = soup.find(id="content").find_all("a")

    # print(links)

    with open("msg.html", writemode) as text_file:
        for link in links:
            text_file.write(link.prettify())
            text_file.write("<br>")


    return

