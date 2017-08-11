#adapted from MechanicalSoup example.py

from __future__ import print_function
import mechanicalsoup

def getPFIpage(url):
    username = "cchen"
    password = "btmuu"

    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'html.parser'},
        # raise_on_404=True
    )

    browser.open("http://www.pfie.com/sign-in") #pfi sign in page
    browser.select_form('#signonform')
    browser["username"] = username
    browser["passWord"] = password
    browser.submit_selected()

    browser.open(url)
    page = browser.get_current_page()

    return page

def getSEAandWriteHTML():
    # SEA URL http://www.pfie.com/asia-pacific/southeast-asia/
    # Indonesia URL http://www.pfie.com/search?saddfilter|wvcategory=21098/21527/21536

    soup = getPFIpage("http://www.pfie.com/asia-pacific/southeast-asia/")
    links = soup.find(id="content").find_all("a")

    # print(links)

    with open("msg.html", "w") as text_file:
        for link in links:
            text_file.write(link.prettify())
            text_file.write("<br>")

    return

