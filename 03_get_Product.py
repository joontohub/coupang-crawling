from stringGetter   import getPageString
from bs4            import BeautifulSoup
from productsParser import getProducts
from download_excel import moveExcel

url = "https://www.coupang.com/np/categories/328436?page=2"
pageString = getPageString(url)
for i in range(0,60):
    moveExcel(getProducts(pageString,i),i)
