import newspaper
from newspaper import Article

articleurl = 'http://www.mining.com/copper-price-felled-chinese-factory-reading-drops-5-years/'
siteurl = 'http://www.mining.com/'

def parseurl(url):
    article = Article(url)
    article.download()
    article.parse()
    return article


def getkeywords(url):
    article = parseurl(url)
    article.nlp()
    keywords = article.keywords
    return keywords

# mine_paper = newspaper.build(siteurl)
# print(mine_paper.size())