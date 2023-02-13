from scrap_url import scrap_url
from scrap_product import scrap_product
import csv

##Inital Setting
#Before Start, go to scrap_url.py and change local address for chromedriver

#URL LOADTIME -> Time needed to wait until all products are loaded
url_loadtime = 5

#ITERATION NUM -> Number of products that are scrapped for each URLS
iteration_num = 2000

#URLS -> URL for scrapping; each URLs needs to have all products in its page, therefore change "?page" num to approporiate number(ex.200).
urls = ["https://www.ikea.com/kr/ko/cat/lamps-li002/?filters=f-subcategories%3A20515%7C10731%7C10732%7C20502&page=100","https://www.ikea.com/kr/ko/cat/sofas-armchairs-fu003/?filters=f-measurement-buckets%3AWIDTH_50_100%7CWIDTH_100_150%7CWIDTH_150_200%7CDEPTH_80_90%7CDEPTH_90_100%2Cf-seats%3A38827%7C38767%7C38768%2Cf-subcategories%3A10661%7C16238%7C10663%7C10662&page=2","https://www.ikea.com/kr/ko/cat/cabinets-cupboards-st003/?filters=f-measurement-buckets%3AWIDTH_20_40%7CWIDTH_40_60%7CWIDTH_60_80%2Cf-subcategories%3A10412%7C10409%7C10385&page=4","https://www.ikea.com/kr/ko/cat/chests-of-drawers-drawer-units-st004/?filters=f-measurement-buckets%3AHEIGHT_40_60%7CHEIGHT_60_80%7CHEIGHT_80_100%2Cf-subcategories%3A10451%7C20656%7C10711%7C46081&page=20","https://www.ikea.com/kr/ko/cat/rugs-10653/?filters=f-measurement-buckets%3AWIDTH_50_100%7CWIDTH_100_150%2Cf-subcategories%3A10692%7C10689%7C39267&page=10","https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=f-measurement-buckets%3AWIDTH_20_40%7CWIDTH_40_60%7CWIDTH_60_80%7CLENGTH_50_100%2Cf-subcategories%3A20649%7C10705%7C21825&page=10","https://www.ikea.com/kr/ko/cat/beds-bm003/?filters=f-subcategories%3A16285%2Cf-typed-reference-measurement%3A80x200%20cm_bed%20frames%7C90x200%20cm_bed%20frames&page=30","https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=f-subcategories%3A25219%7C19144&page=60","https://www.ikea.com/kr/ko/cat/wardrobes-19053/?filters=f-measurement-buckets%3AHEIGHT_0_100%7CHEIGHT_100_150%7CHEIGHT_150_200%2Cf-subcategories%3A43634%7C48005%7C43631"]

#URL NAMES -> Name of csv files for each URLs
url_names = ["lamp","shofa","cabinet","drawer","rug","table","bed","chair","wardrobe"]

##Scrapping
for i, url in enumerate(urls):
    #Scrap Product URL from Category URL

    url_list = scrap_url(url,url_loadtime)

    #Scrap Product Details from Product URL
    product_list = scrap_product(url_list,iteration_num)

    #Save product list-dictionary to CSV file
    keys = product_list[0].keys()
    text = url_names[i] + '.csv'
    a_file = open(text, "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(product_list)
    a_file.close()
    print("-> Product Catalogue Saved as " + url_names[i] + ".csv")