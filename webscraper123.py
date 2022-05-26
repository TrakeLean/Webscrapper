from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html_to_json
import os
import json

def scrap():
    # Save page
    url = 'https://www.komplett.no/category/21656/gaming/gaming-utstyr/gamingskjermer'
    key = '1783319260d70f84da21868ce0fd6207'
    api_link = f"http://api.scraperapi.com?api_key={key}&url={url}"

    page=urlopen(api_link)
    # Read data on page
    html_bytes=page.read()
    # Decode data from page
    html=html_bytes.decode("utf-8")
    # Write html file from data scrapped
    with open("tmp.html","w",encoding="utf-8")as html_file:
        html_file.write(html)

def read():    
    # Read html file from scrapped data
    with open("tmp.html","r",encoding='utf-8')as html_file:
        output=html_file.read()
        
        soup = BeautifulSoup(output, 'lxml')
        screens = soup.find_all('div', class_ = '')



def main():
    do_scrap = True
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