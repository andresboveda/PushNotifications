#!/usr/bin/python3.8

#Create custom push notifications using the Pushsafer API
#In this example we will scrape the Coindesk website and notify us if the price of our crypto meets certain conditions.

import urllib3
urllib3.disable_warnings()
import requests, bs4, re

res = requests.get('https://www.coindesk.com/price/ethereum')
res.raise_for_status()
ethSoup = bs4.BeautifulSoup(res.text, 'html.parser')
ethList = ethSoup.find_all("div", attrs={"class": "price-large"})
ethPrice = [el.text for el in ethList]
ethString = ' '.join([str(elem) for elem in ethPrice])
ethClean = ethString.replace(',','')
ethFloat = float(ethClean.replace('$',''))
print("The price of ETHEREUM is {}".format(ethFloat))

res4 = requests.get('https://www.coindesk.com/price/cardano')
res4.raise_for_status()
adaSoup = bs4.BeautifulSoup(res4.text, 'html.parser')
adaList = adaSoup.find_all("div", attrs={"class": "price-large"})
adaPrice = [el.text for el in adaList]
adaString = ' '.join([str(elem) for elem in adaPrice])
adaClean = adaString.replace(',','')
adaFloat = float(adaClean.replace('$',''))
print("The price of Cardano ADA is {}".format(adaFloat))


res2 = requests.get('https://www.coindesk.com/price/tron')
res2.raise_for_status()
tronSoup = bs4.BeautifulSoup(res2.text, 'html.parser')
tronList = tronSoup.find_all("div", attrs={"class": "price-large"})
tronPrice = [el.text for el in tronList]
tronString = ' '.join([str(elem) for elem in tronPrice])
tronClean = tronString.replace(',','')
tronFloat = float(tronClean.replace('$',''))
print("The price of TRX is {}".format(tronFloat))

res3 = requests.get('https://www.coindesk.com/price/iota')
res3.raise_for_status()
iotaSoup = bs4.BeautifulSoup(res3.text, 'html.parser')
iotaList = iotaSoup.find_all("div", attrs={"class": "price-large"})
iotaPrice = [el.text for el in iotaList]
iotaString = ' '.join([str(elem) for elem in iotaPrice])
iotaClean = iotaString.replace(',','')
iotaFloat = float(iotaClean.replace('$',''))
print("The price of IOTA is {}".format(iotaFloat))

from pushsafer import init, Client

if ethFloat > 5000:
    init('INSERT PUSHSAFER CLIENT KEY')
    Client("").send_message("Ethereum goes over $5000", "Ethereum!", "INSERT PUSHSAFER DEVICE NUMBER", "1", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "600", "60", "1", "", "", "")
    print("A push notification for Ethereum will be sent now")

if tronFloat > 0.5:
    init('INSERT PUSHSAFER CLIENT KEY')
    Client("").send_message("Tron TRX goes over $0.5", "TRX Coin!", "INSERT PUSHSAFER DEVICE NUMBER", "1", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "600", "60", "1", "", "", "")
    print("A push notification for Tron TRX will be sent now")

if iotaFloat > 5:
    init('INSERT PUSHSAFER CLIENT KEY')
    Client("").send_message("IOTA goes over $5", "IOTA Coin!", "INSERT PUSHSAFER DEVICE NUMBER", "1", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "600", "60", "1", "", "", "")
    print("A push notification for IOTA will be sent now")

if adaFloat > 5:
    init('INSERT PUSHSAFER CLIENT KEY')
    Client("").send_message("Cardano ADA goes over $5", "ADA Coin!", "INSERT PUSHSAFER DEVICE NUMBER", "1", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "600", "60", "1", "", "", "")
    print("A push notification for ADA will be sent now")



