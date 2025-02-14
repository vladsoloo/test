from loguru import logger
from bs4 import BeautifulSoup
import requests


class Parser:
    def init(self, title, url):
        self.title = title
        self.url = url
        self.chapter = 1
        self.chapters = {}

    def get_novel(self):
        soup = self.get_webpage(self.url)
        chapters_list = soup.find('ul', class_='list clearfix')
        element = chapters_list.find_all('a')
        links = []
        for element in elements:
            href = element.get('href')
            if href:
                links.append(href)
        
        for link in links:
            chapters_page = self.get_webpage(link)
            text = chapters_page.finde('div', class_='book_con fix')
            self.chapters.update({str{self.chapter}: link + text.text})


    def get_webpage(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"page {link} is got")
            return BeautifulSoup(response.text, "html.parser")
        else:
            logger.error(f"page {link} is not got {response.status_code}")
