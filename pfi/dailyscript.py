from pfiscrape import getURLandWriteHTML
from emailscript import readFileAndSend

SEAurl = "http://www.pfie.com/asia-pacific/southeast-asia/"
CHINAurl = "http://www.pfie.com/asia-pacific/china-and-east-asia/"
INDIAurl = "http://www.pfie.com/asia-pacific/india-and-south-asia/"
INDOurl = "http://www.pfie.com/search?saddfilter|wvcategory=21098/21527/21536"

with open("msg.html", "w") as tf:
    tf.write("<h2>SouthEast Asia</h2>")

getURLandWriteHTML(SEAurl, "a")

with open("msg.html", "a") as tf:
    tf.write("<br><h2>China</h2>")

getURLandWriteHTML(CHINAurl, "a")

with open("msg.html", "a") as tf:
    tf.write("<br><h2>India</h2>")

getURLandWriteHTML(INDIAurl, "a")

readFileAndSend()

