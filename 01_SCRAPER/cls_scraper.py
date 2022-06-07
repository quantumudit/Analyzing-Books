import time
from datetime import datetime, timezone
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

ROOT_URL = "https://books.toscrape.com/"
SESSION = requests.Session()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "accept-language": "en-US"
}


class Scraper:
    def __init__(self):
        self.all_genres = []
        self.all_books = []

    @staticmethod
    def response_status():
        response = SESSION.get(ROOT_URL, headers=HEADERS)
        return response.status_code

    def scrape_genres(self) -> None:
        """
        This function neither takes an argument nor returns anything but, scrapes and adds
        all the genre URLs and genre name to a list.
        """
        response = SESSION.get(ROOT_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'lxml')
        genre_list_content = soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li')

        for genre in genre_list_content:
            genre_name = genre.find('a').text.strip()

            genre_partial_url = genre.find('a')['href']
            genre_full_url = urljoin(ROOT_URL, genre_partial_url)

            genre_details = (genre_name, genre_full_url)
            self.all_genres.append(genre_details)
        return

    def scrape_content(self, genre_tuple: tuple) -> None:
        """
        This functions takes a tuple that contains the 'genre name' and
        'page URL' as an input argument to scrape the books and its related feature and adds them to a list.
        """

        utc_timezone = timezone.utc
        current_utc_timestamp = datetime.now(utc_timezone).strftime('%d-%b-%Y %H:%M:%S')

        genre_name = genre_tuple[0]
        page_url = genre_tuple[1]

        response = SESSION.get(page_url, headers=HEADERS)

        soup = BeautifulSoup(response.content, 'lxml')
        content = soup.select('article.product_pod')

        for book in content:
            name = book.select('h3 a')[0]['title']
            price = book.find('p', class_='price_color').text.replace('£', '')
            availability = book.find('p', class_='availability').text.strip().replace('\n', '')
            stars = book.select('p.star-rating')[0]['class'][1]

            book_partial_image_link = book.select('div.image_container a img')[0]['src']
            book_image_link = urljoin(ROOT_URL, book_partial_image_link)

            book_details = {
                "title": name,
                "genre": genre_name,
                "price": price,
                "star_rating": stars,
                "stock_availability": availability,
                "book_image": book_image_link,
                "last_updated_at_UTC": current_utc_timestamp
            }

            self.all_books.append(book_details)
        return

    @staticmethod
    def scrape_next_page_link(genre_tuple: tuple) -> str:
        """
        This functions takes a tuple that contains the 'genre name' and
        'page URL' as an input argument to checks whether the 'next page' button is present or, not.
        It returns the next page URL, if exists, otherwise, it returns 'None'.
        """

        page_url = genre_tuple[1]
        response = SESSION.get(page_url, headers=HEADERS)

        soup = BeautifulSoup(response.content, 'lxml')

        if soup.find('li', class_='next') is not None:
            next_page_partial_link = soup.find('li', class_='next').find('a')['href']
            next_page_link = urljoin(page_url, next_page_partial_link)
        else:
            next_page_link = None
        return next_page_link

    def scrape_genre_books(self, genre_tuple: tuple):
        """
        This function takes a tuple that contains the 'genre name' and 'page URL' as an input argument to
        scrapes all the books in that particular genre. It loops through all the pages of that genre, if exists,
        to scrape all the content of a genre.
        """

        genre_name = genre_tuple[0]

        while True:
            self.scrape_content(genre_tuple)

            time.sleep(0.5)

            if self.scrape_next_page_link(genre_tuple) is None:
                break
            else:
                next_page_link = self.scrape_next_page_link(genre_tuple)
                genre_tuple = (genre_name, next_page_link)
        return

    def load_data(self) -> None:
        """
        This function neither takes an argument nor returns anything but, loads the scraped data into a CSV file.
        """

        books_df = pd.DataFrame(self.all_books)
        books_df.to_csv('scraped_data.csv', encoding='utf-8', index=False)
        return
