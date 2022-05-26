from cmath import exp
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html_to_json
import os
import json

def scrap():
    # Save page
    #url = 'www.komplett.no/category/11158/datautstyr/skjermer/skjermer?nlevel=10000%C2%A710392%C2%A711158&hits=264'
    url = 'www.komplett.no/category/21635/gaming/gaming-utstyr/gaming-tastatur?nlevel=10431%C2%A721603%C2%A721635&hits=168'
    key = '1783319260d70f84da21868ce0fd6207'
    api_link = f"http://api.scraperapi.com?api_key={key}&url={url}"

    page=urlopen(api_link)
    # Read data on page
    html_bytes=page.read()
    # Decode data from page
    html=html_bytes.decode("utf-8")

    # Write html file from data scrapped
    with open("komplett/tastatur.html","w",encoding="utf-8")as html_file:
        html_file.write(html)

def read_skjerm():    
    # Read html file from scrapped data
    with open("komplett/tastatur.html","r",encoding='utf-8')as html_file:
        output=html_file.read()
        
        soup = BeautifulSoup(output, 'lxml')
        screens = soup.find_all('div', class_ = 'product-list-item subscription-price-visible')
        screen_dict = {}
        all_screens = []
        for screen in screens:
            screen_name = screen.h2.text
            screen_stats = screen.p.text.split()
            screen_available = screen.find('div', class_='stockstatus').text.split('\n')[3].split(' ')[0]
            if screen_available == "Ikke":
                screen_available = 0
            screen_itemnumber = screen.find('div', class_='product-data').text.replace(' ', '').replace('\n', '').split('/')[0].split(':')[1]
            screen_price = screen.find('div', class_='product-price').text.replace(',-', '').replace('NÅ', '').replace('\n','')
            screen_link = "komplett.no{}".format(str(screen.find('div', class_='buy-button align-right')).split()[7].split('"')[1])

            print(f'Screen: {screen_name}')
            print(f'\tPrice: {screen_price}')
            print(f'\tStats: {screen_stats}')
            print(f'\tAvailable: {screen_available}')
            print(f'\tLink: {screen_link}')
            
def read_tastatur():    
    # Read html file from scrapped data
    with open("komplett/tastatur.html","r",encoding='utf-8')as html_file:
        output=html_file.read()
        
        soup = BeautifulSoup(output, 'lxml')
        screens = soup.find('div', class_ = 'product-list-item')
        screen_dict = {}
        all_screens = []
        for screen in screens:
            screen_image = screen.find("image-wrapper ")
            print(screen_image)
            # screen_name = screen.h2.text
            # screen_stats = screen.p.text.replace(',','').split()
            # screen_available = screen.find('div', class_='stockstatus').text.split('\n')[3].split(' ')[0]
            # if screen_available == "Ikke":
            #     screen_available = 0
            # screen_itemnumber = screen.find('div', class_='product-data').text.replace(' ', '').replace('\n', '').split('/')[0].split(':')[1]
            # screen_price = screen.find('div', class_='product-price').text.replace(',-', '').replace('NÅ', '').replace('\n','')
            #screen_link = "komplett.no{}".format(str(screen.find('div', class_='buy-button align-right')).split()[7].split('"')[1])
            # try:
            #     screen_link = "komplett.no{}".format(str(screen.find('div', class_='buy-button align-right')).split('href=')[1].split()[0].replace('>', '').replace('"',''))
            # except IndexError as error:
            #     screen_link = "No link"
            # print(f'Screen: {screen_name}')
            # print(f'\tPrice: {screen_price}')
            # print(f'\tStats: {screen_stats}')
            # print(f'\tAvailable: {screen_available}')
            # print(f'\tLink: {screen_link}')
            
            
            
        


         
        
        
# def scrap():
#     # Save page
#     url="https://webscraper.io/test-sites/e-commerce/allinone"
#     page=urlopen(url)
#     # Read data on page
#     html_bytes=page.read()
#     # Decode data from page
#     html=html_bytes.decode("utf-8")
#     # Write html file from data scrapped
#     with open("tmp.html","w",encoding="utf-8")as html_file:
#         html_file.write(html)
#     # Read html file from scrapped data
#     with open("tmp.html","r",encoding='utf-8')as html_file:
#         output_json=html_to_json.convert(html_file)
#     # Delete tmp.html
#     #os.remove("tmp.html")
#     # Read output_json and write it to txt file    
#     with open("sample.json", 'w', encoding='utf-8') as f:
#         json.dump(output_json, f, ensure_ascii=False, indent=4)





def main():
    do_scrap = False
    if do_scrap:
        try:
            scrap()
            print("Done!")
        except ValueError as VError:
            print(f"ValueError {VError}")
        except HTTPError as HError:
            print(f"ValueError {HError}")
        except URLError as UError:
            print(f"URLError {UError}")
    else:
        #read_skjerm()
        read_tastatur()
            

# Run program      
main()