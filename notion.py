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

print(get_database())


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
            "Name": {
                "title": [{"text": {"content": data["Name"]}}]
            },
            "Price": {
                "number": data["Price"]
            },
            "Location": {
                "rich_text": [{"text": {"content": data["Location"]}}]
            }
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()



data = [{
        "Name": "Ninja Kawasaki 400",
        "Price": 5000,
        "Location": "Dallas"
    },
    {
        "Name": "Suzuki Hayabusa",
        "Price": 15000,
        "Location": "Austin"
    },
    {
        "Name": "Yamaha R1",
        "Price": 12000,
        "Location": "Houston"
    }
]

for entry in data:
    add_entry(entry)

