import logging
import random
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import os

# returns a list of Ultimate Guitar index page links - these can be used to get links to the song pages
# can specific start, stop, step numbers to limit the number of pages if desired
def get_index_pages(start, stop, step):
    base_url = "https://www.ultimate-guitar.com/explore?order=hitstotal_desc&page={}&type[]=Chords"
    idxs = [base_url.format(page) for page in range(start, stop + 1, step)]
    # print(len(urls))
    return idxs

# from within the index pages, get a list of links to the song pages
def get_song_pages(index_pages):

    link_list = []

    for url in index_pages:
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        html_content = response.text

        if response.status_code == 200:

            soup = BeautifulSoup(html_content, 'html.parser')

            data_content = soup.find('div', class_='js-store')['data-content']
            data = json.loads(data_content)

            page_dict = data['store']['page']['data']['data']['tabs']

            for d in page_dict:
                print(d['tab_url'])
                link_list.append(d['tab_url'])
                # delay = random.randint(2,3)
                delay = random.uniform(1.5, 3.5)
                print(f"Sleeping for {delay:.2f} seconds")
                time.sleep(delay)

    return link_list

# takes in a ultimate guitar song page and returns only the chords for that song as a string
def get_chord_data(url):
    print("in get chord data")
    print(url)
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


def write_chords_to_csv(urls, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Chords'])

        for url in urls:
            print(url)
            chords = get_chord_data(url)
            if chords:
                writer.writerow([url, chords])
            delay = random.uniform(1.5, 3.5)
            print(f"Sleeping for {delay:.2f} seconds")
            time.sleep(delay)
            print(f"done with writing chords for {url}")
    abs_path = os.path.abspath(filename)
    print(f"All URLs processed. Data saved to {abs_path}")


if __name__ == '__main__':
    #
    idxs = get_index_pages(1,1,1)
    # print(idxs)
    song_pages = get_song_pages(idxs)
    print("----------------------------------------------")
    test = song_pages[0:20]
    print(test)
    print(song_pages)

    write_chords_to_csv(test, 'chords.csv')


# # song data for testing
#     song1 = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/take-me-out-to-the-ball-game-chords-653035')
#     print(song1)
#     song2 = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-chords-1084205')
#     print(song2)
#     song3 = get_chord_data('https://tabs.ultimate-guitar.com/tab/irving-berlin/all-by-myself-chords-2762746')
#     print(song3)
#     songs = [song1, song2, song3]
#     print()
#     print(songs)