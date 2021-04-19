import requests
import threading
from queue import Queue
import json
import time
from bs4 import BeautifulSoup
from discordwebhook import Discord
from lxml import html
from datetime import date
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import random
import sys

'''
#not really used currently
def initWebhook(status, title):


     #Import starting webhook template from file
    with open('./webhookContent.json') as f:
        data = json.load(f)

    #Loop to input each product's info
    productCount = len(title)
    for i in range(0,productCount):
        
        data["embeds"][0]["fields"][i]["name"] = title[i].text.strip()

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
        x = "Status {}\nLast Updated: {}\n".format(status[i].text.strip(), dt_string)
        data["embeds"][0]["fields"][i]["value"] = x

    
    #Webhook URL
    url = "https://discord.com/api/webhooks/829186101670576168/2zFk-jxf6Ht1v9euKxCnk5UsLkCW7dOVPlCuEABrIYENPGpD0WahmwmEyRFSGy8joDTz"

    #POST Request sending JSON data
    payload = json.dumps(data)
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "68f3c9c9-d5c4-9071-8e1f-437cd031f64f"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

    with open('./webhookContent.json', "w") as f:
        json.dump(data,f)

#updates last time items were checked
def updateWebhook(curTitle, curStatus):


    with open('./webhookContent.json') as f:
        data = json.load(f)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
    
    for i in range(0,len(curTitle)):
        data["embeds"][0]["fields"][i]["name"] == curTitle[i]
        x = "Status {}\nLast Updated: {}\n".format(curStatus[i], dt_string)
        data["embeds"][0]["fields"][i]["value"] = x

    url = "https://discord.com/api/webhooks/829186101670576168/2zFk-jxf6Ht1v9euKxCnk5UsLkCW7dOVPlCuEABrIYENPGpD0WahmwmEyRFSGy8joDTz/messages/831746068625752084"

    payload = json.dumps(data)
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "33f0d6d9-abe1-f1eb-97a5-2bcc32e80323"
        }

    requests.request("PATCH", url, data=payload, headers=headers)
    #print(response.request.body)

    #saves info to file
    with open('./webhookContent.json', "w") as f:
        json.dump(data,f)

#unneccesary?
def revisedTask(proxies, inStockList):
    startTime = time.time()
    seconds = 60
    inStockProd = inStockList
    x = -1

    while x < 1:
        currentTime = time.time()
        elapsedTime = currentTime - startTime

        if elapsedTime > seconds:
            print("Returning to normal")
            x = 1
            task(proxies)
        else:

            proxy = random.choice(proxies)
            print("Proxy: {}".format(proxy))
            #get all products and their info 
            status, title = dataPull(proxy)

            #removing all previously used items

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
            print(dt_string)

            for i in range(0,len(title)):
                title[i] = title[i].text.strip()
                status[i] = status[i].text.strip()


                if (status[i] != "Out of Stock") and (title[i] not in inStockProd):
                    inStockWebhook(title[i], status[i])
                    time.sleep(1)

                    inStockProd.append(title[i])
                    print(inStockProd)
                    revisedTask(proxies, inStockProd)

                if (title[i] in inStockProd) and (status[i] == "Out of Stock"):
                    inStockProd.remove(title[i])
'''

#todo, will send a webhook that pings when an item is in stock
def inStockWebhook(productTitle, productStatus):
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")

    #Import starting webhook template from file
    with open('./inStock.json') as f:
        data = json.load(f)

    #product's title
    data["embeds"][0]["fields"][0]["name"] = productTitle
    
    #status string 
    x = "Status: {}\nLast Updated: {}\n".format(productStatus, dt_string)
    data["embeds"][0]["fields"][0]["value"] = x
    
    #loop for image
    if (productTitle == "AMD Radeon™ RX 6900 XT Graphics"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/663934-amd-radeon-rx-6900xt-box-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5458372200/us?add-to-cart=true"

    elif (productTitle == "AMD Radeon™ RX 6800 XT Graphics"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/663934-amd-radeon-rx-6800xt-box-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5458372800/us?add-to-cart=true"

    elif (productTitle == "AMD Radeon™ RX 6800 Graphics"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/663934-amd-radeon-rx-6800-box-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5458373400/us?add-to-cart=true"

    elif (productTitle == "AMD Radeon™ RX 6700 XT Graphics"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/758188-amd-radeon-rx-6700xt-box-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5496921400/us?add-to-cart=true"

    elif (productTitle == "AMD Radeon™ RX 6800 XT Midnight Black Graphics Card"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/762922-amd-radeon-rx-6800xt-black-box-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5496921500/us?add-to-cart=true"

    elif (productTitle == "AMD Ryzen™ 9 3950X Desktop Processor"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/thumbnail/19239710-A_RYZEN9__COMP_RF_ROW_100x85.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5358857400/us?add-to-cart=true"

    elif (productTitle == "AMD Ryzen™ 9 3900X Desktop Processor"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/thumbnail/19239710-A_RYZEN9__COMP_RF_ROW_100x85.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5335621300/us?add-to-cart=true"
        
    elif (productTitle == "AMD RYZEN™ 9 5950X Processor"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/amd-ryzen-9-5950x-PIB-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5450881400/us?add-to-cart=true"

    elif (productTitle == "AMD RYZEN™ 7 5800X Processor"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://computerage.lk/wp-content/uploads/2020/12/5800x-1.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5450881600/us?add-to-cart=true"

    elif (productTitle == "AMD RYZEN™ 9 5900X Processor"): 
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/amd-ryzen-9-5900x-PIB-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5450881500/us?add-to-cart=true"

    elif (productTitle == "AMD RYZEN™ 5 5600X Processor"):
        data["embeds"][0]["thumbnail"]["url"] = "https://drh1.img.digitalriver.com/DRHM/Storefront/Company/amd/images/product/detail/amd-ryzen-5-5600x-PIB-fan-1260x709.png"
        data["embeds"][0]["url"] = "https://www.amd.com/en/direct-buy/5450881700/us?add-to-cart=true"
    else:
        print("You're fucked")



    #Webhook URL
    url = "https://discord.com/api/webhooks/829186101670576168/2zFk-jxf6Ht1v9euKxCnk5UsLkCW7dOVPlCuEABrIYENPGpD0WahmwmEyRFSGy8joDTz"

    #POST Request sending JSON data
    payload = json.dumps(data)
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "68f3c9c9-d5c4-9071-8e1f-437cd031f64f"
        }

    requests.request("POST", url, data=payload, headers=headers)
    #print(response.text)

#retrieves current status of each product on page
def dataPull(proxy):

    test = {
        "http": proxy, 
        "https": proxy
        }

    url = "https://www.amd.com/en/direct-buy/us"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
        "Referer": "https://www.amd.com/",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0"
    }

    page = requests.get(url, headers=headers, proxies=test)

    #prints 200 if the response went through successfully
    #print(page)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='block-amd-content')

    status = results.find_all('div', class_='shop-links')
    title = results.find_all('div', class_='shop-title')

    return status, title

#essentially main; put in a seperate function for possible threading in the future
def task(proxies, inStockProd):

    #todo?
    #picks a random proxy from the list, could be refined
    proxy = random.choice(proxies)
    print("Proxy: {}".format(proxy))
    #get all products and their info 
    status, title = dataPull(proxy)

    #fetches the date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
    print(dt_string)

    #loops through every product and checks if the item is in stock
    for i in range(0,len(title)):
        title[i] = title[i].text.strip()
        status[i] = status[i].text.strip()

        #checks that the product is in stock and has not been in stock before
        if (status[i] != "Out of Stock") and (title[i] not in inStockProd):
            inStockWebhook(title[i], status[i])
            time.sleep(1)

            inStockProd.append(title[i])
            print(inStockProd)
            task(proxies, inStockProd)

        #if the item was in stock, and is now OOS, removes from the list
        if (title[i] in inStockProd) and (status[i] == "Out of Stock"):
            inStockProd.remove(title[i])


def main():

    with open ('proxies.txt', 'r+') as f:
        proxies = [line.strip() for line in f]   

    inStockProd = []
    
    for i in range(200):
        x = threading.Thread(target=task(proxies, inStockProd), args=(i,), daemon=True)
        x.start()

if __name__ == "__main__":
    main()
