import re
import sys
import urllib
import time
import requests
from bs4 import BeautifulSoup


def remove_interfere_tags(soup):
    tags = ['a', 'p', 'li', 'ol']
    for tag in soup.find_all(True):
        if tag.name not in tags:
            tag.decompose()
    return soup


def get_link(url):
    page = requests.get(url)
    if not page.status_code == 200:
        print('No such wikipedia page.')
        exit()
    soup = BeautifulSoup(page.text, 'html.parser')
    found_url = None
    content = soup.find('div', attrs={'id': 'mw-content-text'}).find('div', attrs={'class': 'mw-parser-output'})
    content = remove_interfere_tags(content)

    for a_tag in content.find_all('a'):
        if a_tag.get('href').startswith('#'):
            continue
        if a_tag.get('class') == 'new':
            continue
        if 'File:' in a_tag.get('href'):
            continue
        if 'Help:' in a_tag.get('href'):
            continue

        p_tag = a_tag.parent
        p = re.sub("[(\[].*?[)\]]", "", str(p_tag))

        if not str(a_tag.get('href')) in p:
            continue

        found_url = urllib.parse.urljoin('https://en.wikipedia.org', a_tag.get('href'))
        found_url = urllib.parse.unquote(found_url)
        break
    return found_url


if __name__ == '__main__':
    wikipedia_random_url = 'https://en.wikipedia.org/wiki/Special:Random'
    philosophy_url = 'https://en.wikipedia.org/wiki/Philosophy'
    if "--page" in sys.argv:
        result = sys.argv[2]
        if (result == '') or 'wikipedia.org' not in result:
            print('Wrong wikipedia link. Getting random article..')
            result = wikipedia_random_url
    else:
        result = wikipedia_random_url
    paths = []
    loop = False
    while result != philosophy_url:
        if result not in paths:
            paths.append(result)
        else:
            print('Loop detected!')
            exit()
        time.sleep(1)
        result = get_link(result)
        print(result)
