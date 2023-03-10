from selenium import webdriver
from bs4 import BeautifulSoup
import time


def scrap_url(url,load_time):
    #Change local address for chromedriver
    driver = webdriver.Chrome('/WebScrapper/chromedriver 2')
    driver.get(url)
    time.sleep(load_time)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    link = []

    product_list = soup.find_all("div",{"class":"pip-product-compact"})

    for product in product_list:
        anchor = product.find("a")
        link.append(anchor["href"])

    # Print product numbers
    print("Number of products: ",len(link))

    return link
    