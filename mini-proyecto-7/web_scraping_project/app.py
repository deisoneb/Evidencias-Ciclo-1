from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    try:
        url = "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        episodes = []
        tables = soup.select('table.wikitable.plainrowheaders.wikiepisodetable')

        for table in tables:
            season = table.find_previous('span', class_='mw-headline').text
            rows = table.select('tr.vevent')
            for row in rows:
                try:
                    episode_number = row.find('th').text.strip()
                    title = row.find('td', class_='summary').text.strip()
                    air_date = row.find_all('td')[-1].text.strip()
                    episodes.append({'Season': season, 'Episode Number': episode_number, 'Title': title, 'Air Date': air_date})
                except Exception as e:
                    print(f"Error extracting data from row: {e}")
                    continue
    except Exception as e:
        print(f"Error during scraping: {e}")
        episodes = []

    return render_template('index.html', episodes=episodes)

if __name__ == '__main__':
    app.run(debug=True)
