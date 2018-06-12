import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_links(page_num):
    if page_num > 1:
        page = requests.get('https://www.theguardian.com/profile/barneyronay?page={}'.format(page_num), headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',})
    else:
        page = requests.get('https://www.theguardian.com/profile/barneyronay', headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',})
    soup = BeautifulSoup(page.text, 'html.parser')

    #article_list = soup.find_all(class_='fc-container__inner')
    #article_list_1 = soup.find(class_='fc-container__inner')
    article_list_2 = soup.find_all(class_='fc-container fc-container--has-show-more fc-container--tag ')
    #article_list_3 = soup.find_all(class_='fc-container fc-container--tag ')
    #article_list_4 = soup.find_all(class_='fc-container--rolled-up-hide fc-container__body')
    #print(len(article_list_2))
    # Pull text from all instances of <a> tag within BodyText div
    article_list_items_ = []
    try:
        for _ in article_list_2:
            for item in _.find_all('a'):
                #print(item)
                article_list_items_.append(str(item))
    except:
        pass
    """
    try:
        for item in article_list_1.find_all('a'):
            print(item)
            article_list_items_.append(str(item))
    except:
        pass
    try:
        for item in article_list_2.find_all('a'):
            article_list_items_.append(str(item))
    except:
        pass
    try:
        for item in article_list_3.find_all('a'):
            article_list_items_.append(str(item))
    except:
        pass
    try:
        for item in article_list_4.find_all('a'):
            article_list_items_.append(str(item))
    except:
        pass
    """
    #article_list_items_.append(article_list_1.find_all('a'))
    #article_list_items.append(article_list_2.find_all('a'))
    #article_list_items_ = article_list_1.find_all('a')
    #article_list_items = article_list_2.find_all('a')
    #print(len(article_list_items_))
    link_list = []

    for item in article_list_items_:
        item = item.split('href="')[1]
        item = item.split('"')[0]
        if item not in link_list and 'audio' not in item:
            link_list.append(item)

    #article_list_items_ = list(set(article_list_items_))

    return link_list


with open('guardian_links.txt', 'a+') as f:
    for i in tqdm(range(1,141)):
        links = get_links(i)
        #print(len(links))
        for link in links:
            f.write("{}\n".format(link))
        time.sleep(2)