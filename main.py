# coding=utf-8
import requests
import sys
import os

home = os.getenv('HOME', 'WontExist')
dest_dir = os.path.join(home, 'Desktop')
if not os.path.exists(dest_dir):
    dest_dir = '.'

def fetch_img(img_url, name):
    req = requests.get(img_url)
    if req.status_code != 200:
        sys.stderr.write('return code for fetching img %s is not 200, abort\n' % img_url)
        return False

    sys.stdout.write('downloading %s...\n' % name)
    dest = os.path.join(dest_dir, name)
    open(dest, 'wb').write(req.content)
    return True

def using_re(url):
    import re
    pattern = re.compile('https://stickershop.line-scdn.net/stickershop/v1/sticker/(\w+)/.*/sticker.png')

    req = requests.get(url)
    if req.status_code != 200:
        sys.stderr.write('return code for fetching %s is not 200, abort\n' % url)
        return False

    for p in pattern.finditer(req.text):
        img_url, name = p.group(0), p.group(1) + '.png'
        if not fetch_img(img_url, name):
            sys.stderr.write('failed to fetch img %s, just ignore it\n' % img_url)
    return True

def using_bs(url):
    from bs4 import BeautifulSoup

    req = requests.get(url)
    if req.status_code != 200:
        sys.stderr.write('return code for fetching %s is not 200, abort\n' % url)
        return False

    soup = BeautifulSoup(req.text, 'lxml')
    stickers = soup.find_all('span', 'mdCMN09Image')
    for s in stickers:
        print s.get('style').split('(')[1].split(';')[0]

    # GG, using re is better, the string parser is not good
    return True

if __name__ == '__main__':
    for i in xrange(1, len(sys.argv)):
        url = sys.argv[i]
        using_re(url)
