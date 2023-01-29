import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
from datetime import datetime

def get_article_content(url, DEBUG):
    #   Prepare tools and init lib functions
    driver = webdriver.Firefox()
    soup = BeautifulSoup(source_code, "lxml")

    #   Prepare dataholders
    full_webcontent = []
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    """
    #   Preload webpage sourcecode
    driver.get(url)
    source_code = driver.page_source


    #   DEBUG/TEST CODE
    #   Traverse and open up source code
    #   Look for code tags of:
    #       "span"
    #       "style"
    #       "script"
    #       "a"

    """
    with open("./104.html", "r", encoding="utf-8") as f:
        lastest_scan = f.read()
    for data in soup(["span", "style", "script", "a"]):
        data.decompose()
    print(soup)
    """

    #   Search for all link and context tags, as well as meta tags
    #       (comes in handy for decoding webcontent into correct charset)
    source_log = soup.find_all(["h1", "h2", "h3", "href", "p", "meta"])

    #   Iterate through individual lines of HTML code
    for context in source_log:
        #   If line in source code does not have any code:
        if len(context.contents) != 0:
            #   Merge empty lines and 
            print(' '.join(soup.stripped_strings))
            full_webcontent.append(context.contents)

        if DEBUG == True:
            source_encoding = str(context).split('"')[-2]
            if "charset" in str(context):
                print(f"Page Encoding {source_encoding}")

    if DEBUG == True:
        print(full_webcontent)

    for i, line in enumerate(full_webcontent):
        try:
            full_webcontent[i] = line.decompose()
            if DEBUG == True:
                print("decomposed")
        except:
            pass

    log_time = datetime.now().strftime("%S-%M-%H-%d-%Y")
    with open(f"./104/{log_time}.txt", "w", encoding="utf-8") as save:
        for line in full_webcontent:
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