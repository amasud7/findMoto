import requests
from dotenv import load_dotenv
import os

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


def query_database():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS, json={})
    return response.json()


def add_entry(data):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Price": {
                "number": data["Price"]
            },
            "Name": {
                "title": [{"text": {"content": data["Name"]}}]
            },
            "Mileage": {
                "number": data["Mileage"]
            },
            "Location": {
                "rich_text": [{"text": {"content": data["Location"]}}]
            },
            "Image": {
                "files": [ {"name": "image", "type": "external", "external": {"url": data["Image"]} } ]
            },
            "Link": {
                "url": data["Link"]
            }
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()
