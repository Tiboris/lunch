# -*- coding: utf-8 -*-
from datetime import date
from .utils import fetch_html

NAME = "Rubín"
URL = "http://restauracerubin.cz/"
GPS = (49.218438061027825, 16.576717845038438)


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        for table in html.find_all("table", class_="menu_table"):
            for tr in table.find_all("tr"):
                cells = [td.text.strip() for td in tr.find_all("td")]
                result.setdefault(today, []).append(' '.join(cells))

    return result
