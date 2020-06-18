from bs4 import BeautifulSoup
import requests

FOX_NEWS_ROOT_URL = 'https://www.foxnews.com'
FOX_URL = "https://www.foxnews.com/category/health/infectious-disease/coronavirus"
NBC_URL = "https://www.nbcnews.com/health/coronavirus"
THE_WASHINGTON_POST = "https://www.washingtonpost.com/coronavirus/?itid=nb_hp_coronavirus"

# coronavirous news!


def get_news_from_nbc():
    news_list = []
    site_url = NBC_URL
    site_html = requests.get(site_url).text
    nbc_soup = BeautifulSoup(site_html, 'lxml')
    nbc_latest_news = nbc_soup.find("div", {"class": "package-grid__column"})
    for l in nbc_latest_news.findAll('li'):
        news_list.append((l.text, l.a['href']))
    return news_list


def get_news_from_fox():
    news_list = []
    site_url = FOX_URL
    site_html = requests.get(site_url).text
    soup = BeautifulSoup(site_html, 'lxml')
    latest = soup.find("div", {"class": "content article-list"})
    for article in latest.findAll('article'):
        news_list.append((article.text, FOX_NEWS_ROOT_URL+article.a['href']))
    return news_list


def get_news_from_washington_post():
    news_list = []
    site_url = THE_WASHINGTON_POST
    site_html = requests.get(site_url).text
    soup = BeautifulSoup(site_html, 'lxml')
    latest = soup.find("div", {"class": "chain-content no-skin clear"})
    for section in latest.findAll('a'):
        # print(section)
        print(section.text)
        print(section['href'])
        # news_list.append((section.text, FOX_NEWS_ROOT_URL+section.a['href']))
    return news_list


# print(get_news_from_nbc())
print(get_news_from_fox())
# print(get_news_from_washington_post())
