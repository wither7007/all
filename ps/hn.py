import requests
from bs4 import BeautifulSoup as bs


def extract_news(url):
    print('HN Top Stories:n'+'-'*50+'-'*50)
#    content = urllib2.urlopen(url).read()
    page_raw = requests.get(url).text

    soup = bs(page_raw,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        print(str(i+1)+' :: '+tag.text +  '-'*5) if tag.text!='More' else ''
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    print('End') 
extract_news('https://news.ycombinator.com/')
