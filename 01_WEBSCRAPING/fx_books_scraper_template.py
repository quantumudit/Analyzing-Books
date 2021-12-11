import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timezone

SESSION = requests.Session()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "accept-language": "en-US"
}

all_books = []
all_genres = []

def extract_genres() -> None:
    """
    This function extracts all the 'genre name' and 'genre URL' as a tuple and appends each to 'all_genres' list
    """
    
    root_url = "https://books.toscrape.com/"
    response = SESSION.get(root_url, headers=HEADERS)

    soup = BeautifulSoup(response.content, 'lxml')
    genre_list_content = soup.find('ul', class_ = 'nav nav-list').find('li').find('ul').find_all('li')

    for genre in genre_list_content:
        
        genre_name = genre.find('a').text.strip()
        
        genre_partial_url = genre.find('a')['href']
        genre_full_url = urljoin(root_url, genre_partial_url)

        genre_details = (genre_name, genre_full_url)

        all_genres.append(genre_details)
    return

def scrape_content(genre_tuple: tuple) -> None:
    """
    This functions takes a tuple extracted from 'extract_genre()' that contains the 'genre name' and 'genre start page URL' as an input argument; scrapes the books and its related feature and adds them to 'all_books' list.
    Args: 
        genre_tuple (tuple): a tuple with 'genre name' and 'genre start page URL'
    Returns:
        None: This function returns nothing but adds the data to the 'all_books' list
    """
    
    utc_timezone = timezone.utc
    current_utc_timestamp = datetime.now(utc_timezone).strftime('%d-%b-%Y %H:%M:%S')
    
    root_url = "https://books.toscrape.com/"
    
    genre_name = genre_tuple[0]
    page_url = genre_tuple[1]
    
    response = SESSION.get(page_url, headers=HEADERS)
    
    soup = BeautifulSoup(response.content, 'lxml')
    content = soup.select('article.product_pod')
    
    for book in content:
        
        name = book.select('h3 a')[0]['title']
        price = book.find('p', class_= 'price_color').text.replace('£','')
        availability = book.find('p', class_= 'availability').text.strip().replace('\n', '')
        stars = book.select('p.star-rating')[0]['class'][1]
        book_partial_image_link = book.select('div.image_container a img')[0]['src']
        book_image_link = urljoin(root_url, book_partial_image_link)

        book_details = {
            "title": name,
            "genre": genre_name,
            "price": price,
            "star_rating": stars,
            "stock_availability": availability,
            "book_image": book_image_link,
            "last_updated_at_UTC": current_utc_timestamp
        }

        all_books.append(book_details)
    return

def extract_nextpage_link(genre_tuple: tuple) -> str:
    """
    This function checks whether the 'next page' button is present in the webpage or, not and returns the value accordingly.
    Args:
        page_url (str): This is the input page URL
    Returns:
        str: next page URL; if it exists, otherwise, the function will return "None"
    """
    
    page_url = genre_tuple[1]
    response = SESSION.get(page_url, headers=HEADERS)
    
    soup = BeautifulSoup(response.content, 'lxml')
    
    if soup.find('li', class_= 'next') is not None:
        next_page_partial_link = soup.find('li', class_= 'next').find('a')['href']
        next_page_link = urljoin(page_url, next_page_partial_link)
    else:
        next_page_link = None
    return next_page_link

# Testing the scraper template #
# ---------------------------- #

if __name__ == '__main__':
    
    extract_genres()
    
    print('\n')
    print(f'Total genres to scrape: {len(all_genres)}')
    print('\n')
    
    genre_tuple = ("Sequential Art", "https://books.toscrape.com/catalogue/category/books/sequential-art_5/")
    
    scrape_content(genre_tuple)
    
    print('\n')
    print(f'Total books scraped: {len(all_books)}')
    print('\n')
    print(all_books)
    
    print('\n')
    print(f"Does next page exists? : {extract_nextpage_link(genre_tuple) != None}")
    print('\n')
    print(f"Next Page URL: {extract_nextpage_link(genre_tuple) }")