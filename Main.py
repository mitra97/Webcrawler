import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://chambana.craigslist.org/search/apa?s=' + str(100 * page - 100)
        source_code = requests.get(url) #gets website source code
        plain_text = source_code.text   #gets just the text of the source code
        soup = BeautifulSoup(plain_text, "html.parser") #converts the plain text to a beautiful soup object
        for alt in soup.find_all('p', {'class': 'result-info'}):
            for costs in alt.find_all('span', {'class':"result-price"}):
                cost = costs.string
                print(cost, end = " ")
            for link in alt.find_all('a',{'class': 'result-title hdrlnk'}):
                href = 'https://chambana.craigslist.org' + link.get('href')
                title = link.string
                print(title)
                print(href)
        page+=1

spider(25)
