"""
Books to Scrape Website Scraper
=================================

Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=================================

This script collects relevant data from the https://books.toscrape.com/ website using the requests and BeautifulSoup
modules, and stores the data in a CSV file. The functional programming approach has been used in the script,
where specific functions have been created to perform the web scraping tasks. The functions included are:

- scrape_genres: This function returns a list of tuples, each tuple representing a genre and its associated link.
- scrape_content: This function scrapes and returns a list with complete details for all books in a specific genre.
"""

# imports
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timezone
from csv import DictWriter
from art import scraper_title, scraper_art

# setting root URL and session with headers
ROOT_URL = "https://books.toscrape.com/"
SESSION = requests.Session()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "accept-language": "en-US"
}


# ========== Helper Functions ========== #

def scrape_genres() -> list:
    """
    This function returns a list having tuples for each genre and its link.
    """

    # initializing list to store all genres
    genres = []

    # sending request to root URL and fetching content
    resp = SESSION.get(ROOT_URL, headers=HEADERS)
    soup = BeautifulSoup(resp.content, 'lxml')
    genre_list_content = soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li')

    # looping through the genres list to fetch name and link of each genre
    for genre in genre_list_content:
        gen_name = genre.find('a').text.strip()

        genre_partial_url = genre.find('a')['href']
        genre_full_url = urljoin(ROOT_URL, genre_partial_url)

        genre_details = (gen_name, genre_full_url)
        genres.append(genre_details)
    return genres


def scrape_content(gen_tuple: tuple) -> list:
    """
    This functions takes a tuple that contains the 'genre name' and
    'page URL' as an input argument to scrape the books and its related feature and
    returns a list with all the book details from the genre
    """

    # initializing list to store all books details for the genre
    all_genre_books = []

    # fetching the UTC timezone and current timestamp
    utc_timezone = timezone.utc
    current_utc_timestamp = datetime.now(utc_timezone).strftime('%d-%b-%Y %H:%M:%S')

    # fetching genre name and link from the input argument
    gen_name = gen_tuple[0]
    page_url = gen_tuple[1]

    # looping through the pages of the genre
    while True:

        # sending request to the page URL and fetching content
        resp = SESSION.get(page_url, headers=HEADERS)
        soup = BeautifulSoup(resp.content, 'lxml')
        content = soup.select('article.product_pod')

        # looping through the books and fetching details
        for book in content:
            name = book.select('h3 a')[0]['title']
            price = book.find('p', class_='price_color').text.replace('£', '')
            availability = book.find('p', class_='availability').text.strip().replace('\n', '')
            stars = book.select('p.star-rating')[0]['class'][1]

            book_partial_image_link = book.select('div.image_container a img')[0]['src']
            book_image_link = urljoin(ROOT_URL, book_partial_image_link)

            book_details = {
                "title": name,
                "genre": gen_name,
                "price": price,
                "star_rating": stars,
                "stock_availability": availability,
                "book_image": book_image_link,
                "last_updated_at_UTC": current_utc_timestamp
            }

            all_genre_books.append(book_details)

        # checking for next page presence for the genre
        if soup.find('li', class_='next') is not None:
            next_page_partial_link = soup.find('li', class_='next').find('a')['href']
            next_page_link = urljoin(page_url, next_page_partial_link)
            page_url = next_page_link
        else:
            break

    return all_genre_books


# ========== Web Scraping & Data Load ========== #

if __name__ == '__main__':

    # sending request to get response code
    response = SESSION.get(ROOT_URL, headers=HEADERS)
    status = response.status_code

    if status != 200:
        print(f"The status code is: {status}. Web scraping is not possible")
    else:
        print(scraper_art)
        print(scraper_title)
        print('\n')
        print('Collecting Books...')

        # initializing list to store all books
        all_books = []

        # logging the web scraping start time
        start_time = datetime.now()

        # scraping all genres
        all_genres = scrape_genres()
        print(f'Total genres to scrape: {len(all_genres)}')

        # looping through each genre_tuple and scraping data
        for genre_tuple in all_genres:
            genre_name = genre_tuple[0]
            genre_link = genre_tuple[1]

            print('\n')
            print(f'Scraping Genre: {genre_name}')

            genre_books = scrape_content(genre_tuple)
            all_books = all_books + genre_books

            print(f'Total Books Collected: {len(all_books)}')

        # logging the web scraping start time and finding time elapsed
        end_time = datetime.now()
        scraping_time = end_time - start_time

        print('\n')
        print('All Books Collected...')
        print(f'Time elapsed on scraping: {scraping_time}')
        print(f'Total books collected: {len(all_books)}')
        print('\n')
        print('Loading data into CSV...')

        # writing scraped data into a CSV file
        with open('scraped_data.csv', 'w', newline='') as f:
            csv_writer = DictWriter(f, fieldnames=["title", "genre", "price", "star_rating",
                                                   "stock_availability", "book_image", "last_updated_at_UTC"])
            csv_writer.writeheader()
            csv_writer.writerows(all_books)

        print('Data Exported to CSV...')
        print('Web Scraping Completed !!!\n')
