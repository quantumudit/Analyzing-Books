from datetime import datetime

from art import scraper_title, scraper_art
from cls_scraper import Scraper

books = Scraper()

if books.response_status() == 200:
    print(scraper_art)
    print(scraper_title)
    print('\n')
    print('Collecting Books...')

    start_time = datetime.now()

    books.scrape_genres()

    print(f'Total genres to scrape: {len(books.all_genres)}')

    for genre_tuple in books.all_genres:
        genre_name = genre_tuple[0]
        genre_link = genre_tuple[1]

        print('\n')
        print(f'Scraping Genre: {genre_name}')

        books.scrape_genre_books(genre_tuple)

        print(f'Total Books Collected: {len(books.all_books)}')

    end_time = datetime.now()
    scraping_time = end_time - start_time

    print('\n')
    print('All Books Collected...')
    print(f'Time spent on scraping: {scraping_time}')
    print(f'Total books collected: {len(books.all_books)}')
    print('\n')
    print('Loading data into CSV...')

    books.load_data()

    print('Data Exported to CSV...')
    print('Web Scraping Completed !!!')
