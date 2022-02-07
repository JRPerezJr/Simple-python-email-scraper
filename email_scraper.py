#!/usr/bin/python3
import sys
import random
from bs4 import BeautifulSoup
import requests.exceptions
import urllib.parse
from collections import deque
import re


def print_logo():
    clear = "\x1b[0m"
    colors = [31, 32, 33, 34, 35, 36]

    logo = """                                                                                                                    
   ___       _   _                     __                _ _   __                                
  / _ \_   _| |_| |__   ___  _ __     /__\ __ ___   __ _(_) | / _\ ___ _ __ __ _ _ __   ___ _ __ 
 / /_)/ | | | __| '_ \ / _ \| '_ \   /_\| '_ ` _ \ / _` | | | \ \ / __| '__/ _` | '_ \ / _ \ '__|
/ ___/| |_| | |_| | | | (_) | | | | //__| | | | | | (_| | | | _\ \ (__| | | (_| | |_) |  __/ |   
\/     \__, |\__|_| |_|\___/|_| |_| \__/|_| |_| |_|\__,_|_|_| \__/\___|_|  \__,_| .__/ \___|_|   
       |___/                                                                    |_|  
"""
    for line in logo.split("\n"):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))


print_logo()
user_url = str(input('[+] Enter Target URL To Scan: '))
urls = deque([user_url])

scraped_urls = set()
emails = set()

count = 0
try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue
        new_emails = set(re.findall(r"[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if link not in urls and link not in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

for mail in emails:
    print(mail)
