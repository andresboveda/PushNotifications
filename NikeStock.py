#!/usr/bin/python3.8

#Customized push notification on the Nike stock using the Pushsafer API


import urllib3
urllib3.disable_warnings()
import requests, bs4, re

res = requests.get('https://finance.yahoo.com/quote/NKE/')
res.raise_for_status()
nikeSoup = bs4.BeautifulSoup(res.text, 'html.parser')
nikePrice = nikeSoup.select('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)')
nikePrice = [el.text for el in nikePrice]
nikeFloat = float(nikePrice[0])

from pushsafer import init, Client

if nikeFloat > 150:
    init('INSERT CLIENT KEY')
    Client("").send_message("Nike goes over $150", "Nike Stock", "INSERT DEVICE NUMBER ON PUSHSAFER", "1", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "600", "60", "1", "", "", "")
    print("Nike goes over 150. A push notification for Nike stock will be sent now")
else:
    print("Nike stock is at ${} and is not over $150, so no push will be sent.".format(nikeFloat))



