from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

FOX_NEWS_ROOT_URL = 'https://www.foxnews.com'
NBC_URL = "https://www.nbcnews.com/health/coronavirus"
CHROME_DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
FOX_URL = "https://www.foxnews.com/category/health/infectious-disease/coronavirus"
THE_WASHINGTON_POST = "https://www.washingtonpost.com/coronavirus/?itid=sf_coronavirus-living_subnav"

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
        news_list.append((article.h4.text, FOX_NEWS_ROOT_URL+article.h4.a['href']))
    return news_list


def get_news_from_washington_post():
    news_list = []
    site_url = THE_WASHINGTON_POST
    site_html = requests.get(site_url).text
    soup = BeautifulSoup(site_html, 'lxml')
    latest = soup.find("div", {"data-chain-name": "virus-stream-1"})
    for div in latest.findAll("div", {"class": "headline x-small normal-style text-align-inherit"}):
        news_list.append((div.a.text, div.a['href']))
    return news_list


def using_selenium():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get('https://www.washingtonpost.com/')
    button = driver.find_elements_by_xpath("//form[@id='search-form']")[0]
    button.click()
    # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
    #                                                             "//a[@class='vilynx_listened']"))).click()
    # WebDriverWait(driver, 50).until(ec.element_to_be_clickable((By.XPATH,
                                                                # "//div[@class='global']/span[@class='hfs-i hfs-i-search']"))).click()

    # driver.quit()
# print(get_news_from_nbc())
# print(get_news_from_fox())
# print(get_news_from_washington_post())

# using_selenium()
