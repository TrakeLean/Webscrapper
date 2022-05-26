from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html_to_json
import os
import json

def scrap():
    # Save page
    url = 'https://www.elkjop.no/pc-datautstyr-og-kontor/skjermer-og-tilbehor/pc-skjerm/page-0'
    key = '1783319260d70f84da21868ce0fd6207'
    api_link = f"http://api.scraperapi.com?api_key={key}&url={url}"

    page=urlopen(api_link)
    # Read data on page
    html_bytes=page.read()
    # Decode data from page
    html=html_bytes.decode("utf-8")

    # Write html file from data scrapped
    with open("elkjop/skjerm.html","w",encoding="utf-8")as html_file:
        html_file.write(html)

def read():    
    # Read html file from scrapped data
    with open("elkjop/skjerm.html","r",encoding='utf-8')as html_file:
        output=html_file.read()
        
        soup = BeautifulSoup(output, 'lxml')
        screens = soup.find('div', 'product-tile__information information')
        screen_dict = {}
        all_screens = []
        screen_name = screens.h2
        print(screen_name)
        # for screen in screens:
        #     screen_name = 
        #     #screen_stats = 
        #     #screen_available = 
        #     #screen_available =
        #     #screen_itemnumber = 
        #     #screen_price = 
        #     #screen_link = 
        #     print(f'Screen: {screen_name}')
        #     # print(f'\tPrice: {screen_price}')
        #     # print(f'\tStats: {screen_stats}')
        #     # print(f'\tAvailable: {screen_available}')
        #     # print(f'\tLink: {screen_link}')
            

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
        read()
            

# Run program      
main()