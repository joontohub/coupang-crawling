from stringGetter import getPageString
from bs4 import BeautifulSoup


def getProduct(li):
    img = li.find("dt", {"class":"image"}).find("img")
    name = img['alt']
    price = 0
    priceWrap = li.find("div", {"class":"price-wrap"})
    strong = priceWrap.find("strong")
    price = strong.text
    a = li.find("a", {"class":"baby-product-link"})
    link = a['href']
    website = "www.coupang.com" + link
    #print(website)

    try:
        ex_price = priceWrap.find("del").text
        #print(name , price, ex_price)
        return {"name":img['alt'], "price":strong.text , "ex_price":ex_price , "website":website}
    except:
        #print(name , price)
        return {"name":img['alt'], "price":strong.text , "ex_price":"None" , "website":website}

def getProducts(string , number):
    bsObj = BeautifulSoup(string, "html.parser")

    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    li = lis[number]
    return getProduct(li)
