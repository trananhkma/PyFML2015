#!/usr/bin/python

"""
Ket qua so xo toan quoc
"""

from bs4 import BeautifulSoup as Bs4
import requests


def main():
    url = 'http://ketqua.net/'
    r = requests.get(url)
    soup = Bs4(r.content, 'html.parser')
    target = soup.find('td', attrs={'class': 'bor f2 db'})
    return target.get_text()


if __name__ == '__main__':
    try:
        result = main()
        print 'Ket qua so xo:', result
    except AttributeError:
        print 'Ma nguon trang web da thay doi, khong the lay ket qua so xo.'
