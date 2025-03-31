from src.notion import add_entry
from src.scrape import build_url, get_listings

def main():
    data = build_url('austin')
    listings = get_listings(data)

    for listing in listings:
        add_entry(listing)

if __name__ == '__main__':
    main()