import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
from datetime import datetime

def get_article_content(url, DEBUG):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    full_context = []

    driver = webdriver.Firefox()
    driver.get(url)

    source_code = driver.page_source


    #with open("./104.html", "r", encoding="utf-8") as f:
    #    lastest_scan = f.read()

    soup = BeautifulSoup(source_code, "lxml")

    for data in soup(["span", "style", "script", "a"]):
        data.decompose()
    #print(soup)
    source_log = soup.find_all(["h1", "h2", "h3", "href", "p", "meta"])
    for context in source_log:

        if len(context.contents) != 0:
            print(' '.join(soup.stripped_strings))
            full_context.append(context.contents)

        if DEBUG == True:
            source_encoding = str(context).split('"')[-2]
            if "charset" in str(context):
                print(f"Page Encoding {source_encoding}")

    if DEBUG == True:
        print(full_context)

    for i, line in enumerate(full_context):
        try:
            full_context[i] = line.decompose()
            if DEBUG == True:
                print("decomposed")
        except:
            pass

    log_time = datetime.now().strftime("%S-%M-%H-%d-%Y")
    with open(f"./104/{log_time}.txt", "w", encoding="utf-8") as save:
        for line in full_context:
            try:
                save.write(f"{line[0]}\n")
            except:
                save.write(f"{str(line[0].contents)}\n")

    if DEBUG == True:
        print(type(source_code))

def main():
    url = "https://www.104.com.tw/info/privacy"
    get_article_content(url, DEBUG = False)

if __name__ == "__main__":
    main()
    exit()