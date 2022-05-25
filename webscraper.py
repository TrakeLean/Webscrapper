from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import html_to_json
import json

def scrap():
    # Save page
    #url="Komplett.no"
    #url="https://www.komplett.no/category/16075/datautstyr/lagring/harddiskerssd/ssd-m2"
    url="https://generated.photos/face-generator/new"
    #url="https://webscraper.io/test-sites/e-commerce/allinone"
    page=urlopen(url)
    # Read data on page
    html_bytes=page.read()
    # Decode data from page
    html=html_bytes.decode("utf-8")
    # Write html file from data scrapped
    with open("sample.html","w",encoding="utf-8")as html_file:
        html_file.write(html)
    # Read html file from scrapped data
    with open("sample.html","r",encoding='utf-8')as html_file:
        output_json=html_to_json.convert(html_file)
    # Read output_json and write it to txt file    
    with open("sample.txt", 'w', encoding='utf-8') as f:
        json.dump(output_json, f, ensure_ascii=False, indent=4)





def main():
    # True = Scrap | False = Read
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
        print("asd")    

    


# Run program      
main()