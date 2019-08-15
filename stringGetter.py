import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
    }

def getPageString(url):
    data = requests.get(url , headers = headers)
    bsObj = BeautifulSoup(data.content, "html.parser")


    return data.content
