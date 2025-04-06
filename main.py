from src.notion import add_entry, query_database
from src.scrape import build_url, get_listings
from urllib.parse import urlparse

def get_base_url(url):
    parsed = urlparse(url)
    # Only keep the path, which includes /marketplace/item/{item_id}/
    return parsed.scheme + "://" + parsed.netloc + parsed.path

def main():
    db = query_database()
    db_length = len(db['results'])

    # Identifier of a duplicate listing, converted to set for 0(1) lookup time
    links = set( [ get_base_url(db['results'][i]['properties']['Link']['url']) for i in range(db_length) ] )

    data = build_url('austin')
    listings = get_listings(data)

    for listing in listings:
        base_url = get_base_url(listing['Link'])
        if base_url not in links: # Prevents duplicate listings from being added
            add_entry(listing)

if __name__ == '__main__':
    main()
    