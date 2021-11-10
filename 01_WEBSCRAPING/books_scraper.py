import pandas as pd
import time
import pyfiglet
from fx_books_scraper_template import *

def main() -> None:
    """
    This function loops through all the page links to scrape data
    """    
    
    for genre_tuple in all_genres:
        
        genre_name = genre_tuple[0]
        genre_link = genre_tuple[1]
        
        print('\n')
        print(f'Scraping Genre: {genre_name}')
        
        while True:
            
            print(f'Scraping Genre URL: {genre_tuple[1]}')
            
            scrape_content(genre_tuple)
            time.sleep(0.5)
            
            print(f'Total Books Collected: {len(all_books)}')
            print('\n')
            
            if extract_nextpage_link(genre_tuple) == None:
                break
            else:
                next_page_link = extract_nextpage_link(genre_tuple)
                genre_tuple = (genre_name, next_page_link)

def load_data() -> None:
    """
    This function loads the scraped data into a CSV file
    """
    
    books_df = pd.DataFrame(all_books)
    books_df.to_csv('books_data.csv', index=False)

if __name__ == '__main__':
    
    scraper_title = "BOOKS DATA COLLECTOR"
    ascii_art_title = pyfiglet.figlet_format(scraper_title, font='small')
    
    print('\n\n')
    print(ascii_art_title)
    print('Collecting Books...')
    
    start_time = datetime.datetime.now()
    
    extract_genres()
    
    print(f'Total genres to scrape: {len(all_genres)}')
    
    main()
    
    end_time = datetime.datetime.now()
    scraping_time = end_time - start_time
    
    print('\n')
    print('All Books Collected...')
    print(f'Time spent on scraping: {scraping_time}')
    print(f'Total beers grabbed: {len(all_books)}')
    print('\n')
    print('Loading data into CSV...')
    
    load_data()
    
    print('Data Exported to CSV...')
    print('Webscraping completed !!!')