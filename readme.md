# FindMoto

## Overview
FindMoto is a Notion Integration that automates the search for the freshest and best deals on motorcycles from Facebook Marketplace. The script runs as a background cron job, refreshing listings in a Notion workspace every four hours to help users quickly discover great deals before they disappear.

## Inspiration
As motorcycle enthusiasts, we found ourselves spending too much time manually browsing Facebook Marketplace for deals. We came up with this idea when we were talking about how you have to be quick to get the best deals on FB marketplace because they disappear fast. we wanted a way to automate this process and send updates to a platform we frequently use—Notion. This led to the creation of FindMoto, a tool that streamlines the discovery of fresh motorcycle deals by automatically fetching and updating listings.

## Features
- **Automated Marketplace Scraping:** Uses Selenium to scrape the first 10 freshest listings in a specified city.
- **Notion Integration:** Sends extracted data to a Notion workspace via the Notion API, creating an organized dashboard of motorcycle deals.
- **Scheduled Updates:** Runs as a cron job, refreshing listings every 4 hours to ensure users see the latest offers.

## How It Works
1. A Python script using Selenium scrapes the latest motorcycle listings from Facebook Marketplace.
2. The extracted data is formatted and structured.
3. The script sends the data to a Notion workspace using the Notion API.
4. A cron job ensures the script runs at scheduled intervals, keeping the Notion dashboard up to date.

## Installation
### Prerequisites
- Python 3.12
- Selenium
- Notion Integration Setup and Integration Secret

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/FindMoto.git
   cd FindMoto
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Notion API:
   - Create a Notion integration and obtain an API key.
   - Share your Notion database with the integration.
4. Configure cron job for automation:
   ```bash
   crontab -e
   ```
   Add the following line to run the script every 4 hours:
   ```bash
   0 */4 * * * /usr/bin/python3 /path/to/findmoto.py
   ```

## Challenges Faced
- **Web Scraping Complexity:** This was our first web scraping project, requiring deep inspection of Facebook Marketplace’s HTML structure.
- **Facebook Marketplace API Deprecation:** With no official API, we had to manually extract data.
- **Notion API Learning Curve:** Integrating with Notion was new to us, requiring adjustments to format and structure the data correctly.
- **Cron Job Setup:** Automating the script execution proved tedious but was successfully implemented.

## Accomplishments
- Successfully built an automation tool that solves a real-world problem we both faced.
- Created a local solution that runs efficiently without requiring cloud deployment.
- Developed a flexible tool that can be adapted to track deals for other products beyond motorcycles.

## Lessons Learned
- Gained deeper insight into web scraping and handling websites with dynamic content.
- Explored the power of Notion integrations for automating workflows.
- Understood the challenges and workarounds involved in dealing with deprecated APIs.

## Future Enhancements
- **GPS-Based Search:** Automate city selection using Apple’s Core Location API for more personalized searches.
- **Enhanced Security:** Improve how user location data is handled to ensure privacy.
- **Multi-Item Search:** Expand functionality to track deals on other items beyond motorcycles.

## Contributors
- **Lloyd** – Web Scraping, Cronjob Automation, Data Formatting
- **Ayad** – Notion API Integration, Web Scraping

## License
This project is licensed under the MIT License.

---
FindMoto makes motorcycle shopping easier by delivering fresh deals straight to your Notion workspace. 🚀

