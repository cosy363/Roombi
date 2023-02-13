import httpx
from bs4 import BeautifulSoup
from selenium import webdriver


def scrap_product(url_list,iteration_num):
    product_list = []
    n = iteration_num
    for product_url in url_list:
        if n == 0:
            break
        n = n - 1
        product_html = httpx.get(product_url)
        soup = BeautifulSoup(product_html.content, 'html.parser')

        product_dict = {}
        # Product Name
        product_name = (soup.find("span",{"class":"pip-header-section__title--big notranslate"})).text
        product_dict['Name'] = product_name

        # Product Price
        main_product = soup.find("div",{"class":"pip-temp-price-module__price"})
        product_price = (main_product.find("span",{"class":"pip-temp-price__integer"})).text
        product_dict['Price'] = product_price

        # Product Category & Color(Material)
        str = (soup.find("span",{"class":"pip-header-section__description-text"})).text
        str_split = str.split(',')
        try:
            product_category = str_split[0]
            product_dict['Category'] = product_category
        except:
            product_dict['Category'] = "No Category"  
            print("No category error occured") 

        try:
            product_color = str_split[1]
            product_dict['Color'] = product_color
        except:
            product_dict['Color'] = "No Color"  
            print("No Color error occured") 

        # Product Size
        try : 
            product_size = (soup.find("button",{"class":"pip-link-button pip-header-section__description-measurement js-measurement-link"})).text
            product_dict['Size'] = product_size
        except :
            product_dict['Size'] = "No Size"
            print("Nonetype error occured") 


        # Product Rating and Number of Reviews
        try:
            product_review = soup.find("button",{"class":"pip-average-rating pip-average-rating__button"})
            product_review_str = product_review['aria-label']
            str_split_2 = product_review_str.split('총 리뷰: ')
            str_split_2[0] = (str_split_2[0].split(': '))[1]
            str_split_2[0] = (str_split_2[0].split(' /'))[0]
            product_rating = str_split_2[0]
            product_reviewnum = str_split_2[1]
            product_dict['Rating'] = product_rating
            product_dict['Reviews'] = product_reviewnum
        except:
            product_dict['Rating'] = "No Review"
            product_dict['Reviews'] = "No Review"
            print("No Review Item occured")
        
        # Product URL & Image URL
        media_grid = soup.find("div",{"class":"pip-media-grid__media-container"})
        product_dict['URL'] = product_url

        try:
            product_image_url = (media_grid.find("img",{"class":"pip-aspect-ratio-image__image"})).get('src')
            product_dict['Image URL'] = product_image_url
        except:
            product_dict['Image URL'] = "No Product Image"

        # Product Number
        number_grid = soup.find("div",{"class":"pip-product__subgrid product-pip js-product-pip"}).get('data-product-no')
        product_dict['Product Number'] = number_grid

        # Return List of Dictionary of product
        product_list.append(product_dict)

    return product_list





