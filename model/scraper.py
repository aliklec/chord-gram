import logging
import re
from urllib.error import HTTPError, URLError
import requests
from bs4 import BeautifulSoup

def get_chord_data(url):

    validsite = 'https://tabs.ultimate-guitar.com'
    if not url.startswith(validsite):
        print("Scraper only works for Ultimate Guitar chords")
        return None

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        html_content = response.text

        if response.status_code == 200:
            soup = BeautifulSoup(html_content, 'html.parser')

            matches = re.findall(r'\[ch\](.*?)\[/ch\]', str(soup))

            string = ' '.join(matches)
            return string

    except HTTPError as e:
        logging.error(f"HTTP error: {e}")
        print(f"HTTP error: {e}")

    except URLError as e:
        logging.error(f"URL error: {e}")
        print(f"URL error: {e}")

    except Exception as e:
        logging.error(f"There was an error: {e}")
        print(f"There was an error: {e}")

if __name__ == '__main__':
#     test = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/greensleeves-chords-173713')
#     test2 = get_chord_data('www.test.com')
#     print(test)
#     print(test2)

# song data for testing
    song1 = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/take-me-out-to-the-ball-game-chords-653035')
    print(song1)
    song2 = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-chords-1084205')
    print(song2)
    song3 = get_chord_data('https://tabs.ultimate-guitar.com/tab/irving-berlin/all-by-myself-chords-2762746')
    print(song3)
    songs = [song1, song2, song3]
    print()
    print(songs)