#!/usr/bin/python3.8

#Script that will send us a push notification when there's a price drop on an Amazon product.
#Using the Pushsafer API. 

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = 'https://www.amazon.es/dp/B000CZ0R42/ref=s9_acsd_simh_bw_c2_x_0_i?pf_rd_m=A1AT7YVPFBWXBL&pf_rd_s=merchandised-search-2&pf_rd_r=BG1WKYQVHWC51A9690R9&pf_rd_t=101&pf_rd_p=4df180d1-91d4-44a7-a03c-6a5bca960827&pf_rd_i=4965354031'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})

webpage = urlopen(req).read()
page_soup = soup(webpage, 'html.parser')
smList = page_soup.select('#price_inside_buybox')
smPrice = [el.text for el in smList]
smPrice = smPrice[0]
smNum = smPrice.replace('€','')
smFloat = float(smNum.replace(',','.'))

from pushsafer import init, Client

if smFloat < 98: #price that it's currently at
    init('INSERT CLIENT KEY')
    Client("").send_message("The item you want is now cheaper", "Amazon Price Drop", "INSERT DEVICE NUMBER ON PUSHSAFER", "1", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "600", "60", "1", "", "", "")
    print("Price drop! A push notification will be sent now.")
else:
    print("Price has not dropped, so no push will be sent.".format(nikeFloat))




