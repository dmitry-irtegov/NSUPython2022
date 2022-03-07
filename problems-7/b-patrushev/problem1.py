#!/usr/bin/env python3
"""
This module implements solution for problem 1 in Problems-7 [1]
[1]: http://parallels.nsu.ru/~fat/Python/problems-7.pdf
"""

import argparse
import requests
from bs4 import BeautifulSoup
import sys
import urllib
import time
import re


def remove_tags(soup):
    """
    Returns the soup with only whitelist tags
    :param soup: BeautifulSoup object
    :return: BeautifulSoup object with only whitelist tags
    """
    whitelist = ['a','p','ul','ol','li']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.decompose()
    return soup


def get_first_link(url):
    """
    Returns first link of wiki page by defined rules in task
    :param url: URL of wiki page
    :return: first URL in given page
    """
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        exit()


    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    first_url = None

    try:
        article_content = soup.find('div', attrs={'id': 'mw-content-text'}).find('div', attrs={'class': 'mw-parser-output'})
        article_content = remove_tags(article_content)
    except AttributeError as e:
        print(f'Something wrong with url: {url}\n{e}')
        exit()
    except Exception as e:
        print(e)
        exit()


    for a in article_content.find_all('a'):
        if a.get('class') == 'new':
            continue
        if a.get('href').startswith('#'):
            continue
        if 'File:' in a.get('href'):
            continue
        if 'Help:' in a.get('href'):
            continue

        parent = a.parent
        in_parentheses = False

        for p in re.findall('\(([^)]+)', str(parent)):
            if str(a) in p:
                in_parentheses = True
                break

        if in_parentheses:
            continue

        first_url = a.get('href')
        break
    first_url = urllib.parse.urljoin(url, first_url)
    return first_url


def getting_to_philosophy(url):
    """
    Prints visited urls and result of "Getting to philosophy"
    :param url: URL of wiki page
    """
    history = []
    found = False
    cycle = False
    no_links = False

    while not found and not cycle and not no_links:
        url = get_first_link(url)
        print(url)

        if url == None:
            no_links = True
        elif url in history:
            cycle = True
        elif url == end_url:
            found = True
        else:
            history.append(url)
        time.sleep(1)

    if cycle:
        print('Cycle - philosophy not found')
    elif no_links:
        print('No links in article - philosophy not found')
    elif found:
        print('Philosophy found!')


if __name__ == '__main__':
    wiki_url = 'https://en.wikipedia.org/wiki/'
    end_url = wiki_url + 'Philosophy'
    random_wiki = wiki_url + 'Special:Random'

    parser = argparse.ArgumentParser(description='Wikipedia: Getting to Philosophy')
    parser.add_argument('-u', '--url', type=str, help='wiki url article to start from')
    parser.add_argument('-w', '--wiki', type=str, help='wiki article to start from')

    args = parser.parse_args()

    if args.url:
        if 'wikipedia.org' in args.url:
            start_url = args.url
        else:
            print('URL doesn\'t contain wiki page. Try again')
            exit()
    elif args.wiki:
        start_url = wiki_url + args.wiki
    else:
        start_url = random_wiki
    try:
        getting_to_philosophy(start_url)
    except KeyboardInterrupt:
            print()
            exit(0)
    except Exception as e:
        print(e)

