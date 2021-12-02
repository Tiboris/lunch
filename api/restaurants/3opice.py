# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "U 3 Opic"
URL = "https://www.menicka.cz/3225-u-3-opic-.html"
RESTAURANT_ID = "3225"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
