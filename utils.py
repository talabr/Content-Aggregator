import json
import requests
from bs4 import BeautifulSoup


def load_configurations():
    with open('configurations.json', 'r') as json_file:
        configurations = json.load(json_file)
    return configurations


def get_html_from_site(url):
    site_html = requests.get(url).text
    site_lxml = BeautifulSoup(site_html, 'lxml')
    return site_lxml


def find_top_news_div_from_html(site_name):
    list_of_top_news = []
    configurations = load_configurations()[site_name]
    fox_lxml = get_html_from_site(configurations["coronavirus_page_url"])
    latest_news_xml = fox_lxml.find(configurations["css_selector"],
                                    configurations["css_selector_value"])
    return list_of_top_news, configurations, latest_news_xml


def make_list_of_fox_top_news():
    list_of_top_news, configurations, latest_news_xml = find_top_news_div_from_html("fox_news")
    print(list_of_top_news)
    for article in latest_news_xml.findAll(configurations["inner_css_selector"]):
        list_of_top_news.append((article.h4.text, configurations["site_url"] + article.h4.a['href']))
    return list_of_top_news


def make_list_of_nbc_top_news():
    list_of_top_news, configurations, latest_news_xml = find_top_news_div_from_html("nbc_news")
    for l in latest_news_xml.findAll(configurations["inner_css_selector"]):
        list_of_top_news.append((l.text, l.a['href']))
    return list_of_top_news


def make_list_of_washington_post_top_news():
    list_of_top_news, configurations, latest_news_xml = find_top_news_div_from_html("washington_post")
    for div in latest_news_xml.findAll(configurations["inner_css_selector"],
                                       configurations["inner_css_selector_value"]):
        list_of_top_news.append((div.a.text, div.a['href']))
    return list_of_top_news
