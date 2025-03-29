import requests
from dotenv import load_dotenv
import os
import scrape

load_dotenv()
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def get_database():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# print(get_database())


def query_database():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS, json={})
    return response.json()

# print(query_database())

def add_entry(data):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            # "cover": {
            #     "type": "file",
            #     "file": [ {"name": "image", "type": "external", "external": {"url": data["Image"]}} ]
            # },
            "Price": {
                "number": data["Price"]
            },
            "Name": {
                "title": [{"text": {"content": data["Name"]}}]
            },
            "Location": {
                "rich_text": [{"text": {"content": data["Location"]}}]
            },
            "Mileage": {
                "number": data["Mileage"]
            },
            "Image": {
                "files": [ {"name": "image", "type": "external", "external": {"url": data["Image"]}} ]
            },
            "Link": {
                "url": data["Link"]
            }
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()



# data = [ {
#     "Price": 5000,
#     "Name": "2023 Harley Davidson",
#     "Location": "Dallas, TX",
#     "Mileage": 2000,
#     "Image": "https://scontent.fftw1-1.fna.fbcdn.net/v/t39.30808-6/486700650_10237644108188379_8841458980709029598_n.jpg?stp=c256.0.1537.1537a_dst-jpg_s600x600_tt6&_nc_cat=100&ccb=1-7&_nc_sid=454cf4&_nc_ohc=hO7Nr4tmcJsQ7kNvgE745Mm&_nc_oc=Adm2fw-Fi46dN7bDw84hGm3-rwZAAYFYY2h3bryyUXpMopuFjwjGrt3ikWPx8TFStUA&_nc_zt=23&_nc_ht=scontent.fftw1-1.fna&_nc_gid=K7-hIvZ7p1zWC9qS65_J-A&oh=00_AYHJw_quenWpXpeTG8uJ_dYQI2zBzQI_Vn-zG6XylpAvMg&oe=67EE02A9",
#     "Link": "https://www.google.com"
#     }
# ]

data = scrape.build_url()
listings = scrape.get_listings(data)

for listBody in listings:
    for item in listBody:
        add_entry(item)

