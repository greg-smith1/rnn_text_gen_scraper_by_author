import requests
import re
import time
import urllib
from tqdm import tqdm
from bs4 import BeautifulSoup

# example link --> https://www.theguardian.com/sport/2018/jun/08/danny-rose-story-take-care-of-elite-athletes?CMP=twt_gu

def get_text(link):
    page = requests.get('{}'.format(link), headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',})

    soup = BeautifulSoup(page.text, 'html.parser')

    text = soup.find_all('p')
    #print(len(text))
    
    corpus = []

    for _ in text:
        if 'EDT' not in str(_) and 'Last modified on' not in str(_) and 'Contact author' not in str(_):
            #print(_, '\n')
            _ = str(_).replace('”', '')
            _ = str(_).replace('“', '')
            corpus.append(_)
            #_ = str(_)
            #_ = re.sub('<.*?>','',_, flags=re.DOTALL)
    corpus = ''.join(corpus)
    corpus = str(corpus)
    corpus = re.sub('<.*?>','',corpus, flags=re.DOTALL)
    return corpus

def print_text(link_list):
    with open('{}'.format(link_list), 'r') as f:
        links = f.readlines()
        #for num in range (10):
        #    print(links[num])
        for link in tqdm(links):
            #print(link)
            link = link.strip()
            link = "{}".format(link.encode('utf-8'))
            print(link)
            text = get_text(link)
            print(text)
            with open('training_text_data.txt', 'a+') as d:
                d.write("{}\n".format(text))
            time.sleep(2)

#url = www.theguardian.com/sport/2018/jun/08/danny-rose-story-take-care-of-elite-athletes?CMP=twt_gu
#new_string = ur'url'
#print(get_text(url))
print(get_text('https://www.theguardian.com/football/blog/2018/may/26/liverpool-mohamed-salah-cruel-end-real-madrid-sergio-ramos-champions-league'))
#print(get_text('https://www.theguardian.com/sport/2018/jun/08/danny-rose-story-take-care-of-elite-athletes?CMP=twt_gu'))
#print_text('guardian_links.txt')