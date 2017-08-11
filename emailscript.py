import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def readFileAndSend():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'PFI News'
    msg['From'] = 'me'
    msg['To'] = 'kevin.lee@ca-cib.com'


    text = "this is your daily PFI update:"
    html = ""

    with open("msg.html") as file:
        html = file.read()

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # send message and quit
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("inspir3d@gmail.com","rrrpn@24")
    server.send_message(msg)
    server.quit()